# Algorithm Visualizer

Interactive platform for understanding algorithms through visualization and AI assistance.

## 🎯 Features

- **7 Algorithm Implementations**: Bubble, Quick, Merge, Selection, Insertion Sort + Linear, Binary Search
- **Real-time Visualization**: Step-by-step animation with color-coded states
- **AI Assistant**: Powered by Google Gemini for algorithm explanations
- **Complexity Analysis**: Time/space complexity information for each algorithm
- **Execution History**: Track and review past algorithm runs

## 🏗️ Architecture

**Full-Stack Application**:
- **Frontend**: Next.js 14, React 19, TypeScript, Tailwind CSS, Shadcn/UI
- **Backend**: FastAPI (Python), SQLAlchemy, SQLite
- **AI**: Google Gemini API

## 🚀 Quick Start

### Local Development

**Backend**:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

**Frontend**:
```bash
npm install --legacy-peer-deps
npm run dev
```

Visit: http://localhost:3000

### Environment Variables

**Backend** (`backend/.env`):
```env
GEMINI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///./algorithm_visualizer.db
FRONTEND_URL=http://localhost:3000
```

**Frontend** (`.env.local`):
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## 📦 Deployment

### Backend (Render.com)

1. Create Web Service
2. Root Directory: `backend`
3. Build: `pip install -r requirements.txt`
4. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables (see above)

### Frontend (Render/Vercel)

**Render Static Site**:
- Build: `npm install --legacy-peer-deps && npm run build`
- Publish: `.next`
- Env: `NEXT_PUBLIC_API_URL=https://your-backend.onrender.com/api`

**Vercel**:
- Auto-detected Next.js
- Env: `NEXT_PUBLIC_API_URL=https://your-backend.onrender.com/api`

## 📚 API Documentation

Once deployed, visit: `https://your-backend-url.onrender.com/api/docs`

## 🛠️ Tech Stack

**Frontend**: Next.js, React, TypeScript, Tailwind CSS, Shadcn/UI, Recharts  
**Backend**: FastAPI, Pydantic, SQLAlchemy, Uvicorn  
**AI**: Google Gemini API  
**Database**: SQLite

## 📄 License

MIT
