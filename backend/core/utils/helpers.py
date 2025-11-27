from typing import Dict


def get_algorithm_metadata(algorithm_type: str) -> Dict[str, str]:
    """
    Get metadata for an algorithm
    
    Args:
        algorithm_type: Type of algorithm
        
    Returns:
        Dictionary with algorithm name and category
    """
    metadata = {
        "bubble": {"name": "Bubble Sort", "category": "sorting"},
        "quick": {"name": "Quick Sort", "category": "sorting"},
        "merge": {"name": "Merge Sort", "category": "sorting"},
        "selection": {"name": "Selection Sort", "category": "sorting"},
        "insertion": {"name": "Insertion Sort", "category": "sorting"},
        "linear": {"name": "Linear Search", "category": "searching"},
        "binary": {"name": "Binary Search", "category": "searching"}
    }
    
    if algorithm_type not in metadata:
        raise ValueError(f"Unknown algorithm type: {algorithm_type}")
    
    return metadata[algorithm_type]
