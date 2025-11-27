from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from datetime import datetime

from database import Base, engine
from routers import algorithms, complexity, ai, history
from models.response_models import HealthResponse

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Algorithm Visualizer API",
    description="Backend API for Algorithm Visualizer - Execute algorithms, analyze complexity, and query AI assistant",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configure CORS
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.getenv("FRONTEND_URL", "http://localhost:3000"),
        "http://localhost:3000",
        "https://*.onrender.com",
        "https://*.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(algorithms.router)
app.include_router(complexity.router)
app.include_router(ai.router)
app.include_router(history.router)


@app.get("/", tags=["root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Algorithm Visualizer API",
        "version": "1.0.0",
        "docs": "/api/docs"
    }


@app.get("/api/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat(),
        version="1.0.0"
    )


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
