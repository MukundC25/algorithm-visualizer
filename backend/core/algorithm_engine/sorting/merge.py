from typing import List, Dict, Any


def merge_sort(arr: List[int]) -> List[Dict[str, Any]]:
    """
    Merge Sort Algorithm
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    In-place: No
    
    Args:
        arr: List of integers to sort
        
    Returns:
        List of steps showing the sorting process
    """
    steps = []
    working_array = [{"value": val, "id": idx} for idx, val in enumerate(arr)]
    comparisons = 0
    swaps = 0

    def merge(left: int, mid: int, right: int):
        nonlocal comparisons, swaps
        
        left_arr = working_array[left:mid + 1]
        right_arr = working_array[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_arr) and j < len(right_arr):
            comparisons += 1
            step_array = [
                {
                    **el,
                    "isComparing": idx >= left and idx <= right,
                    "isSorted": idx < left or idx > right
                }
                for idx, el in enumerate(working_array)
            ]
            steps.append({
                "array": step_array,
                "comparisons": comparisons,
                "swaps": swaps,
                "description": f"Merging: comparing {left_arr[i]['value']} and {right_arr[j]['value']}"
            })

            if left_arr[i]["value"] <= right_arr[j]["value"]:
                working_array[k] = left_arr[i]
                i += 1
            else:
                working_array[k] = right_arr[j]
                j += 1
            swaps += 1
            k += 1

        while i < len(left_arr):
            working_array[k] = left_arr[i]
            i += 1
            k += 1
            swaps += 1

        while j < len(right_arr):
            working_array[k] = right_arr[j]
            j += 1
            k += 1
            swaps += 1

    def merge_sort_helper(left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(left, mid)
            merge_sort_helper(mid + 1, right)
            merge(left, mid, right)

    merge_sort_helper(0, len(working_array) - 1)

    # Final sorted array
    final_array = [{"value": el["value"], "id": el["id"], "isSorted": True} for el in working_array]
    steps.append({
        "array": final_array,
        "comparisons": comparisons,
        "swaps": swaps,
        "description": "Merge sort completed!"
    })

    return steps
