#!/bin/bash

echo "🚀 Starting Algorithm Visualizer Backend..."
echo ""

# Navigate to backend directory
cd backend

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run: python -m venv venv"
    exit 1
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import fastapi" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create backend/.env with your GEMINI_API_KEY"
    echo "See backend/.env.example for reference"
fi

# Start the server
echo ""
echo "🎯 Starting FastAPI server on http://localhost:8000"
echo "📚 API Docs available at http://localhost:8000/api/docs"
echo ""
python main.py
