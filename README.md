# Algorithm Visualizer

Full-stack interactive platform for understanding algorithms through visualization and AI assistance.

## Features

- 🎯 **7 Algorithm Implementations**: Bubble, Quick, Merge, Selection, Insertion Sort + Linear, Binary Search
- 🎨 **Real-time Visualization**: Step-by-step animation with color-coded states
- 🤖 **AI Assistant**: Powered by Google Gemini for algorithm explanations
- 📊 **Complexity Analysis**: Time/space complexity with operation counting
- 📝 **Execution History**: Track and review past algorithm runs
- 🎮 **Interactive Controls**: Custom input, speed control, step navigation

## Tech Stack

**Frontend**: Next.js 14, React 19, TypeScript, Tailwind CSS, Shadcn/UI  
**Backend**: FastAPI, Python 3.11, SQLAlchemy, Pydantic  
**AI**: Google Gemini API  
**Database**: SQLite

## Quick Start

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

### Frontend
```bash
npm install --legacy-peer-deps
npm run dev
```

Visit: http://localhost:3000

## Deployment

**Backend**: Deploy to Render.com (see `backend/render.yaml`)  
**Frontend**: Deploy to Vercel or Render Static Site

Environment variables required:
- `GEMINI_API_KEY` (backend)
- `NEXT_PUBLIC_API_URL` (frontend)

## API Documentation

Interactive docs: http://localhost:8000/api/docs

## License

MIT
