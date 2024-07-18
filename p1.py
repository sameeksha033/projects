def depth_limit_search(array, depth_limit): 
    def dls_helper(arr, current_depth):
        if current_depth > depth_limit:
            return
        for element in arr:
            if isinstance(element, list):
                print(f"At depth {current_depth}: Encountered nested list, diving deeper...")
                dls_helper(element, current_depth + 1) 
            else:
                print(f"At depth {current_depth}: Processing element:{element}")
# Start the depth-limited search with the initial depth of 0 
        dls_helper(array, 0)
# Example usage
nested_array = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10, 11]]]]
depth_limit = 2
depth_limit_search(nested_array, depth_limit)