from typing import List, Dict, Any


def selection_sort(arr: List[int]) -> List[Dict[str, Any]]:
    """
    Selection Sort Algorithm
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: No
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
        min_index = i
        
        # Show selection of current position
        selecting_array = [
            {
                **el,
                "isComparing": idx == i,
                "isSorted": idx < i
            }
            for idx, el in enumerate(working_array)
        ]
        steps.append({
            "array": selecting_array,
            "comparisons": comparisons,
            "swaps": swaps,
            "description": f"Finding minimum element from position {i} onwards"
        })

        for j in range(i + 1, n):
            comparisons += 1
            search_array = [
                {
                    **el,
                    "isComparing": idx == j,
                    "isPivot": idx == min_index,
                    "isSorted": idx < i
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": search_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Comparing {working_array[j]['value']} with current minimum {working_array[min_index]['value']}"
            })

            if working_array[j]["value"] < working_array[min_index]["value"]:
                min_index = j

        # Swap if needed
        if min_index != i:
            working_array[i], working_array[min_index] = working_array[min_index], working_array[i]
            swaps += 1

            swap_array = [
                {
                    **el,
                    "isSwapping": idx == i or idx == min_index,
                    "isSorted": idx <= i
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": swap_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Swapped elements at positions {i} and {min_index}"
            })

    # Final sorted array
    final_array = [{"value": el["value"], "id": el["id"], "isSorted": True} for el in working_array]
    steps.append({
        "array": final_array,
        "comparisons": comparisons,
        "swaps": swaps,
        "description": "Selection sort completed!"
    })

    return steps
