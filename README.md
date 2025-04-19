# Code Usage Guide

This guide demonstrates how to use the functionalities provided in the Python code (`spell_and_assign.py`).

## Spell Checker

The `SpellChecker` class provides suggestions for potentially misspelled words based on a provided text file. It ranks suggestions based on frequency and prefix similarity.

### Initialization

First, import the `SpellChecker` class and initialize it with the path to a text file containing known words. The text file will be processed to build the dictionary.

```python
from spell_and_assign import SpellChecker

# Initialize the spell checker with a word list file
# Assumes 'messages.txt' exists and contains words.
# Punctuation is ignored, and words are split by non-alphanumeric characters.
checker = SpellChecker('messages.txt') 
```

### Checking Words

Use the `check` method to get suggestions for an input word. It returns a list of up to 3 suggestions based on the internal ranking (prefix similarity, frequency, alphabetical order). It returns an empty list if the word exists exactly in the dictionary or if no suitable suggestions are found within the defined criteria.

```python
# Example usage (output depends on the content of 'messages.txt')
# Assuming 'messages.txt' contains words like IDK, IDC, LOL, LMK, If, I...

suggestions_partial = checker.check("ID") 
print(suggestions_partial) # Output might be ['IDK', 'IDC', 'I'] based on frequency and order

suggestions_misspelled = checker.check("LOK")
print(suggestions_misspelled) # Output might be ['LOL', 'LMK']

suggestions_exact = checker.check("LOL")
print(suggestions_exact) # Output: [] (if "LOL" exists exactly)

suggestions_none = checker.check("XYZ")
print(suggestions_none) # Output: [] (if no similar words are found)
```

## Preference Assignment

The `assign` function allocates participants to activities based on their preferences and the capacity of each activity. It aims to satisfy preferences while ensuring each activity has at least two designated leaders (`preference == 2`).

### Usage

Import the `assign` function and provide it with a list of preferences and a list of places (capacities) for each activity.

*   **Preferences**: A list of lists. Each inner list represents a participant. The values indicate preference for the activity at that index:
    *   `0`: Not interested
    *   `1`: Interested
    *   `2`: Interested in leading
*   **Places**: A list where each element is the integer number of available spots for the corresponding activity.

```python
from spell_and_assign import assign

# Example preferences: 5 participants, 2 activities
preferences = [[2, 1], [2, 2], [1, 1], [2, 1], [0, 2]] 
# Example places: Activity 0 has 2 spots, Activity 1 has 3 spots
places = [2, 3]

# Call the assign function
result = assign(preferences, places)

# Print the result
if result:
    print("Assignment successful:")
    for i, activity_group in enumerate(result):
        # Participants are represented by their original index (0 to N-1)
        print(f"Activity {i}: {activity_group}") 
else:
    print("Assignment not possible.")

# Example Output (one possible valid assignment):
# Assignment successful:
# Activity 0: [0, 3]
# Activity 1: [1, 2, 4] 
```

The function returns a list of lists, where each inner list contains the indices of participants assigned to that activity. If a valid assignment fulfilling all constraints (capacity, >= 2 leaders per activity, participant preferences) is not possible, it returns `None`.

## Running Tests

Unit tests are provided in `test.py` to verify the functionality of both `SpellChecker` and `assign`. To run the tests, navigate to the directory containing the files in your terminal and execute:

```bash
python -m unittest test.py
```

This command will discover and run all tests defined within the `test.py` file. The `SpellChecker` tests will temporarily create a `messages.txt` file for testing purposes and clean it up afterward.
