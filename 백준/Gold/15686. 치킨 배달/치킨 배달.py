import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(input().split()) for _ in range(n)]

houses = []
chickens = []

# This list will hold the sorted distances for each house.
# dists_from_house[i] = list of (distance, chicken_bitmask) for houses[i]
dists_from_house = [] 

# 1. Find all coordinates
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            houses.append((i, j))
            dists_from_house.append([]) # Add a new empty list for this house
        elif city[i][j] == '2':
            chickens.append((i, j))

# 2. Pre-calculate all distances from each house to each chicken shop
for idx_house, (hx, hy) in enumerate(houses):
    for idx_chicken, (cx, cy) in enumerate(chickens):
        dist = abs(hx - cx) + abs(hy - cy)
        bitmask = 1 << idx_chicken
        dists_from_house[idx_house].append((dist, bitmask))
    
    # Sort this house's chicken shops by distance (closest first)
    dists_from_house[idx_house].sort()

num_chickens = len(chickens)
min_city_street = float('inf') # Use 'inf' for robustness

def dfs(depth, chosen_chicken_mask, chickens_to_choose, chickens_to_close):
    """
    Backtracking function to find the best combination of M chicken shops.
    - depth: The index of the chicken shop we are currently deciding on.
    - chosen_chicken_mask: A bitmask of shops we have decided to KEEP OPEN.
    - chickens_to_choose: How many more shops we MUST choose to reach M.
    - chickens_to_close: How many more shops we CAN close.
    """
    
    # Base Case: We've made a decision for all chicken shops
    if depth == num_chickens:
        global min_city_street
        total_street = 0
        
        for chicken_dists_for_house in dists_from_house:
            # Pruning: If this combo is already worse than our best, stop.
            if total_street >= min_city_street:
                return
            
            # Find the closest *chosen* chicken shop for this one house
            for chicken_dist, chicken_bitmask in chicken_dists_for_house:
                # Use bitwise & to check if this shop is in our chosen mask
                if chicken_bitmask & chosen_chicken_mask:
                    total_street += chicken_dist
                    break # Found the closest one, move to the next house
        
        # Update the global minimum if this combination is better
        if total_street < min_city_street:
            min_city_street = total_street
        return

    # --- Recursive Steps ---

    # Option 1: Keep this chicken shop (index = depth)
    # We can only do this if we still have shops left to choose
    if chickens_to_choose > 0:
        new_mask = chosen_chicken_mask | (1 << depth)
        dfs(depth + 1, new_mask, chickens_to_choose - 1, chickens_to_close)

    # Option 2: Close this chicken shop (index = depth)
    # We can only do this if we still have shops left to close
    if chickens_to_close > 0:
        dfs(depth + 1, chosen_chicken_mask, chickens_to_choose, chickens_to_close - 1)
    
    return


# Start the search
# We start at shop 0, with an empty mask, needing to choose M shops,
# and having (total - M) shops available to close.
dfs(0, 0, m, num_chickens - m)

print(min_city_street)