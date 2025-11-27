# Algorithm Visualizer - Full-Stack Setup Guide

## 🎯 Project Overview

This project has been transformed from a frontend-only application into a complete full-stack system matching your SRS architecture:

### **Architecture**
```
Frontend (Next.js 14) → API Layer → FastAPI Backend → Algorithm Engine → Database
                                  ↓
                            Gemini AI Assistant
```

### **Tech Stack**

**Frontend:**
- Next.js 14 (App Router)
- React 19
- TypeScript
- Tailwind CSS
- Shadcn/UI + Radix UI
- Recharts

**Backend:**
- FastAPI (Python)
- SQLAlchemy (ORM)
- SQLite (Database)
- Google Gemini AI
- Pydantic (Validation)

---

## 📁 Project Structure

```
algorithm-visualizer/
├── app/                          # Next.js frontend
│   ├── page.tsx                  # Main visualizer (refactored to use API)
│   ├── layout.tsx
│   └── globals.css
├── components/                   # React components (Shadcn/UI)
├── lib/
│   ├── api.ts                    # ✨ NEW: API client for backend
│   └── utils.ts
├── backend/                      # ✨ NEW: FastAPI backend
│   ├── main.py                   # FastAPI app entry point
│   ├── requirements.txt          # Python dependencies
│   ├── .env                      # Backend environment variables
│   ├── routers/                  # API endpoints
│   │   ├── algorithms.py         # Algorithm execution
│   │   ├── complexity.py         # Complexity analysis
│   │   ├── ai.py                 # Gemini AI proxy
│   │   └── history.py            # Execution history
│   ├── core/
│   │   ├── algorithm_engine/     # Algorithm implementations
│   │   │   ├── sorting/          # Bubble, Quick, Merge, etc.
│   │   │   └── searching/        # Linear, Binary
│   │   ├── analyzer/             # Complexity analyzer
│   │   └── utils/
│   ├── models/                   # Pydantic schemas
│   │   ├── request_models.py
│   │   └── response_models.py
│   └── database/                 # SQLAlchemy models
│       ├── models.py
│       └── connection.py
├── .env.local                    # Frontend environment variables
└── package.json
```

---

## 🚀 Setup Instructions

### **Prerequisites**
- Node.js 18+ and pnpm (or npm/yarn)
- Python 3.9+
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

---

### **Step 1: Backend Setup**

#### 1.1 Navigate to backend directory
```bash
cd backend
```

#### 1.2 Create Python virtual environment
```bash
python -m venv venv

# Activate it:
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

#### 1.3 Install Python dependencies
```bash
pip install -r requirements.txt
```

#### 1.4 Configure environment variables
Edit `backend/.env` and add your Gemini API key:

```env
# Get your API key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_actual_gemini_api_key_here

DATABASE_URL=sqlite:///./algorithm_visualizer.db
FRONTEND_URL=http://localhost:3000
HOST=0.0.0.0
PORT=8000
```

#### 1.5 Start the backend server
```bash
python main.py
```

The backend will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

---

### **Step 2: Frontend Setup**

#### 2.1 Navigate to project root
```bash
cd ..  # Go back to project root
```

#### 2.2 Install frontend dependencies
```bash
pnpm install
# or: npm install
# or: yarn install
```

#### 2.3 Configure frontend environment
Edit `.env.local` to ensure it points to your backend:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

#### 2.4 Start the frontend development server
```bash
pnpm dev
# or: npm run dev
# or: yarn dev
```

The frontend will be available at: **http://localhost:3000**

---

## 🧪 Testing the Integration

### **1. Test Backend API**

Visit http://localhost:8000/api/docs to see interactive API documentation.

**Test Algorithm Execution:**
```bash
curl -X POST "http://localhost:8000/api/execute-algorithm" \
  -H "Content-Type: application/json" \
  -d '{
    "algorithm_type": "bubble",
    "array": [64, 34, 25, 12, 22, 11, 90]
  }'
```

**Test AI Assistant:**
```bash
curl -X POST "http://localhost:8000/api/ai/query" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "What is the time complexity of Bubble Sort?",
    "context": "bubble"
  }'
```

### **2. Test Frontend**

1. Open http://localhost:3000
2. Select an algorithm (e.g., Bubble Sort)
3. Click "Start" to visualize
4. Open AI Assistant and ask a question
5. Check browser console for any errors

---

## 🔧 API Endpoints

### **Algorithm Execution**
`POST /api/execute-algorithm`
```json
{
  "algorithm_type": "bubble",
  "array": [64, 34, 25, 12, 22],
  "search_target": null
}
```

### **Complexity Analysis**
`POST /api/analyze-complexity`
```json
{
  "algorithm_type": "quick",
  "array_size": 100
}
```

### **AI Query**
`POST /api/ai/query`
```json
{
  "user_query": "Explain merge sort",
  "context": "merge"
}
```

### **Execution History**
`GET /api/history?limit=50`

### **Health Check**
`GET /api/health`

---

## 📊 Supported Algorithms

### **Sorting Algorithms**
- Bubble Sort - O(n²)
- Quick Sort - O(n log n)
- Merge Sort - O(n log n)
- Selection Sort - O(n²)
- Insertion Sort - O(n²)

### **Searching Algorithms**
- Linear Search - O(n)
- Binary Search - O(log n)

---

## 🗄️ Database Schema

### **AlgorithmExecution**
Stores algorithm execution history
- `id`, `algorithm_type`, `algorithm_name`, `array_size`
- `comparisons`, `swaps`, `category`, `timestamp`

### **AIQuery**
Stores AI assistant interactions
- `id`, `user_query`, `ai_response`, `context`, `timestamp`

### **ComplexityAnalysis**
Stores complexity analysis results
- `id`, `algorithm_type`, `array_size`, `estimated_operations`, `timestamp`

---

## 🐛 Troubleshooting

### **Backend won't start**
- Check if Python virtual environment is activated
- Verify all dependencies are installed: `pip list`
- Check if port 8000 is available: `lsof -i :8000`

### **Frontend can't connect to backend**
- Ensure backend is running on http://localhost:8000
- Check `.env.local` has correct `NEXT_PUBLIC_API_URL`
- Check browser console for CORS errors

### **AI Assistant not working**
- Verify `GEMINI_API_KEY` is set in `backend/.env`
- Check API key is valid at https://makersuite.google.com/
- Check backend logs for error messages

### **Database errors**
Delete the database and restart:
```bash
cd backend
rm algorithm_visualizer.db
python main.py
```

---

## 🎨 Key Changes from Original

### **What Changed:**

1. **Algorithm Logic Moved to Backend**
   - All sorting/searching algorithms now run on FastAPI backend
   - Frontend receives step-by-step visualization data via API

2. **AI Integration Refactored**
   - Removed direct AI SDK usage from frontend
   - Created Gemini AI proxy endpoint in backend
   - Frontend calls `/api/ai/query` instead

3. **New API Layer**
   - Created `lib/api.ts` with functions: `runAlgorithm()`, `askAI()`, `getComplexity()`, `getHistory()`
   - All frontend components now use these API functions

4. **Database Integration**
   - SQLite database stores execution history
   - Track algorithm runs, AI queries, complexity analyses

### **What Stayed the Same:**

✅ All UI components (Shadcn/UI)
✅ Tailwind styling
✅ Existing layout and design
✅ Visualization animations
✅ Chat UI interface

---

## 📝 Development Workflow

### **Running Both Servers**

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python main.py
```

**Terminal 2 - Frontend:**
```bash
pnpm dev
```

### **Making Changes**

**Backend Changes:**
- Edit files in `backend/`
- FastAPI auto-reloads on file changes
- Check logs in terminal

**Frontend Changes:**
- Edit files in `app/`, `components/`, `lib/`
- Next.js auto-reloads
- Check browser console

---

## 🚢 Deployment

### **Backend Deployment**
- Deploy to: Railway, Render, Fly.io, or AWS
- Set environment variables in platform
- Update `FRONTEND_URL` to production URL

### **Frontend Deployment**
- Deploy to: Vercel, Netlify, or Cloudflare Pages
- Set `NEXT_PUBLIC_API_URL` to production backend URL
- Build command: `pnpm build`

---

## 📚 Additional Resources

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Next.js Docs**: https://nextjs.org/docs
- **Gemini API**: https://ai.google.dev/docs
- **SQLAlchemy**: https://docs.sqlalchemy.org/

---

## ✅ Checklist

- [ ] Backend running on http://localhost:8000
- [ ] Frontend running on http://localhost:3000
- [ ] Gemini API key configured
- [ ] Can execute algorithms and see visualization
- [ ] AI Assistant responds to questions
- [ ] No errors in browser console
- [ ] No errors in backend terminal

---

## 🎉 Success!

Your Algorithm Visualizer is now a complete full-stack application matching the SRS architecture!

**Next Steps:**
1. Test all algorithms
2. Try the AI assistant
3. Check execution history
4. Customize and extend as needed

For issues or questions, check the troubleshooting section above.
