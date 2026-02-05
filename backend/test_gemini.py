import google.generativeai as genai
import sys

# Replace with the user's key
api_key = "AIzaSyA2X6PgXZsYnJV4czh-bQQ5QCDDPHYZMWg"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    print("Testing Gemini connection...")
    response = model.generate_content("Hello, respond with one word: Success.")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
