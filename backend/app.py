from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.stem import LancasterStemmer
import pickle
import numpy as np
import json
import random
from tensorflow.keras.models import load_model
import os
import google.generativeai as genai

# --- GEMINI CONFIGURATION ---
# Replace 'YOUR_GEMINI_API_KEY' with your actual key from Google AI Studio
GEMINI_API_KEY = "AIzaSyA2X6PgXZsYnJV4czh-bQQ5QCDDPHYZMWg" 
genai.configure(api_key=GEMINI_API_KEY)

# Try to use flash, fallback to pro if needed
try:
    genai_model = genai.GenerativeModel('gemini-1.5-flash')
except:
    genai_model = genai.GenerativeModel('gemini-pro')

# A list of friendly fallback responses if the AI is truly offline
error_responses = [
    "I'm sorry, I'm still learning how to answer that! Can we talk about college admissions instead?",
    "That's a creative question! Currently, I'm optimized for college enquiries. What would you like to know about MPNMJEC?",
    "I understand your question, but my AI brain is taking a quick break. Could you ask me about our courses or facilities?",
    "Interesting! I don't have a specific answer for that yet. However, I can tell you all about our ECE or CSE departments!",
    "Great question! I'm trying to find the best way to answer. In the meantime, feel free to ask about our placement records."
]
# ----------------------------

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

stemmer = LancasterStemmer()

# Load data with absolute paths for Vercel/Render compatibility
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

words = pickle.load(open(os.path.join(BASE_DIR, 'words.pkl'), 'rb'))
classes = pickle.load(open(os.path.join(BASE_DIR, 'classes.pkl'), 'rb'))
model = load_model(os.path.join(BASE_DIR, 'chatbot_model.h5'))

with open(os.path.join(BASE_DIR, 'intents.json')) as file:
    intents = json.load(file)

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    if not ints:
        return "I'm sorry, I don't understand that. Could you please rephrase?"
    
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({"response": "Please provide a message"}), 400
    
    ints = predict_class(message, model)
    
    # --- SMART HYBRID AI APPROACH ---
    # We only use hardcoded data if we are VERY sure (Confidence > 0.7)
    # This prevents the bot from giving wrong info about departments for random questions.
    intent_context = ""
    confidence = 0
    if len(ints) > 0:
        confidence = float(ints[0]['probability'])
        if confidence > 0.7:
            intent_context = get_response(ints, intents)
    
    try:
        if intent_context:
            # We are sure about the topic, let Gemini polish the answer
            prompt = (
                f"Knowledge Base Info: {intent_context}\n"
                f"User Question: {message}\n\n"
                f"Instructions: You are the friendly AI Advisor for MPNMJEC. "
                f"Use the verified Knowledge Base Info above to answer. "
                f"Stay strictly accurate to the provided info. "
                f"Keep it under 3 sentences."
            )
        else:
            # We are NOT sure, so we let Gemini handle it generally OR ask for clarification
            prompt = (
                f"User Question: {message}\n\n"
                f"Instructions: You are a helpful and clever AI Assistant for MPNMJEC. "
                f"The user's question doesn't match our specific trained data. "
                f"If the question is about the college but you don't have the specific detail, politely ask them to clarify or contact the office. "
                f"If the question is general or casual, respond like a high-quality AI like ChatGPT. "
                f"If they are frustrated (like saying 'its bad' or 'useless'), apologize and ask how you can specifically help with college info."
            )

        response = genai_model.generate_content(prompt)
        res = response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        if intent_context:
            res = intent_context # Emergency fallback to hardcoded
        else:
            res = random.choice(error_responses)

    return jsonify({"response": res})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
