from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import os
from dotenv import load_dotenv
from google import genai

from models.request_models import AIQueryRequest
from models.response_models import AIQueryResponse
from database import get_db
from database.models import AIQuery

load_dotenv()

router = APIRouter(prefix="/api", tags=["ai"])

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = None
if GEMINI_API_KEY:
    client = genai.Client(api_key=GEMINI_API_KEY)


@router.post("/ai/query", response_model=AIQueryResponse)
async def query_ai(
    request: AIQueryRequest,
    db: Session = Depends(get_db)
):
    """
    Query the AI assistant (Gemini) about algorithms
    
    Args:
        request: AI query request containing user's question
        db: Database session
        
    Returns:
        AI-generated response
    """
    try:
        print(f"[AI] Received query: {request.user_query[:50]}...")
        print(f"[AI] API Key configured: {bool(GEMINI_API_KEY)}")
        print(f"[AI] Client initialized: {bool(client)}")
        
        if not client:
            print("[AI] ERROR: Gemini client not initialized")
            raise HTTPException(
                status_code=500,
                detail="GEMINI_API_KEY not configured. Please set it in the .env file."
            )
        
        # Prepare the prompt with context
        system_prompt = """You are an expert Algorithm Learning Assistant. Answer questions about sorting algorithms, search algorithms, time complexity, space complexity, and algorithm design. Keep responses concise and educational.

Available algorithms in the visualizer:
- Sorting: Bubble Sort, Quick Sort, Merge Sort, Insertion Sort, Selection Sort
- Searching: Linear Search, Binary Search

Provide accurate technical explanations and help users understand algorithm concepts."""
        
        user_prompt = request.user_query
        if request.context:
            user_prompt = f"Context: Currently viewing {request.context} algorithm.\n\nQuestion: {user_prompt}"
        
        full_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        # Generate response using new SDK
        print("[AI] Generating content with gemini-2.0-flash-exp...")
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=full_prompt
        )
        print(f"[AI] Response received: {bool(response.text)}")
        
        if not response.text:
            print("[AI] ERROR: Empty response from Gemini")
            raise HTTPException(
                status_code=500,
                detail="Failed to generate AI response"
            )
        
        ai_response = response.text
        print(f"[AI] Success! Response length: {len(ai_response)}")
        
        # Store query in database
        query_record = AIQuery(
            user_query=request.user_query,
            ai_response=ai_response,
            context=request.context
        )
        db.add(query_record)
        db.commit()
        
        return AIQueryResponse(
            response=ai_response,
            timestamp=datetime.utcnow().isoformat()
        )
        
    except Exception as e:
        # Log the error but provide a user-friendly message
        print(f"AI Query Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process AI query: {str(e)}"
        )
