from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional

from models.response_models import HistoryResponse, HistoryEntry
from database import get_db
from database.models import AlgorithmExecution

router = APIRouter(prefix="/api", tags=["history"])


@router.get("/history", response_model=HistoryResponse)
async def get_history(
    algorithm_type: Optional[str] = Query(None, description="Filter by algorithm type"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of entries to return"),
    db: Session = Depends(get_db)
):
    """
    Get algorithm execution history
    
    Args:
        algorithm_type: Optional filter by algorithm type
        limit: Maximum number of entries to return
        db: Database session
        
    Returns:
        List of historical algorithm executions
    """
    try:
        # Build query
        query = db.query(AlgorithmExecution)
        
        # Apply filter if provided
        if algorithm_type:
            query = query.filter(AlgorithmExecution.algorithm_type == algorithm_type.lower())
        
        # Order by most recent first
        query = query.order_by(AlgorithmExecution.timestamp.desc())
        
        # Get total count
        total = query.count()
        
        # Apply limit
        executions = query.limit(limit).all()
        
        # Convert to response model
        entries = [
            HistoryEntry(
                id=execution.id,
                algorithm_type=execution.algorithm_type,
                array_size=execution.array_size,
                comparisons=execution.comparisons,
                swaps=execution.swaps,
                timestamp=execution.timestamp
            )
            for execution in executions
        ]
        
        return HistoryResponse(
            entries=entries,
            total=total
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
