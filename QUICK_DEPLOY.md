# ⚡ Quick Deploy Checklist

## 🎯 Your API Key (Already Configured)
```
GEMINI_API_KEY=AIzaSyD2VT0SFqOyotOomKKdyBky1Ovg1Ls-G6w
```

---

## 📝 Quick Steps

### 1️⃣ Push to GitHub (5 minutes)

```bash
cd /Users/apple/Downloads/algorithm-visualizer

# Initialize and commit
git init
git add .
git commit -m "Full-stack Algorithm Visualizer ready for deployment"

# Create repo on GitHub: https://github.com/new
# Name: algorithm-visualizer
# Public repository

# Push (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/algorithm-visualizer.git
git branch -M main
git push -u origin main
```

---

### 2️⃣ Deploy Backend to Render (10 minutes)

1. **Go to**: https://dashboard.render.com
2. **Click**: "New +" → "Web Service"
3. **Connect**: Your GitHub repository
4. **Configure**:
   ```
   Name: algorithm-visualizer-backend
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   Plan: Free
   ```

5. **Environment Variables** (Click "Advanced"):
   ```
   GEMINI_API_KEY = AIzaSyD2VT0SFqOyotOomKKdyBky1Ovg1Ls-G6w
   DATABASE_URL = sqlite:///./algorithm_visualizer.db
   HOST = 0.0.0.0
   PYTHON_VERSION = 3.11.0
   FRONTEND_URL = *
   ```

6. **Click**: "Create Web Service"
7. **Wait**: 5-10 minutes for deployment
8. **Copy**: Your backend URL (e.g., `https://algorithm-visualizer-backend.onrender.com`)

---

### 3️⃣ Deploy Frontend to Render (10 minutes)

1. **Go to**: https://dashboard.render.com
2. **Click**: "New +" → "Static Site"
3. **Connect**: Same GitHub repository
4. **Configure**:
   ```
   Name: algorithm-visualizer
   Branch: main
   Build Command: npm install --legacy-peer-deps && npm run build
   Publish Directory: .next
   ```

5. **Environment Variables** (Click "Advanced"):
   ```
   NEXT_PUBLIC_API_URL = https://YOUR-BACKEND-URL.onrender.com/api
   NODE_VERSION = 18
   ```
   ⚠️ Replace `YOUR-BACKEND-URL` with the URL from step 2

6. **Click**: "Create Static Site"
7. **Wait**: 5-10 minutes for build
8. **Copy**: Your frontend URL

---

### 4️⃣ Update Backend CORS (2 minutes)

1. **Go to**: Backend service on Render
2. **Click**: "Environment" tab
3. **Update**: `FRONTEND_URL` variable
   ```
   Old: *
   New: https://YOUR-FRONTEND-URL.onrender.com
   ```
4. **Save**: Service will auto-redeploy

---

## ✅ Test Your Deployment

Visit: `https://YOUR-FRONTEND-URL.onrender.com`

**Test**:
- [ ] Page loads
- [ ] Select Bubble Sort
- [ ] Click Start
- [ ] Visualization works
- [ ] AI Assistant responds

---

## 🎉 Done!

Your app is now live at:
- **Frontend**: `https://YOUR-FRONTEND-URL.onrender.com`
- **Backend API**: `https://YOUR-BACKEND-URL.onrender.com/api/docs`

---

## 🆘 Issues?

**Frontend can't connect to backend**:
- Check `NEXT_PUBLIC_API_URL` includes `/api` at the end
- Verify backend is running (visit `/api/health`)

**AI Assistant not working**:
- Verify `GEMINI_API_KEY` is set in backend environment

**Build fails**:
- Check logs in Render dashboard
- Ensure all environment variables are set

---

## 📚 Full Guide

For detailed instructions, see: `RENDER_DEPLOYMENT_GUIDE.md`

---

**Total Time**: ~25 minutes  
**Cost**: $0 (Free tier)  
**Result**: Publicly accessible full-stack app! 🚀
