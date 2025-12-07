# 🚀 Simple Deployment Steps

## What You Have Now

✅ A working heart disease prediction app  
✅ Frontend (React + Vite)  
✅ Backend (FastAPI + Python)  
✅ Model file (hear_disease_model.pkl)  

---

## 🎯 Easiest Way to Deploy

### Step 1: Test Locally First

Make sure everything works:

```cmd
# Terminal 1 - Backend
cd backend
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Open http://localhost:5173 - Does it work? ✅

---

### Step 2: Deploy Frontend to Vercel

#### A. Install Vercel CLI (one-time)

```cmd
npm install -g vercel
```

#### B. Build Frontend

```cmd
cd frontend
npm run build
```

You should see a `dist` folder created.

#### C. Deploy

```cmd
npx vercel --prod
```

Follow the prompts:
- Set up and deploy? **Y**
- Which scope? Choose your account
- Link to existing project? **N**
- Project name? **heart-disease-app** (or any name)
- Directory? **./frontend** (or just press Enter)
- Override settings? **N**

You'll get a URL like: `https://heart-disease-app.vercel.app`

---

### Step 3: Keep Backend Running Locally

Your backend has a large model file, so keep it local for now.

#### Option A: Use ngrok (Expose Local Backend)

1. **Download ngrok**: https://ngrok.com/download
2. **Run backend**:
   ```cmd
   cd backend
   python main.py
   ```
3. **In another terminal, run ngrok**:
   ```cmd
   ngrok http 8000
   ```
4. **Copy the ngrok URL** (looks like: `https://abc123.ngrok.io`)

5. **Update Frontend API URL**:
   
   Edit `frontend/src/Api.jsx`:
   ```javascript
   const API = axios.create({
     baseURL: "https://abc123.ngrok.io", // Your ngrok URL
   });
   ```

6. **Rebuild and redeploy frontend**:
   ```cmd
   cd frontend
   npm run build
   npx vercel --prod
   ```

---

## 🎉 You're Done!

Your app is now live:
- **Frontend**: https://your-app.vercel.app
- **Backend**: Running locally (exposed via ngrok)

---

## 🔄 Alternative: Deploy Backend to Railway

If you want backend online too:

### Step 1: Sign up for Railway

Go to https://railway.app and sign up (free tier available)

### Step 2: Create New Project

1. Click "New Project"
2. Choose "Deploy from GitHub repo"
3. Connect your GitHub account
4. Select your repository

### Step 3: Configure Backend

1. Set **Root Directory**: `backend`
2. Railway will auto-detect Python
3. It will use `requirements.txt` automatically
4. Click "Deploy"

### Step 4: Get Backend URL

After deployment, Railway gives you a URL like:
`https://your-app.railway.app`

### Step 5: Update Frontend

Edit `frontend/src/Api.jsx`:
```javascript
const API = axios.create({
  baseURL: "https://your-app.railway.app",
});
```

Rebuild and redeploy frontend:
```cmd
cd frontend
npm run build
npx vercel --prod
```

---

## 📱 What You'll Have

### With ngrok (Free, Temporary):
- ✅ Frontend online 24/7
- ⚠️ Backend only when your computer is on
- ⚠️ ngrok URL changes when you restart

### With Railway (Free Tier):
- ✅ Frontend online 24/7
- ✅ Backend online 24/7
- ✅ Permanent URLs
- ⚠️ Free tier has limits (500 hours/month)

---

## 🐛 Troubleshooting

### "404 NOT_FOUND" Error

This means Vercel can't find your files.

**Fix:**
1. Make sure you're in the `frontend` folder
2. Run `npm run build` first
3. Check if `dist` folder exists
4. Then run `npx vercel --prod`

### "Build Failed" Error

**Fix:**
```cmd
cd frontend
npm install
npm run build
```

If errors appear, fix them first, then deploy.

### "Cannot connect to backend"

**Fix:**
1. Make sure backend is running: `python backend/main.py`
2. Check if ngrok is running: `ngrok http 8000`
3. Update API URL in `frontend/src/Api.jsx`
4. Rebuild frontend: `npm run build`
5. Redeploy: `npx vercel --prod`

---

## 💡 Quick Commands Reference

### Build Frontend:
```cmd
cd frontend
npm run build
```

### Deploy Frontend:
```cmd
cd frontend
npx vercel --prod
```

### Run Backend:
```cmd
cd backend
python main.py
```

### Expose Backend (ngrok):
```cmd
ngrok http 8000
```

---

## ✅ Checklist

Before deploying:
- [ ] App works locally (both frontend and backend)
- [ ] Frontend builds successfully (`npm run build`)
- [ ] `dist` folder exists in frontend
- [ ] Backend is running
- [ ] Model file is in backend folder

After deploying:
- [ ] Frontend URL works
- [ ] Can see the form
- [ ] Backend is accessible (local or Railway)
- [ ] Predictions work

---

## 🎯 Recommended Setup

**For Demo/Testing:**
- Frontend: Vercel (free)
- Backend: Local + ngrok (free)

**For Production:**
- Frontend: Vercel (free)
- Backend: Railway (free tier)
- Model: Keep in backend folder

---

Need help? Check `DEPLOYMENT_GUIDE.md` for more details!
