def cakes(recipe, available):
    # Start with a very big number
    max_cakes = float('inf')

    # Check each ingredient in the recipe
    for ingredient, needed in recipe.items():
        if ingredient not in available:
            # If missing ingredient → can't bake
            return 0
        # How many cakes can this ingredient make?
        possible = available[ingredient] // needed
        # Keep the smallest number (the limiting ingredient)
        if possible < max_cakes:
            max_cakes = possible

    return max_cakes


# Example usage:
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))  # Output: 2
