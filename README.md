# College Enquiry Chatbot 🎓🤖

A smart, NLP-powered chatbot designed to handle college-related enquiries. The system uses a Flask backend with a Deep Learning model (TensorFlow/Keras) and a modern, responsive frontend.

---

## 🚀 How to Run the Project

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Setup the Backend
The backend handles the Natural Language Processing and serves responses via an API.

1.  **Open a terminal/command prompt.**
2.  **Navigate to the backend folder:**
    ```bash
    cd "d:/Prabhakar/MINI Project/backend"
    ```
3.  **Install Dependencies:**
    It is recommended to use a virtual environment, but you can install directly using:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Start the Server:**
    ```bash
    python app.py
    ```
    *The backend will run on `http://127.0.0.1:5000`.*

### 3. Setup the Frontend
The frontend is a clean web interface for interacting with the bot.

1.  **Locate the file:** `d:/Prabhakar/MINI Project/frontend/index.html`
2.  **Open it:** Simply double-click `index.html` to open it in your web browser (Chrome, Edge, or Firefox).
3.  **Start Chatting!**

---

## 🧠 Training the Model
If you modify the knowledge base (`backend/intents.json`), you must retrain the AI model for the changes to take effect.

1.  Open a terminal in the `backend` folder.
2.  Run the training script:
    ```bash
    python train_model.py
    ```
3.  The script will generate new `chatbot_model.h5`, `words.pkl`, and `classes.pkl` files.
4.  Restart the `app.py` server to load the new model.

---

## 🛠️ Technology Stack
- **Frontend:** HTML5, Vanilla CSS, JavaScript (Fetch API)
- **Backend:** Python, Flask, Flask-CORS
- **AI/ML:** TensorFlow, Keras, NLTK (Natural Language Toolkit), NumPy

---

## 📧 Support
If you encounter any issues with the connection, ensure that the backend server (`app.py`) is running and that your browser allows local requests.
