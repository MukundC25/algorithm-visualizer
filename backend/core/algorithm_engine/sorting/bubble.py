from typing import List, Dict, Any


def bubble_sort(arr: List[int]) -> List[Dict[str, Any]]:
    """
    Bubble Sort Algorithm
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    In-place: Yes
    
    Args:
        arr: List of integers to sort
        
    Returns:
        List of steps showing the sorting process
    """
    steps = []
    working_array = [{"value": val, "id": idx} for idx, val in enumerate(arr)]
    comparisons = 0
    swaps = 0
    n = len(working_array)

    for i in range(n - 1):
        for j in range(n - i - 1):
            # Create comparison step
            step_array = [
                {
                    **el,
                    "isComparing": idx == j or idx == j + 1,
                    "isSorted": idx >= n - i
                }
                for idx, el in enumerate(working_array)
            ]
            
            comparisons += 1
            steps.append({
                "array": step_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Comparing elements at positions {j} and {j + 1}"
            })

            # Swap if needed
            if working_array[j]["value"] > working_array[j + 1]["value"]:
                working_array[j], working_array[j + 1] = working_array[j + 1], working_array[j]
                swaps += 1

                swap_array = [
                    {
                        **el,
                        "isSwapping": idx == j or idx == j + 1,
                        "isSorted": idx >= n - i
                    }
                    for idx, el in enumerate(working_array)
                ]

                steps.append({
                    "array": swap_array,
                    "comparisons": comparisons,
                    "swaps": swaps,
                    "description": f"Swapped elements at positions {j} and {j + 1}"
                })

    # Final sorted array
    final_array = [{"value": el["value"], "id": el["id"], "isSorted": True} for el in working_array]
    steps.append({
        "array": final_array,
        "comparisons": comparisons,
        "swaps": swaps,
        "description": "Sorting completed!"
    })

    return steps
