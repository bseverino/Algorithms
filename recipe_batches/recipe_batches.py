#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    """
    -Initialize an empty list of possible batches
    -Check if all recipe ingredients are on hand; if not, return 0
    -Compare each corresponding ingredient
    -If ingredients on hand are less than recipe ingredients, return 0
    -Else, divide ingredients on hand by recipe ingredients
    -Append the result to the list of possible batches
    -Return the lowest possible batch
    """
    list_batches = []
    r = set(recipe.keys())

    for key in r:
        if key not in ingredients:
            return 0
        elif recipe[key] > ingredients[key]:
            return 0
        else:
            result = math.floor(ingredients[key] / recipe[key])
            list_batches.append(result)

    return min(list_batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 50, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
