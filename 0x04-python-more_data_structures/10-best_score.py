#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) > 0:
        high = max([val for key, val in a_dictionary.items()])
        highScore = [key for key, val in a_dictionary.items() if val == high]
        highScore = ", ".join(highScore)
        return highScore
    return None
