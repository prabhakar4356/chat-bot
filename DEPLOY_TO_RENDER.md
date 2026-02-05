# 🚀 Deploying to Render

Your chatbot is now ready to deploy to **Render**, which is perfect for Python Flask applications with ML models.

## Quick Deploy Steps

### 1. **Push to GitHub** (Already Done ✅)
Your code is already on GitHub at: `https://github.com/prabhakar4356/chat-bot`

### 2. **Create Render Account**
- Go to [render.com](https://render.com)
- Sign up with your GitHub account

### 3. **Create a New Web Service**
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository: `prabhakar4356/chat-bot`
3. Configure the service:

   **Settings:**
   - **Name**: `college-chatbot` (or any name you prefer)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Runtime**: `Python 3`
   - **Build Command**: 
     ```bash
     pip install -r backend/requirements.txt
     ```
   - **Start Command**:
     ```bash
     gunicorn --chdir backend app:app
     ```

4. **Environment Variables** (Optional but recommended):
   - Click "Advanced"
   - Add: `PYTHON_VERSION` = `3.11.0`
   - Add: `GEMINI_API_KEY` = `AIzaSyA2X6PgXZsYnJV4czh-bQQ5QCDDPHYZMWg`

5. **Instance Type**:
   - Select **"Free"** tier (perfect for testing)

6. Click **"Create Web Service"**

### 4. **Wait for Deployment**
- Render will automatically build and deploy your app
- This takes about 3-5 minutes
- You'll get a URL like: `https://college-chatbot.onrender.com`

### 5. **Test Your Chatbot**
- Visit your Render URL
- The chatbot should load and work perfectly!

---

## ⚠️ Important Notes

1. **Free Tier Limitations**:
   - The free tier spins down after 15 minutes of inactivity
   - First request after inactivity may take 30-60 seconds to wake up
   - Upgrade to paid tier ($7/month) for always-on service

2. **NLTK Downloads**:
   - Your `app.py` already handles NLTK downloads automatically ✅
   - No additional configuration needed

3. **Static Files**:
   - Your Flask app serves the frontend from the `frontend` folder ✅
   - Everything is already configured correctly

---

## 🎉 That's It!

Your chatbot will be live at your Render URL. Share it with anyone!

**Need help?** Check the Render dashboard for build logs if anything goes wrong.
