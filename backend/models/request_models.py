from pydantic import BaseModel, Field
from typing import List, Optional


class ExecuteAlgorithmRequest(BaseModel):
    """Request model for executing an algorithm"""
    algorithm_type: str = Field(..., description="Type of algorithm: bubble, quick, merge, selection, insertion, linear, binary")
    array: List[int] = Field(..., description="Input array of integers")
    search_target: Optional[int] = Field(None, description="Target value for search algorithms")

    class Config:
        json_schema_extra = {
            "example": {
                "algorithm_type": "bubble",
                "array": [64, 34, 25, 12, 22, 11, 90],
                "search_target": None
            }
        }


class AnalyzeComplexityRequest(BaseModel):
    """Request model for complexity analysis"""
    algorithm_type: str = Field(..., description="Type of algorithm to analyze")
    array_size: int = Field(..., description="Size of the input array", gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "algorithm_type": "bubble",
                "array_size": 100
            }
        }


class AIQueryRequest(BaseModel):
    """Request model for AI assistant queries"""
    user_query: str = Field(..., description="User's question about algorithms")
    context: Optional[str] = Field(None, description="Additional context (current algorithm, etc.)")

    class Config:
        json_schema_extra = {
            "example": {
                "user_query": "What is the time complexity of Bubble Sort?",
                "context": "bubble"
            }
        }
