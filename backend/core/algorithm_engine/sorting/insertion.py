from typing import List, Dict, Any


def insertion_sort(arr: List[int]) -> List[Dict[str, Any]]:
    """
    Insertion Sort Algorithm
    
    Time Complexity: O(n²) worst, O(n) best
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

    for i in range(1, n):
        key = working_array[i].copy()
        
        # Show key selection
        key_array = [
            {
                **el,
                "isComparing": idx == i,
                "isSorted": idx < i
            }
            for idx, el in enumerate(working_array)
        ]
        steps.append({
            "array": key_array,
            "comparisons": comparisons,
            "swaps": swaps,
            "description": f"Picking key element {key['value']} at position {i}"
        })

        j = i - 1
        while j >= 0 and working_array[j]["value"] > key["value"]:
            comparisons += 1
            compare_array = [
                {
                    **el,
                    "isComparing": idx == j or idx == i,
                    "isSorted": idx >= i
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": compare_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Comparing key {key['value']} with {working_array[j]['value']}"
            })

            working_array[j + 1] = working_array[j]
            swaps += 1
            j -= 1

            shift_array = [
                {
                    **el,
                    "isSwapping": idx == j + 1 or idx == j + 2,
                    "isSorted": idx >= i
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": shift_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Shifted element right to make space"
            })

        working_array[j + 1] = key
        swaps += 1

        insert_array = [
            {
                **el,
                "isSwapping": idx == j + 1,
                "isSorted": idx <= i
            }
            for idx, el in enumerate(working_array)
        ]
        steps.append({
            "array": insert_array,
            "comparisons": comparisons,
            "swaps": swaps,
            "description": f"Inserted key {key['value']} at position {j + 1}"
        })

    # Final sorted array
    final_array = [{"value": el["value"], "id": el["id"], "isSorted": True} for el in working_array]
    steps.append({
        "array": final_array,
        "comparisons": comparisons,
        "swaps": swaps,
        "description": "Insertion sort completed!"
    })

    return steps
