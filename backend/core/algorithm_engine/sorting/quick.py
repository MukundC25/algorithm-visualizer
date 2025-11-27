from typing import List, Dict, Any


def quick_sort(arr: List[int]) -> List[Dict[str, Any]]:
    """
    Quick Sort Algorithm
    
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
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

    def partition(low: int, high: int) -> int:
        nonlocal comparisons, swaps
        
        pivot = working_array[high]
        i = low - 1

        # Show pivot selection
        pivot_array = [
            {**el, "isPivot": idx == high}
            for idx, el in enumerate(working_array)
        ]
        steps.append({
            "array": pivot_array,
            "comparisons": comparisons,
            "swaps": swaps,
            "description": f"Selected pivot: {pivot['value']} at position {high}"
        })

        for j in range(low, high):
            comparisons += 1
            compare_array = [
                {
                    **el,
                    "isPivot": idx == high,
                    "isComparing": idx == j
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": compare_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Comparing {working_array[j]['value']} with pivot {pivot['value']}"
            })

            if working_array[j]["value"] < pivot["value"]:
                i += 1
                if i != j:
                    working_array[i], working_array[j] = working_array[j], working_array[i]
                    swaps += 1

                    swap_array = [
                        {
                            **el,
                            "isPivot": idx == high,
                            "isSwapping": idx == i or idx == j
                        }
                        for idx, el in enumerate(working_array)
                    ]
                    steps.append({
                        "array": swap_array,
                        "comparisons": comparisons,
                        "swaps": swaps,
                        "description": f"Swapped elements at positions {i} and {j}"
                    })

        # Place pivot in correct position
        working_array[i + 1], working_array[high] = working_array[high], working_array[i + 1]
        swaps += 1

        final_swap_array = [
            {
                **el,
                "isSwapping": idx == i + 1 or idx == high,
                "isSorted": idx == i + 1
            }
            for idx, el in enumerate(working_array)
        ]
        steps.append({
            "array": final_swap_array,
            "comparisons": comparisons,
            "swaps": swaps,
            "description": f"Placed pivot in correct position: {i + 1}"
        })

        return i + 1

    def quick_sort_helper(low: int, high: int):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)

    quick_sort_helper(0, len(working_array) - 1)

    # Final sorted array
    final_array = [
        {"value": el["value"], "id": el["id"], "isSorted": True, "isPivot": False}
        for el in working_array
    ]
    steps.append({
        "array": final_array,
        "comparisons": comparisons,
        "swaps": swaps,
        "description": "Quick sort completed!"
    })

    return steps
