# 🚀 Deploying to Vercel (via GitHub)

Since the Vercel CLI is having issues with file size, let's deploy directly from GitHub instead!

## Steps to Deploy

### 1. **Go to Vercel Dashboard**
Visit: [vercel.com/new](https://vercel.com/new)

### 2. **Import Your GitHub Repository**
1. Click **"Add New Project"**
2. Select **"Import Git Repository"**
3. Find and select: `prabhakar4356/chat-bot`
4. Click **"Import"**

### 3. **Configure Project Settings**
Vercel will auto-detect your `vercel.json`. Just verify:

- **Framework Preset**: Other
- **Root Directory**: `./` (leave as is)
- **Build Command**: Leave empty
- **Output Directory**: Leave empty

### 4. **Environment Variables** (Important!)
Click **"Environment Variables"** and add:

| Name | Value |
|------|-------|
| `GEMINI_API_KEY` | `AIzaSyA2X6PgXZsYnJV4czh-bQQ5QCDDPHYZMWg` |

### 5. **Deploy!**
Click **"Deploy"** and wait 2-3 minutes.

---

## ✅ Your App Will Be Live!

You'll get a URL like: `https://mini-project-xyz.vercel.app`

---

## 🔄 Auto-Deploy on Push

Every time you push to GitHub, Vercel will automatically redeploy! 🎉

---

## ⚠️ If Deployment Fails

Check the build logs in Vercel dashboard. Common issues:
- **Function size too large**: TensorFlow is big. If this happens, use **Render** instead (see `DEPLOY_TO_RENDER.md`)
- **NLTK errors**: Already handled in your `app.py` ✅

---

## 🎯 Recommendation

If Vercel gives you trouble with the TensorFlow model size, **Render is the better choice** for ML-based apps. See `DEPLOY_TO_RENDER.md` for instructions.
