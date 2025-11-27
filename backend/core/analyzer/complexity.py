from typing import Dict
import math


COMPLEXITY_DATABASE = {
    "bubble": {
        "name": "Bubble Sort",
        "category": "sorting",
        "time_best": "O(n)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "stable": True,
        "in_place": True
    },
    "quick": {
        "name": "Quick Sort",
        "category": "sorting",
        "time_best": "O(n log n)",
        "time_average": "O(n log n)",
        "time_worst": "O(n²)",
        "space": "O(log n)",
        "stable": False,
        "in_place": True
    },
    "merge": {
        "name": "Merge Sort",
        "category": "sorting",
        "time_best": "O(n log n)",
        "time_average": "O(n log n)",
        "time_worst": "O(n log n)",
        "space": "O(n)",
        "stable": True,
        "in_place": False
    },
    "selection": {
        "name": "Selection Sort",
        "category": "sorting",
        "time_best": "O(n²)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "stable": False,
        "in_place": True
    },
    "insertion": {
        "name": "Insertion Sort",
        "category": "sorting",
        "time_best": "O(n)",
        "time_average": "O(n²)",
        "time_worst": "O(n²)",
        "space": "O(1)",
        "stable": True,
        "in_place": True
    },
    "linear": {
        "name": "Linear Search",
        "category": "searching",
        "time_best": "O(1)",
        "time_average": "O(n)",
        "time_worst": "O(n)",
        "space": "O(1)",
        "stable": True,
        "in_place": True
    },
    "binary": {
        "name": "Binary Search",
        "category": "searching",
        "time_best": "O(1)",
        "time_average": "O(log n)",
        "time_worst": "O(log n)",
        "space": "O(1)",
        "stable": True,
        "in_place": True
    }
}


def get_complexity_info(algorithm_type: str) -> Dict:
    """
    Get complexity information for an algorithm
    
    Args:
        algorithm_type: Type of algorithm (bubble, quick, merge, etc.)
        
    Returns:
        Dictionary containing complexity information
    """
    if algorithm_type not in COMPLEXITY_DATABASE:
        raise ValueError(f"Unknown algorithm type: {algorithm_type}")
    
    return COMPLEXITY_DATABASE[algorithm_type]


def estimate_operations(algorithm_type: str, array_size: int) -> Dict[str, int]:
    """
    Estimate the number of operations for different cases
    
    Args:
        algorithm_type: Type of algorithm
        array_size: Size of the input array
        
    Returns:
        Dictionary with estimated operations for best, average, and worst cases
    """
    n = array_size
    
    # Estimation formulas based on complexity
    estimates = {
        "bubble": {
            "best": n,  # O(n) when already sorted
            "average": (n * n) // 2,  # O(n²)
            "worst": n * n  # O(n²)
        },
        "quick": {
            "best": int(n * math.log2(n)) if n > 1 else n,  # O(n log n)
            "average": int(n * math.log2(n)) if n > 1 else n,  # O(n log n)
            "worst": n * n  # O(n²)
        },
        "merge": {
            "best": int(n * math.log2(n)) if n > 1 else n,  # O(n log n)
            "average": int(n * math.log2(n)) if n > 1 else n,  # O(n log n)
            "worst": int(n * math.log2(n)) if n > 1 else n  # O(n log n)
        },
        "selection": {
            "best": n * n,  # O(n²)
            "average": n * n,  # O(n²)
            "worst": n * n  # O(n²)
        },
        "insertion": {
            "best": n,  # O(n)
            "average": (n * n) // 2,  # O(n²)
            "worst": n * n  # O(n²)
        },
        "linear": {
            "best": 1,  # O(1) - found at first position
            "average": n // 2,  # O(n)
            "worst": n  # O(n)
        },
        "binary": {
            "best": 1,  # O(1) - found at middle
            "average": int(math.log2(n)) if n > 1 else 1,  # O(log n)
            "worst": int(math.log2(n)) if n > 1 else 1  # O(log n)
        }
    }
    
    if algorithm_type not in estimates:
        raise ValueError(f"Unknown algorithm type: {algorithm_type}")
    
    return estimates[algorithm_type]
