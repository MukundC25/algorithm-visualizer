# Deploy to Render

## Backend (10 min)

1. Go to https://dashboard.render.com
2. New + → Web Service
3. Connect: https://github.com/MukundC25/algorithm-visualizer
4. Settings:
   - Name: `algorithm-visualizer-backend`
   - Root: `backend`
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Environment Variables:
   ```
   GEMINI_API_KEY=AIzaSyD2VT0SFqOyotOomKKdyBky1Ovg1Ls-G6w
   DATABASE_URL=sqlite:///./algorithm_visualizer.db
   PYTHON_VERSION=3.11.0
   FRONTEND_URL=*
   ```
6. Create Web Service
7. Copy backend URL

## Frontend (10 min)

1. New + → Static Site
2. Connect same repo
3. Settings:
   - Name: `algorithm-visualizer`
   - Build: `npm install --legacy-peer-deps && npm run build`
   - Publish: `.next`
4. Environment:
   ```
   NEXT_PUBLIC_API_URL=https://YOUR-BACKEND-URL.onrender.com/api
   NODE_VERSION=18
   ```
5. Create Static Site
6. Copy frontend URL

## Update CORS

1. Go to backend service
2. Environment → Update `FRONTEND_URL` to your frontend URL
3. Save (auto-redeploys)

Done! 🚀
