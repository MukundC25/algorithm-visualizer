# 🚀 Render.com Deployment Guide

## Complete Step-by-Step Guide for Deploying Algorithm Visualizer

This guide will help you deploy both the **Backend (FastAPI)** and **Frontend (Next.js)** to Render.com.

---

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] GitHub account
- [ ] Render.com account (sign up at https://render.com)
- [ ] Your code pushed to a GitHub repository
- [ ] Gemini API key (already configured: `AIzaSyD2VT0SFqOyotOomKKdyBky1Ovg1Ls-G6w`)

---

## 🎯 Deployment Strategy

We'll deploy in this order:

1. **Backend First** → Get the API URL
2. **Frontend Second** → Configure it to use the backend URL

---

## Part 1: Push Code to GitHub

### Step 1: Initialize Git Repository

```bash
cd /Users/apple/Downloads/algorithm-visualizer

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Full-stack Algorithm Visualizer"
```

### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `algorithm-visualizer`
3. Description: "Interactive Algorithm Visualizer with AI Assistant"
4. **Important**: Keep it **Public** (Render free tier requires public repos)
5. **Do NOT** initialize with README (we already have files)
6. Click "Create repository"

### Step 3: Push to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/algorithm-visualizer.git

# Push code
git branch -M main
git push -u origin main
```

---

## Part 2: Deploy Backend to Render

### Step 1: Create New Web Service

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect a repository"**
4. Authorize Render to access your GitHub
5. Select your `algorithm-visualizer` repository

### Step 2: Configure Backend Service

Fill in the following settings:

**Basic Settings:**
- **Name**: `algorithm-visualizer-backend`
- **Region**: `Oregon (US West)` (or closest to you)
- **Branch**: `main`
- **Root Directory**: `backend`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Advanced Settings:**

Click **"Advanced"** and add these **Environment Variables**:

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | `AIzaSyD2VT0SFqOyotOomKKdyBky1Ovg1Ls-G6w` |
| `DATABASE_URL` | `sqlite:///./algorithm_visualizer.db` |
| `HOST` | `0.0.0.0` |
| `PYTHON_VERSION` | `3.11.0` |
| `FRONTEND_URL` | `*` (we'll update this later) |

**Plan:**
- Select **"Free"** plan

### Step 3: Deploy Backend

1. Click **"Create Web Service"**
2. Wait for deployment (5-10 minutes)
3. Watch the logs for any errors
4. Once deployed, you'll see: **"Your service is live 🎉"**

### Step 4: Get Backend URL

After deployment:
1. Copy your backend URL (e.g., `https://algorithm-visualizer-backend.onrender.com`)
2. **Save this URL** - you'll need it for frontend configuration

### Step 5: Test Backend

Visit these URLs to verify:

```
https://YOUR-BACKEND-URL.onrender.com/api/health
https://YOUR-BACKEND-URL.onrender.com/api/docs
```

You should see:
- `/api/health` → `{"status": "healthy"}`
- `/api/docs` → Interactive API documentation

---

## Part 3: Deploy Frontend to Render

### Option A: Deploy as Static Site (Recommended)

#### Step 1: Update Frontend Environment

First, update your local `.env.local`:

```bash
# Edit .env.local
nano .env.local
```

Change to your backend URL:
```env
NEXT_PUBLIC_API_URL=https://YOUR-BACKEND-URL.onrender.com/api
```

Commit and push:
```bash
git add .env.local
git commit -m "Update API URL for production"
git push
```

#### Step 2: Create Static Site on Render

1. Go to https://dashboard.render.com
2. Click **"New +"** → **"Static Site"**
3. Select your `algorithm-visualizer` repository

#### Step 3: Configure Frontend

**Basic Settings:**
- **Name**: `algorithm-visualizer`
- **Branch**: `main`
- **Root Directory**: (leave empty - root of repo)
- **Build Command**: `npm install --legacy-peer-deps && npm run build`
- **Publish Directory**: `.next`

**Environment Variables:**

Click **"Advanced"** and add:

| Key | Value |
|-----|-------|
| `NEXT_PUBLIC_API_URL` | `https://YOUR-BACKEND-URL.onrender.com/api` |
| `NODE_VERSION` | `18` |

#### Step 4: Deploy Frontend

1. Click **"Create Static Site"**
2. Wait for build (5-10 minutes)
3. Once deployed, you'll get a URL like: `https://algorithm-visualizer.onrender.com`

---

### Option B: Deploy as Web Service (Alternative)

If Static Site doesn't work, use Web Service:

1. **New +** → **Web Service**
2. Select repository
3. Configure:
   - **Name**: `algorithm-visualizer-frontend`
   - **Runtime**: `Node`
   - **Build Command**: `npm install --legacy-peer-deps && npm run build`
   - **Start Command**: `npm start`
   - **Environment Variables**: Same as above

---

## Part 4: Update CORS Settings

After frontend is deployed:

### Step 1: Update Backend Environment

1. Go to your backend service on Render
2. Go to **"Environment"** tab
3. Update `FRONTEND_URL` variable:
   - **Old**: `*`
   - **New**: `https://YOUR-FRONTEND-URL.onrender.com`
4. Click **"Save Changes"**
5. Service will auto-redeploy

---

## Part 5: Final Testing

### Test Your Deployed Application

1. **Visit Frontend**: `https://YOUR-FRONTEND-URL.onrender.com`

2. **Test Algorithm Execution**:
   - Select "Bubble Sort"
   - Click "Start"
   - Verify visualization works

3. **Test AI Assistant**:
   - Click AI Assistant button
   - Ask: "What is the time complexity of Bubble Sort?"
   - Verify response appears

4. **Check Backend Logs**:
   - Go to Render dashboard
   - Click on backend service
   - View "Logs" tab
   - Look for any errors

---

## 🔧 Troubleshooting

### Issue 1: Frontend Can't Connect to Backend

**Symptoms**: API calls fail, "Failed to fetch" errors

**Solutions**:
1. Check `NEXT_PUBLIC_API_URL` in frontend environment variables
2. Verify backend is running (visit `/api/health`)
3. Check CORS settings in backend
4. Ensure backend URL includes `/api` at the end

### Issue 2: AI Assistant Not Working

**Symptoms**: AI queries fail

**Solutions**:
1. Verify `GEMINI_API_KEY` is set in backend environment
2. Check backend logs for Gemini API errors
3. Verify API key is valid at https://makersuite.google.com/

### Issue 3: Build Fails

**Frontend Build Errors**:
```bash
# If dependency errors, use:
npm install --legacy-peer-deps
```

**Backend Build Errors**:
```bash
# Check Python version is 3.11
# Verify all dependencies in requirements.txt
```

### Issue 4: Database Errors

**SQLite Issues**:
- Render's free tier has ephemeral storage
- Database resets on each deployment
- For persistent data, upgrade to paid plan or use PostgreSQL

**Solution for Persistent Database**:
1. Create PostgreSQL database on Render
2. Update `DATABASE_URL` to PostgreSQL connection string
3. Update SQLAlchemy connection in `backend/database/connection.py`

---

## 📊 Deployment Checklist

### Backend Deployment
- [ ] Code pushed to GitHub
- [ ] Backend service created on Render
- [ ] Environment variables configured
- [ ] `GEMINI_API_KEY` added
- [ ] Service deployed successfully
- [ ] `/api/health` endpoint working
- [ ] `/api/docs` accessible
- [ ] Backend URL copied

### Frontend Deployment
- [ ] `.env.local` updated with backend URL
- [ ] Changes committed and pushed
- [ ] Frontend service/static site created
- [ ] `NEXT_PUBLIC_API_URL` configured
- [ ] Build completed successfully
- [ ] Frontend URL accessible
- [ ] Can load homepage

### Integration Testing
- [ ] Algorithm visualization works
- [ ] API calls successful
- [ ] Statistics update correctly
- [ ] AI Assistant responds
- [ ] No CORS errors
- [ ] No console errors

### Final Configuration
- [ ] Backend `FRONTEND_URL` updated
- [ ] Both services redeployed
- [ ] All features tested
- [ ] Performance acceptable

---

## 🎯 Expected URLs

After deployment, you'll have:

**Backend API**:
```
https://algorithm-visualizer-backend.onrender.com
https://algorithm-visualizer-backend.onrender.com/api/docs
https://algorithm-visualizer-backend.onrender.com/api/health
```

**Frontend**:
```
https://algorithm-visualizer.onrender.com
```

---

## 💡 Pro Tips

### 1. Free Tier Limitations

**Render Free Tier**:
- Services spin down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- 750 hours/month free (enough for 1 service 24/7)

**Solutions**:
- Use a service like UptimeRobot to ping your app every 14 minutes
- Upgrade to paid plan for always-on services

### 2. Environment Variables

**Never commit**:
- `.env` files
- API keys
- Secrets

**Always use**:
- Render's environment variables
- `.env.example` for documentation

### 3. Monitoring

**Set up monitoring**:
1. Go to service → "Settings" → "Health Check Path"
2. Set to `/api/health`
3. Render will auto-restart if health check fails

### 4. Custom Domain (Optional)

**Add custom domain**:
1. Go to service → "Settings" → "Custom Domain"
2. Add your domain
3. Update DNS records as instructed
4. Update `FRONTEND_URL` in backend

---

## 🚀 Alternative: Vercel for Frontend

If you prefer Vercel for frontend:

### Deploy Frontend to Vercel

1. Go to https://vercel.com
2. Import your GitHub repository
3. Configure:
   - **Framework**: Next.js
   - **Root Directory**: `/`
   - **Environment Variable**: `NEXT_PUBLIC_API_URL` = `https://YOUR-BACKEND-URL.onrender.com/api`
4. Deploy

**Advantages**:
- Faster builds
- Better Next.js optimization
- Free tier more generous
- No spin-down

---

## 📞 Support Resources

**Render Documentation**:
- https://render.com/docs
- https://render.com/docs/deploy-fastapi

**Troubleshooting**:
- Check service logs in Render dashboard
- View build logs for errors
- Monitor resource usage

**Community**:
- Render Community Forum
- Stack Overflow
- GitHub Issues

---

## ✅ Success Criteria

Your deployment is successful when:

✅ Backend API responds at `/api/health`  
✅ Frontend loads without errors  
✅ Algorithm visualization works  
✅ AI Assistant responds to queries  
✅ No CORS errors in console  
✅ Statistics update correctly  
✅ All 7 algorithms functional  

---

## 🎉 Congratulations!

Your Algorithm Visualizer is now deployed and publicly accessible!

**Share your app**:
- Frontend: `https://YOUR-FRONTEND-URL.onrender.com`
- API Docs: `https://YOUR-BACKEND-URL.onrender.com/api/docs`

**Next Steps**:
- Add custom domain
- Set up monitoring
- Implement analytics
- Add more algorithms
- Share with the world! 🌍

---

**Last Updated**: November 27, 2025  
**Deployment Platform**: Render.com  
**Status**: Ready for Deployment
