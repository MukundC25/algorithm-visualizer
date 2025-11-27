from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class AlgorithmStep(BaseModel):
    """Single step in algorithm execution"""
    array: List[Dict[str, Any]] = Field(..., description="Array state at this step")
    comparisons: int = Field(..., description="Total comparisons so far")
    swaps: int = Field(..., description="Total swaps so far")
    description: str = Field(..., description="Description of this step")


class ComplexityInfo(BaseModel):
    """Complexity analysis information"""
    time_best: str = Field(..., description="Best case time complexity")
    time_average: str = Field(..., description="Average case time complexity")
    time_worst: str = Field(..., description="Worst case time complexity")
    space: str = Field(..., description="Space complexity")
    stable: bool = Field(..., description="Whether the algorithm is stable")
    in_place: bool = Field(..., description="Whether the algorithm is in-place")


class ExecuteAlgorithmResponse(BaseModel):
    """Response model for algorithm execution"""
    algorithm_type: str = Field(..., description="Type of algorithm executed")
    algorithm_name: str = Field(..., description="Human-readable algorithm name")
    steps: List[AlgorithmStep] = Field(..., description="Step-by-step execution trace")
    complexity: ComplexityInfo = Field(..., description="Complexity information")
    total_comparisons: int = Field(..., description="Total comparisons made")
    total_swaps: int = Field(..., description="Total swaps made")
    timestamp: str = Field(..., description="Execution timestamp")
    category: str = Field(..., description="Algorithm category: sorting or searching")


class AnalyzeComplexityResponse(BaseModel):
    """Response model for complexity analysis"""
    algorithm_type: str = Field(..., description="Type of algorithm analyzed")
    algorithm_name: str = Field(..., description="Human-readable algorithm name")
    complexity: ComplexityInfo = Field(..., description="Complexity information")
    estimated_operations: Dict[str, int] = Field(..., description="Estimated operations for given array size")
    array_size: int = Field(..., description="Array size used for analysis")


class AIQueryResponse(BaseModel):
    """Response model for AI queries"""
    response: str = Field(..., description="AI-generated response")
    timestamp: str = Field(..., description="Response timestamp")


class HistoryEntry(BaseModel):
    """Single history entry"""
    id: int
    algorithm_type: str
    array_size: int
    comparisons: int
    swaps: int
    timestamp: datetime


class HistoryResponse(BaseModel):
    """Response model for history queries"""
    entries: List[HistoryEntry] = Field(..., description="List of history entries")
    total: int = Field(..., description="Total number of entries")


class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="Service status")
    timestamp: str = Field(..., description="Current timestamp")
    version: str = Field(..., description="API version")
