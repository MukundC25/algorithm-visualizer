from typing import List, Dict, Any


def linear_search(arr: List[int], target: int) -> List[Dict[str, Any]]:
    """
    Linear Search Algorithm
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        arr: List of integers to search
        target: Value to find
        
    Returns:
        List of steps showing the search process
    """
    steps = []
    working_array = [{"value": val, "id": idx} for idx, val in enumerate(arr)]
    comparisons = 0

    for i in range(len(working_array)):
        comparisons += 1
        step_array = [
            {
                **el,
                "isComparing": idx == i,
                "isFound": idx == i and el["value"] == target
            }
            for idx, el in enumerate(working_array)
        ]

        description = (
            f"Found target {target} at position {i}!"
            if working_array[i]["value"] == target
            else f"Checking position {i}: {working_array[i]['value']} ≠ {target}"
        )

        steps.append({
            "array": step_array,
            "comparisons": comparisons,
            "swaps": 0,
            "description": description
        })

        if working_array[i]["value"] == target:
            break

    # If not found, add final step
    if not any(el["value"] == target for el in working_array):
        steps.append({
            "array": working_array,
            "comparisons": comparisons,
            "swaps": 0,
            "description": f"Target {target} not found in array"
        })

    return steps
