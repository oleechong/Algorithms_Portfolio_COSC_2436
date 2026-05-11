"""
COSC 2436 - Programming Fundamentals III
Assignment: Knapsack Problem - Dynamic Programming
"""

def calculate_total_value(solution, items):
    """
    TODO 1: Implement calculate_total_value
    Converts a list of item names into a total dollar value.
    """
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total

def knapsack(items, capacity):
    """
    Solve the knapsack problem using dynamic programming.
    """
    n = len(items)
    # grid[i][w] stores the list of item names for that subproblem
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            # TODO 2: Check if current item's weight exceeds current capacity
            if weight > w:
                # TODO: Copy solution from row above (use slice-copy to avoid reference issues)
                grid[i][w] = grid[i - 1][w][:]
            else:
                # TODO 3: Build the two candidate solutions
                # Include: current item + optimal solution for remaining capacity
                include_solution = grid[i - 1][w - weight][:] + [item_name]
                # Exclude: just the optimal solution from the row above
                exclude_solution = grid[i - 1][w][:]
                
                # TODO 4: Convert each candidate to a dollar value
                include_val = calculate_total_value(include_solution, items)
                exclude_val = calculate_total_value(exclude_solution, items)
                
                # TODO 5: Store the winner in grid[i][w]
                if include_val > exclude_val:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution
    
    return grid

def display_grid(grid, items):
    """
    Display the dynamic programming grid in a formatted table.
    """
    n = len(items)
    cell_width = 12
    
    # TODO 6: Build the header row (Capacity numbers)
    header = ""
    for i in range(1, len(grid[0])):
        header += "{:>{width}}".format(str(i), width=cell_width)
    print(" " * cell_width + header)
    
    # TODO: Print each data row
    for i in range(1, n + 1):
        # TODO 7: Start row with item name (left-aligned)
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)
        
        # TODO 8: Fill in the data columns
        for cell in grid[i][1:]:
            if cell:
                # Calculate total value of items in this cell
                val = calculate_total_value(cell, items)
                # Concatenate first letter of each item name
                letters = "".join([name[0] for name in cell])
                # TODO 8: Format as $VALUE(LETTERS)
                cell_text = f"${val}({letters})"
                row += "{:>{width}}".format(cell_text, width=cell_width)
            else:
                # TODO 9: Add empty space for cells with no items
                row += " " * cell_width
        
        print(row)

# Test data - items with (name, weight, value)
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

# TODO 10: Call the knapsack function and store the result
grid = knapsack(items, capacity)

# TODO 11: Display the grid (Uncommented for execution)
display_grid(grid, items)