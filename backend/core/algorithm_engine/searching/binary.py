from typing import List, Dict, Any


def binary_search(arr: List[int], target: int) -> List[Dict[str, Any]]:
    """
    Binary Search Algorithm
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Note: Array must be sorted first
    
    Args:
        arr: List of integers to search (will be sorted)
        target: Value to find
        
    Returns:
        List of steps showing the search process
    """
    steps = []
    
    # Sort the array first
    sorted_arr = sorted(enumerate(arr), key=lambda x: x[1])
    working_array = [{"value": val, "id": idx} for idx, val in sorted_arr]
    comparisons = 0
    
    # Show sorted array
    steps.append({
        "array": [{"value": el["value"], "id": el["id"], "isSorted": True} for el in working_array],
        "comparisons": comparisons,
        "swaps": 0,
        "description": "Array sorted for binary search"
    })

    left = 0
    right = len(working_array) - 1

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        step_array = [
            {
                **el,
                "isComparing": idx == mid,
                "isPivot": idx >= left and idx <= right
            }
            for idx, el in enumerate(working_array)
        ]

        steps.append({
            "array": step_array,
            "comparisons": comparisons,
            "swaps": 0,
            "description": f"Checking middle element at position {mid}: {working_array[mid]['value']}"
        })

        if working_array[mid]["value"] == target:
            found_array = [
                {
                    **el,
                    "isFound": idx == mid
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": found_array,
                "comparisons": comparisons,
                "swaps": 0,
                "description": f"Found target {target} at position {mid}!"
            })
            break
        elif working_array[mid]["value"] < target:
            left = mid + 1
            steps.append({
                "array": step_array,
                "comparisons": comparisons,
                "swaps": 0,
                "description": f"{working_array[mid]['value']} < {target}, searching right half"
            })
        else:
            right = mid - 1
            steps.append({
                "array": step_array,
                "comparisons": comparisons,
                "swaps": 0,
                "description": f"{working_array[mid]['value']} > {target}, searching left half"
            })

    # If not found
    if left > right:
        steps.append({
            "array": working_array,
            "comparisons": comparisons,
            "swaps": 0,
            "description": f"Target {target} not found in array"
        })

    return steps
