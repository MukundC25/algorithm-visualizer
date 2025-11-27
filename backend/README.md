# Algorithm Visualizer - Backend API

FastAPI backend for the Algorithm Visualizer application.

## Features

- **Algorithm Execution**: Execute sorting and searching algorithms with step-by-step visualization data
- **Complexity Analysis**: Analyze time and space complexity for different algorithms
- **AI Assistant**: Gemini-powered AI assistant for algorithm-related queries
- **History Tracking**: Store and retrieve algorithm execution history
- **Database**: SQLite database for persistent storage

## Tech Stack

- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Google Gemini AI**: AI-powered assistant
- **SQLite**: Lightweight database
- **Uvicorn**: ASGI server

## Project Structure

```
backend/
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── routers/                   # API route handlers
│   ├── algorithms.py          # Algorithm execution endpoints
│   ├── complexity.py          # Complexity analysis endpoints
│   ├── ai.py                  # AI assistant endpoints
│   └── history.py             # History endpoints
├── core/                      # Core business logic
│   ├── algorithm_engine/      # Algorithm implementations
│   │   ├── sorting/           # Sorting algorithms
│   │   └── searching/         # Searching algorithms
│   ├── analyzer/              # Complexity analyzer
│   └── utils/                 # Utility functions
├── models/                    # Pydantic models
│   ├── request_models.py      # Request schemas
│   └── response_models.py     # Response schemas
└── database/                  # Database layer
    ├── models.py              # SQLAlchemy models
    └── connection.py          # Database connection
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
cd backend
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///./algorithm_visualizer.db
FRONTEND_URL=http://localhost:3000
HOST=0.0.0.0
PORT=8000
```

**Get Gemini API Key:**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and paste it into your `.env` file

### 4. Run the Server

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

## API Endpoints

### Algorithm Execution
- `POST /api/execute-algorithm` - Execute an algorithm and get step-by-step visualization

### Complexity Analysis
- `POST /api/analyze-complexity` - Analyze algorithm complexity

### AI Assistant
- `POST /api/ai/query` - Query the AI assistant about algorithms

### History
- `GET /api/history` - Get algorithm execution history

### Health Check
- `GET /api/health` - Check API health status

## Example API Calls

### Execute Bubble Sort

```bash
curl -X POST "http://localhost:8000/api/execute-algorithm" \
  -H "Content-Type: application/json" \
  -d '{
    "algorithm_type": "bubble",
    "array": [64, 34, 25, 12, 22, 11, 90]
  }'
```

### Analyze Complexity

```bash
curl -X POST "http://localhost:8000/api/analyze-complexity" \
  -H "Content-Type: application/json" \
  -d '{
    "algorithm_type": "quick",
    "array_size": 100
  }'
```

### Query AI Assistant

```bash
curl -X POST "http://localhost:8000/api/ai/query" \
  -H "Content-Type: application/json" \
  -d '{
    "user_query": "What is the time complexity of Bubble Sort?",
    "context": "bubble"
  }'
```

## Supported Algorithms

### Sorting Algorithms
- Bubble Sort
- Quick Sort
- Merge Sort
- Selection Sort
- Insertion Sort

### Searching Algorithms
- Linear Search
- Binary Search

## Database Schema

### AlgorithmExecution
- Stores algorithm execution history
- Fields: id, algorithm_type, algorithm_name, array_size, comparisons, swaps, category, timestamp

### AIQuery
- Stores AI assistant queries and responses
- Fields: id, user_query, ai_response, context, timestamp

### ComplexityAnalysis
- Stores complexity analysis results
- Fields: id, algorithm_type, algorithm_name, array_size, estimated_operations, timestamp

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
```

### Type Checking
```bash
mypy .
```

## Troubleshooting

### Database Issues
If you encounter database issues, delete the database file and restart:
```bash
rm algorithm_visualizer.db
python main.py
```

### CORS Issues
Make sure `FRONTEND_URL` in `.env` matches your frontend URL.

### Gemini API Issues
- Verify your API key is correct
- Check your API quota at [Google AI Studio](https://makersuite.google.com/)
- Ensure you have internet connectivity

## License

MIT License
