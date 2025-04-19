import os
from spell_and_assign import SpellChecker, assign
import unittest

def validate_allocation(preferences, places, result):
    if len(result) != len(places): # not enough/too many activities
        return f"Expected {len(places)} activities, got {len(result)}:\n{result}"

    flattened_result = []
    for i, num_places in enumerate(places):
        flattened_result += result[i]

        # count leaders and check everyone wants to do activity
        count = 0
        for person in result[i]:
            if preferences[person][i] == 2:
                count += 1
            elif preferences[person][i] == 0:
                return f"The participant {person} did not want to do activity {i}:\n{result}"

        if count < 2: # not enough leaders
            return f"Only {count} leaders in activity {i}:\n{result}"
        elif len(result[i]) != num_places: # not enough/too many places
            return f"Expected {num_places} in activity {i}, got {len(result[i])}:\n{result}"

    if len(set(flattened_result)) != len(flattened_result): # there's duplicates
        return f"There was duplicate participants in the result:\n{result}"

class TestAssigner(unittest.TestCase):
    def test_spec_example(self):
        preferences = [[2, 1], [2, 2], [1, 1], [2, 1], [0, 2]]
        places = [2, 3]
        self._check_if_expected_not_none(preferences, places)

    def test_my_example_1(self):
        preferences = [[2, 1], [2, 2], [1, 1], [1, 1], [0, 2]]
        places = [2, 3]
        self.assertIsNone(assign(preferences, places))

    def test_my_example_2(self):
        preferences = [[1,1] for _ in range(8)]
        places = [2,6]
        self.assertIsNone(assign(preferences, places))
        
    def _check_if_expected_not_none(self, preferences, places):
        result = assign(preferences, places)
        self.assertIsNotNone(result)
        error_message = validate_allocation(preferences, places, result)
        self.assertIsNone(error_message, error_message)
    

class TestSpellChecker(unittest.TestCase):
    def test_example_from_prompt(self):
        """Tests the specific example provided in the prompt."""
        # Create the Messages.txt file for this test
        messages_content = """
            Oh, LOL.
            I do not understand. ELI5.
            IDK. Tell me more.
            LMK if you want to go.
            If you will not go, me neither.
            I know how to do this, AMA.
            Fine, IDC.
            BTW, I will not come back home for dinner tonight.
            IDK. Tell me more.
        """
        messages_filename = "messages.txt"
        with open(messages_filename, "w") as f:
            f.write(messages_content)

        try:
            myChecker = SpellChecker(messages_filename)
            self.assertEqual(myChecker.check("IDK"), [])
            self.assertEqual(myChecker.check("zoo"), [])
            self.assertCountEqual(myChecker.check("LOK"), ["LOL", "LMK"])
            self.assertCountEqual(myChecker.check("IDP"), ["IDK", "IDC", "I"])
            self.assertCountEqual(myChecker.check("Ifc"), ["If", "I", "IDK"])
        finally:
            # Clean up the created file
            if os.path.exists(messages_filename):
                os.remove(messages_filename)

if __name__ == '__main__':
    unittest.main()

