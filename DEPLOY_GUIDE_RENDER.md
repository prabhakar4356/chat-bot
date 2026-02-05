# Deploying Your Chatbot to Render

This guide will help you deploy your **College Enquiry Chatbot** to the web using **Render.com**. Render is a cloud platform that makes it easy to host Python applications for free.

---

## 📋 Prerequisites

1.  A **GitHub Account** (https://github.com/).
2.  **Git** installed on your computer.

---

## 🚀 Step 1: Upload Your Code to GitHub

For Render to access your code, it needs to be in a GitHub repository.

1.  **Initialize Git** (if you haven't already):
    *   Open your terminal (or Command Prompt) inside your project folder: `d:\Prabhakar\MINI Project`.
    *   Run the following commands:
        ```bash
        git init
        git add .
        git commit -m "Initial commit for deployment"
        ```

2.  **Create a New Repository on GitHub**:
    *   Go to [GitHub.com](https://github.com/new).
    *   Name it `college-chatbot` (or similar).
    *   **Do not** check "Add a README" or "Add .gitignore" (you have existing files).
    *   Click **Create repository**.

3.  **Push Your Code**:
    *   Copy the commands shown on GitHub under "…or push an existing repository from the command line". They will look like this:
        ```bash
        git remote add origin https://github.com/<YOUR-USERNAME>/college-chatbot.git
        git branch -M main
        git push -u origin main
        ```
    *   Run those commands in your terminal.

---

## ☁️ Step 2: Deploy on Render

1.  **Sign Up / Log In**:
    *   Go to [dashboard.render.com](https://dashboard.render.com/).
    *   Sign in with your **GitHub** account.

2.  **Create a New Web Service**:
    *   Click the **"New +"** button and select **"Web Service"**.
    *   Select your `college-chatbot` repository from the list.

3.  **Configure the Service**:
    *   **Name**: `college-bot` (or any unique name).
    *   **Region**: Closest to you (e.g., Singapore, Oregon).
    *   **Branch**: `main`.
    *   **Root Directory**: Leave this **blank** (it defaults to `.`).
    *   **Runtime**: **Python 3**.
    *   **Build Command**:
        ```bash
        pip install -r backend/requirements.txt
        ```
    *   **Start Command**:
        ```bash
        gunicorn --chdir backend app:app
        ```
    *   **Instance Type**: Select **Free**.

4.  **Environment Variables** (Optional):
    *   If you encounter Python version issues, you can add an environment variable:
        *   Key: `PYTHON_VERSION`
        *   Value: `3.10.0`

5.  **Deploy**:
    *   Click **"Create Web Service"**.
    *   Render will start building your app. This may take 2-5 minutes.
    *   Watch the logs. Once it says "Your service is live", click the URL at the top (e.g., `https://college-bot.onrender.com`).

---

## ✅ Deployment Complete!

Your chatbot is now live on the internet! 🌍

### Important Notes:
*   **Gemini API Key**: Currently, your API key is in the code. For a public project, it is safer to use Environment Variables in Render (`GEMINI_API_KEY`) and read it in Python using `os.getenv('GEMINI_API_KEY')`.
*   **Free Tier**: The free tier on Render "spins down" after 15 minutes of inactivity. The first request after a break might take 30-50 seconds to load. This is normal for free hosting.
