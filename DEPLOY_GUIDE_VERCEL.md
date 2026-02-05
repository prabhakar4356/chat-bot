# Deploying to Vercel (Hybrid Approach)

Since your project uses **TensorFlow** (a large AI library), it exceeds the file size limits of Vercel's free serverless functions (250MB limit).

**The Solution:** Use the **"Hybrid"** approach.
1.  **Backend (The "Brain")**: Host on **Render** (as per the previous guide).
2.  **Frontend (The "Face")**: Host on **Vercel** (for super-fast loading and easy sharing).

---

## Step 1: Deploy Backend to Render (Required)
You **must** have the backend running on Render first so the Vercel frontend has an AI to talk to.
*   Follow the **DEPLOY_GUIDE_RENDER.md** to get your backend URL.
*   Let's assume your backend URL is: `https://college-bot.onrender.com`

---

## Step 2: Configure Frontend for Vercel

1.  **Connect Frontend to Backend**:
    *   Open `frontend/script.js`.
    *   Find the line `const API_URL = ...`.
    *   Change it to your actual Render backend URL:
        ```javascript
        // const API_URL = '/chat'; // Old local version
        const API_URL = 'https://college-bot.onrender.com/chat'; // <-- REPLACE with your Render URL
        ```

2.  **Prepare for Git**:
    *   Since Vercel connects to GitHub, we need to push just the `frontend` folder or configure Vercel to look at the root.
    *   The easiest way is to deploy the whole repo but tell Vercel to only care about the frontend.

---

## Step 3: Deploy on Vercel

1.  **Go to Vercel**:
    *   Visit [vercel.com](https://vercel.com) and log in with GitHub.
    *   Click **"Add New..."** -> **"Project"**.

2.  **Import Repository**:
    *   Find your `college-chatbot` repository (the one we made for Render).
    *   Click **Import**.

3.  **Configure Project**:
    *   **Framework Preset**: Select "Other" or "Vite" (It will auto-detect usually, "Other" is fine for plain HTML).
    *   **Root Directory**: Click "Edit" and select `frontend`. **(Crucial Step!)**
        *   This tells Vercel: "This is a website file, ignore the Python backend stuff."

4.  **Deploy**:
    *   Click **Deploy**.
    *   Wait ~30 seconds.
    *   You will get a URL like `https://college-chatbot.vercel.app`.

---

## 🎉 Done!
*   **Vercel URL**: `https://college-chatbot.vercel.app` (Give this to users)
*   User opens Vercel site -> Chatbot sends message -> Vercel talks to Render Backend -> Response sent back.
