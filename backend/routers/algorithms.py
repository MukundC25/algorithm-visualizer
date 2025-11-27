from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from models.request_models import ExecuteAlgorithmRequest
from models.response_models import ExecuteAlgorithmResponse, AlgorithmStep, ComplexityInfo
from core.algorithm_engine import (
    bubble_sort, quick_sort, merge_sort, selection_sort, insertion_sort,
    linear_search, binary_search
)
from core.analyzer import get_complexity_info
from core.utils import get_algorithm_metadata
from database import get_db
from database.models import AlgorithmExecution

router = APIRouter(prefix="/api", tags=["algorithms"])


@router.post("/execute-algorithm", response_model=ExecuteAlgorithmResponse)
async def execute_algorithm(
    request: ExecuteAlgorithmRequest,
    db: Session = Depends(get_db)
):
    """
    Execute an algorithm and return step-by-step visualization data
    
    Args:
        request: Algorithm execution request containing algorithm type and input array
        db: Database session
        
    Returns:
        Detailed execution steps and complexity information
    """
    try:
        algorithm_type = request.algorithm_type.lower()
        
        # Get algorithm metadata
        metadata = get_algorithm_metadata(algorithm_type)
        
        # Execute the appropriate algorithm
        steps = []
        if algorithm_type == "bubble":
            steps = bubble_sort(request.array)
        elif algorithm_type == "quick":
            steps = quick_sort(request.array)
        elif algorithm_type == "merge":
            steps = merge_sort(request.array)
        elif algorithm_type == "selection":
            steps = selection_sort(request.array)
        elif algorithm_type == "insertion":
            steps = insertion_sort(request.array)
        elif algorithm_type == "linear":
            if request.search_target is None:
                raise HTTPException(
                    status_code=400,
                    detail="search_target is required for linear search"
                )
            steps = linear_search(request.array, request.search_target)
        elif algorithm_type == "binary":
            if request.search_target is None:
                raise HTTPException(
                    status_code=400,
                    detail="search_target is required for binary search"
                )
            steps = binary_search(request.array, request.search_target)
        else:
            raise HTTPException(
                status_code=400,
                detail=f"Unknown algorithm type: {algorithm_type}"
            )
        
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
        
        # Convert steps to response model
        algorithm_steps = [
            AlgorithmStep(
                array=step["array"],
                comparisons=step["comparisons"],
                swaps=step["swaps"],
                description=step["description"]
            )
            for step in steps
        ]
        
        # Get final statistics
        final_step = steps[-1] if steps else {"comparisons": 0, "swaps": 0}
        total_comparisons = final_step["comparisons"]
        total_swaps = final_step["swaps"]
        
        # Store execution in database
        execution = AlgorithmExecution(
            algorithm_type=algorithm_type,
            algorithm_name=metadata["name"],
            array_size=len(request.array),
            comparisons=total_comparisons,
            swaps=total_swaps,
            category=metadata["category"]
        )
        db.add(execution)
        db.commit()
        
        # Return response
        return ExecuteAlgorithmResponse(
            algorithm_type=algorithm_type,
            algorithm_name=metadata["name"],
            steps=algorithm_steps,
            complexity=complexity,
            total_comparisons=total_comparisons,
            total_swaps=total_swaps,
            timestamp=datetime.utcnow().isoformat(),
            category=metadata["category"]
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
