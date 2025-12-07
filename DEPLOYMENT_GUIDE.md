# 🚀 Deployment Guide

## The 404 Error You're Seeing

The error `404: NOT_FOUND` with ID `dxb1::6r5p5-1765136194150-497f90f5e2a3` indicates a Vercel deployment issue.

---

## 📋 Quick Fix Options

### Option 1: Deploy Frontend Only (Easiest)

Since your backend needs the model file and runs locally, deploy only the frontend:

#### Step 1: Update API URL

Edit `frontend/src/Api.jsx`:
```javascript
const API = axios.create({
  baseURL: "http://localhost:8000", // Keep this for local backend
  // Or use your deployed backend URL if you deploy it separately
});
```

#### Step 2: Deploy to Vercel

```bash
cd frontend
npm run build
npx vercel --prod
```

Or use Vercel Dashboard:
1. Go to https://vercel.com
2. Import your GitHub repo
3. Set root directory to `frontend`
4. Deploy

---

### Option 2: Deploy Both Frontend and Backend

#### Frontend (Vercel/Netlify)

**Vercel:**
```bash
cd frontend
npm run build
npx vercel --prod
```

**Netlify:**
```bash
cd frontend
npm run build
npx netlify deploy --prod --dir=dist
```

#### Backend (Railway/Render/Heroku)

**Railway:**
1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Select your repo
4. Set root directory to `backend`
5. Add environment variables if needed
6. Deploy

**Render:**
1. Go to https://render.com
2. New Web Service
3. Connect your repo
4. Root directory: `backend`
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Deploy

---

### Option 3: Deploy as Monorepo (Advanced)

Use the `vercel.json` files I created:

1. **Root `vercel.json`**: Handles both frontend and backend
2. **Frontend `vercel.json`**: Frontend-specific config
3. **Backend `vercel.json`**: Backend-specific config

Deploy:
```bash
npx vercel --prod
```

---

## ⚠️ Important Notes

### Model File Issue

Your `hear_disease_model.pkl` file:
- **Size**: Likely too large for Vercel (50MB limit)
- **Solution**: Use a cloud storage service

**Options:**
1. **AWS S3**: Store model, download on startup
2. **Google Cloud Storage**: Store model, download on startup
3. **Hugging Face**: Host model, load remotely
4. **Railway/Render**: No file size limits

### Environment Variables

If deploying backend, set these:
- `PORT`: Auto-set by platform
- `CORS_ORIGINS`: Your frontend URL
- `MODEL_PATH`: Path to model file

---

## 🎯 Recommended Approach

### For Development/Demo:

**Keep Backend Local:**
1. Run backend locally: `python backend/main.py`
2. Deploy only frontend to Vercel
3. Use ngrok to expose local backend:
   ```bash
   ngrok http 8000
   ```
4. Update frontend API URL to ngrok URL

### For Production:

**Separate Deployments:**
1. **Frontend**: Vercel/Netlify
2. **Backend**: Railway/Render (supports larger files)
3. **Model**: Cloud storage (S3/GCS)

---

## 🔧 Fix Current Deployment

### If Using Vercel:

1. **Check Build Settings:**
   - Framework Preset: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

2. **Check Environment Variables:**
   - Add any required env vars in Vercel dashboard

3. **Redeploy:**
   ```bash
   cd frontend
   npm run build
   npx vercel --prod
   ```

### If Using Netlify:

1. **Create `netlify.toml`:**
   ```toml
   [build]
     base = "frontend"
     command = "npm run build"
     publish = "dist"

   [[redirects]]
     from = "/*"
     to = "/index.html"
     status = 200
   ```

2. **Deploy:**
   ```bash
   cd frontend
   npm run build
   npx netlify deploy --prod --dir=dist
   ```

---

## 📝 Quick Commands

### Build Frontend:
```bash
cd frontend
npm install
npm run build
```

### Test Build Locally:
```bash
cd frontend
npm run preview
```

### Deploy Frontend (Vercel):
```bash
cd frontend
npx vercel --prod
```

### Deploy Backend (Railway):
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

---

## 🐛 Troubleshooting

### 404 Error:
- Check if `dist` folder exists after build
- Verify `index.html` is in `dist` folder
- Check Vercel/Netlify build logs

### Build Fails:
- Run `npm run build` locally first
- Check for TypeScript/ESLint errors
- Verify all dependencies are in `package.json`

### Backend Connection Error:
- Update CORS settings in `backend/main.py`
- Add frontend URL to `allow_origins`
- Check backend is running and accessible

---

## 💡 Best Practice

For a medical app like this:

1. **Frontend**: Deploy to Vercel/Netlify (free tier)
2. **Backend**: Deploy to Railway/Render (free tier with limits)
3. **Model**: Store in cloud, load on startup
4. **Database**: Add if needed (PostgreSQL on Railway)

This gives you a production-ready, scalable deployment! 🎉
