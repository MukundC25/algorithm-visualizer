from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from models.request_models import AnalyzeComplexityRequest
from models.response_models import AnalyzeComplexityResponse, ComplexityInfo
from core.analyzer import get_complexity_info, estimate_operations
from core.utils import get_algorithm_metadata
from database import get_db
from database.models import ComplexityAnalysis

router = APIRouter(prefix="/api", tags=["complexity"])


@router.post("/analyze-complexity", response_model=AnalyzeComplexityResponse)
async def analyze_complexity(
    request: AnalyzeComplexityRequest,
    db: Session = Depends(get_db)
):
    """
    Analyze the complexity of an algorithm for a given array size
    
    Args:
        request: Complexity analysis request
        db: Database session
        
    Returns:
        Complexity information and estimated operations
    """
    try:
        algorithm_type = request.algorithm_type.lower()
        
        # Get algorithm metadata
        metadata = get_algorithm_metadata(algorithm_type)
        
        # Get complexity information
        complexity_data = get_complexity_info(algorithm_type)
        complexity = ComplexityInfo(
            time_best=complexity_data["time_best"],
            time_average=complexity_data["time_average"],
            time_worst=complexity_data["time_worst"],
            space=complexity_data["space"],
            stable=complexity_data["stable"],
            in_place=complexity_data["in_place"]
        )
        
        # Estimate operations
        operations = estimate_operations(algorithm_type, request.array_size)
        
        # Store analysis in database
        analysis = ComplexityAnalysis(
            algorithm_type=algorithm_type,
            algorithm_name=metadata["name"],
            array_size=request.array_size,
            estimated_operations=operations["average"]
        )
        db.add(analysis)
        db.commit()
        
        return AnalyzeComplexityResponse(
            algorithm_type=algorithm_type,
            algorithm_name=metadata["name"],
            complexity=complexity,
            estimated_operations=operations,
            array_size=request.array_size
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
