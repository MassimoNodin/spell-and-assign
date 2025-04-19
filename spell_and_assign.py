class TrieNode:
    def __init__(self):
        """
        Function Description: Initialises a TrieNode instance.

        Approach Description: This method sets up the structure of a trie node, which is used to represent a single node in a trie. Each node can store child nodes representing subsequent characters, track word ranking based on prefix similarity and frequency, and indicate whether it is the end of a word. It also counts how many times the word is in the input file.

        Input: 
            None
        
        Output: 
            None

        Time Complexity: O(1)
        
        Time Complexity Analysis: 
            Each of the initialisations in the method takes constant time, so the overall time complexity of the method is O(1).

        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            The self.children is a fixed size list of 62 elements, leading to O(62), O(1) space complexity.
            The self.ranking is a fixed size list of 3 elements, each containing a tuple of the form (prefix similarity, frequency, word), leading to O(3), O(1) space complexity.
            The self.is_end_of_word is a boolean value, leading to O(1) space complexity.
            The self.frequency is an integer value, leading to O(1) space complexity.
        """
        # Initialise the TrieNode with 62 children, one for each alphanumeric character 26 + 26 + 10 = 52 (a-z, A-Z, 0-9)
        self.children = [None] * 62
        # Initialise the ranking with 3 elements, each containing a tuple of the form (prefix similarity, frequency, word)
        self.ranking = Ranking()
        # Store if the current node is the end of a word
        self.is_end_of_word = False
        # Store the amount of times the word features in the input file
        self.frequency = 0


class Trie:
    def __init__(self):
        """
        Function Description: Initialises a Trie instance.

        Approach Description: This method creates a Trie instance, which stores the words in a trie structure. The Trie stores a reference to the root TrieNode.

        Input:
            None

        Output:
            None

        Time Complexity: O(1)

        Time Complexity Analysis:
            The method initialises the Trie instance with a constant time complexity of O(1).

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            The space for the root node is fixed at a costant 1 element leading to O(1) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        self.root = TrieNode()

    def _char_to_index(self, char):
        """
        Function Description: Converts a character to an index in the list of characters abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.

        Approach Description: This method converts a character to the index of the chacter in the string abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.
        
        Input:
            char: a character to be converted to an index

        Output:
            index: an integer representing the index of the character in the list

        Time Complexity: O(1)
    
        Time Complexity Analysis:
            The ord method has a constant time complexity of O(1), leading to O(1) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            The space for the index is fixed at a costant 1 element leading to O(1) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        if 'a' <= char <= 'z':
            return ord(char) - 97
        elif 'A' <= char <= 'Z':
            return ord(char) - 39
        elif '0' <= char <= '9':
            return ord(char) + 4

    def insert(self, word):
        """
        Function Description: Inserts a word into the Trie.

        Approach Description: This method iterates over each character in the inputed word and inserts a new trie node if there is no child node for the character. The method also updates the ranking of the word based on the frequency and ASCCI character value. The method then sets the is_end_of_word attribute of the last node to True and increments the frequency of the word.

        Input:
            word: a string representing the word to be inserted into the trie

        Output:
            None

        Time Complexity: O(W) where W is the number of characters in the input word

        Time Complexity Analysis: O(W), where W is the number of characters in the input word
            Initiliasing the node as the root node has a constant time complexity of O(1).
            Similarly, initialising the previous_nodes list has a constant time complexity of O(1).
            The for loop iterates over each character in the input word leading to O(W) time complexity.
            The _char_to_index method has a constant time complexity of O(1) leading to O(W*1), O(W) time complexity.
            Each of creating a new trie node, assigning the new child node and appending the node to the previous_nodes list has a constant time complexity of O(1) leading to O(W*1), O(W) time complexity.
            The for loop iterates over each node in the previous_nodes list leading to O(W+W), O(W) time complexity.
            The insert method called inside the for loop has a time complexity of O(1) leading to O(W*1), O(W) time complexity.
            The is_end_of_word attribute of the last node is set to True and the frequency of the word is incremented, both of which have a constant time complexity of O(1) leading to O(W*1), O(W) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Space Complexity: O(W)

        Space Complexity Analysis:
            The space for the node is fixed at a costant 1 element leading to O(1) space complexity.
            The space for the previous_nodes list is proportional to the number of characters in the input word leading to O(W) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
            
        Auxiliary Space Complexity: O(1)

        Auxiliary Space Complexity Analysis:
            The auxiliary space complexity is equal to space complexity - input size, therefore the auxiliary space complexity is O(W) - O(W) = O(1).

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        # Initialise the node as the root node
        node = self.root
        # Keep track of the previous nodes to allow for backtracking of nodes
        previous_nodes = []
        # Iterate over each character in the word
        for char in word:
            # Convert the character to an index
            index = self._char_to_index(char)
            # If there is no trie node for the character, insert a new trie node
            if not node.children[index]:
                node.children[index] = TrieNode()
            # Move to the child node
            node = node.children[index]
            # Keep track of the previous nodes
            previous_nodes.append(node)
        # Update the ranking of the word based on the frequency and ASCCI character value
        for prefixIndex, prev_node in enumerate(previous_nodes):
            prev_node.ranking.insert((-float('inf'), node.frequency+1, word, word[prefixIndex+1] if prefixIndex+1 < len(word) else ''))
        # Set the is_end_of_word attribute of the last node to True and increment the frequency of the word
        node.is_end_of_word = True
        node.frequency += 1

    def search(self, word):
        """
        Function Description: Searches for a word in the Trie and returns the top 3 words based on prefix similarity, frequency and ASCCI character value.

        Approach Description: This method searches for a word in the Trie and returns the top 3 words based on prefix similarity, frequency and ASCCI character value. The method iterates over each character in the input word and checks if there is a child node for the character. If there is no child node for the character, the method returns the ranking of the previous node. If the character is the last character in the word and the node is the end of a word, the method returns the ranking of the node. The method then inserts the ranking of the previous node into the ranking of the current node.

        Input:
            word: a string representing the word to be searched in the trie

        Output:
            ranking: a Ranking object representing the top 3 words based on prefix similarity, frequency and ASCCI character value
            None: if the exact word is found in the trie

        Time Complexity: O(M) where M is the number of characters in the input word

        Time Complexity Analysis: where M is the number of characters in the input word
            The initialisation of the ranking object, node and previous_nodes has a constant time complexity of O(1).
            The for loop iterates over each character in the input word leading to O(M) time complexity.
            The _char_to_index method has a constant time complexity of O(1) leading to O(M*1), O(M) time complexity.
            Initialising the ranking of the previous node has a constant time complexity of O(1) leading to O(M*1), O(M) time complexity.
            If the full inputed word is found in the trie, or  the for loop exits early leading to O(M) time complexity.
            Or if there are no valid suggestions the previous_nodes will only have the root node leading to O(M + 1), O(M) time complexity.
            If there are valid suggestions, the previous_nodes will have a length of M leading to O(M + M), O(M) time complexity.
            The for loop iterates over the previous_nodes list which can have a max length of M leading to O(M + M), O(M) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Space Complexity: O(M) where M is the number of characters in the input word

        Space Complexity Analysis:
            The space for the ranking object is fixed at a costant 1 element leading to O(1) space complexity.
            The space for the node is fixed at a costant 1 element leading to O(1) space complexity.
            The space for the previous_nodes list is proportional to the number of characters in the input word leading to O(M) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
            
        Auxiliary Space Complexity: O(1)

        Auxiliary Space Complexity Analysis:
            The auxiliary space complexity is equal to space complexity - input size, therefore the auxiliary space complexity is O(M) - O(M) = O(1).

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        # Initialise the node as the root node
        node = self.root
        index = self._char_to_index(word[0])
        # Initialise the ranking object
        ranking = node.children[index].ranking if node.children[index] else Ranking()
        # Keep track of the previous nodes to allow for backtracking of nodes
        previous_nodes = []
        # Iterate over each character in the word
        for charIndex, char in enumerate(word):
            # Convert the character to an index
            index = self._char_to_index(char)
            # If there is no child node for the character, set the ranking to the previous nodes ranking and break
            if not node.children[index]:
                ranking = Ranking(node.ranking, charIndex)
                break
            if charIndex == len(word)-1:
                if node.children[index].is_end_of_word:
                    return
                ranking = node.children[index].ranking
                break
            # Move to the child node
            node = node.children[index]
            if node.ranking.rank_count:
                previous_nodes.append(node)
            # If the exact word is found in the trie, return None
            if node.is_end_of_word and charIndex == len(word)-1:
                return
        # Insert the ranking of the previous node into the ranking of the current node
        for prev_node in reversed(previous_nodes):
            if ranking.append(prev_node.ranking):
                break
        return ranking

class Ranking:
    def __init__(self, ranking=None, depth=0):
        """
        Function Description: Initialises a Ranking instance.

        Approach Description: This method initialises the ranking list, which stores the top 3 words based on prefix similarity, frequency and ASCCI character value. The ranking list is initialised with 3 elements, each containing a tuple of the form (prefix similarity, frequency, word).

        Input:
            ranking: a list of tuples representing the ranking of words
            depth: an integer representing the depth of the word in the trie or the length of the prefix similarity between the input word and the word in the trie

        Output:
            None

        Time Complexity: O(1)

        Time Complexity Analysis:
            The self.ranking initialisation iterates over a constant 3 elements leading to O(3), O(1) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space/Space Complexity: O(1)
        
        Auxiliary Space/Space Complexity Analysis:
            The space for the ranking list is fixed at a costant 3 elements leading to O(1) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        self.ranking = [(-float('inf'), -float('inf'), '', '')] * 3 if not ranking else [(depth, word[1], word[2], word[depth]) if word[2] else word for word in ranking]
        self.rank_count = 0 if not ranking else len([word for word in ranking if word[2]])

    def insert(self, word_obj):
        """
        Function Description: Inserts a word into the ranking list based on prefix similarity, frequency and ASCCI character value.

        Approach Description: This method inserts a word into the ranking list based on the prefix similarity, frequency and ASCCI character value. The method first checks if the word is already in the ranking list. If the word is not in the ranking list, the method compares the word with the existing words in the ranking list. If the word has a higher frequency than the existing words, it is inserted into the ranking list. If the word has the same frequency as an existing word, the method compares the ASCCI character value of the word with the existing word. If the word has a higher ASCCI character value, it is inserted into the ranking list. The method then calls the sink method to insert the word into the ranking list.

        Input:
            word_obj: a tuple representing the word to be inserted into the ranking list

        Output:
            None

        Time Complexity: O(1)

        Time Complexity Analysis:
            The first for loop iterates over the 3 elements in the ranking list leading to O(3), O(1) time complexity.
            If the word is in the ranking list, the next for loop iterates over 3 elements in the ranking list leading to O(3), O(1) time complexity.
            Comparing the third element of the word which is only one character has a constant time complexity of O(1) leading to O(3*1), O(1) time complexity.

            The next for loop iterates over 3 elements in the ranking list leading to O(3), O(1) time complexity.
            If there is an element which has a lower rank, it sinks the elements from a specific index leading to O(1) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios    
            
        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis: O(1)
            The method uses a constant amount of space to store the word_obj, leading to O(1) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        """
        # Check if the word is already in the ranking list
        for rankIndex, rank in enumerate(self.ranking):
            if rank[2] == word_obj[2]:
                # If the word exists, update the frequency and update its ranking
                self.ranking[rankIndex] = (rank[0], word_obj[1], rank[2], rank[3])
                for i in range(rankIndex, 0, -1):
                    if self.ranking[i][1] > self.ranking[i-1][1]\
                        or self.ranking[i][1] == self.ranking[i-1][1] and self.ranking[i][3] < self.ranking[i-1][3]:
                        self.ranking[i], self.ranking[i-1] = self.ranking[i-1], self.ranking[i]
                    return
                return
        # If the word is not in the ranking list, compare the word with the existing words in the ranking list
        for i in range(3):
            # if the word has a higher rank than an existing word, sink the existing words and insert the new word
            if self.ranking[i][1] < word_obj[1]\
                or self.ranking[i][1] == word_obj[1] and self.ranking[i][3] > word_obj[3]:
                self.sink(i)
                self.ranking[i] = word_obj
                self.rank_count += 1 if self.rank_count < 3 else 0
                return
    
    def sink(self, index):
        """
        Function Description: Sinks a word in the ranking list to the specified index.

        Approach Description: This method sinks a word in the ranking list to the specified index. The method shifts the words in the ranking list to the right to make space for the new word. The method then inserts the new word into the ranking list.

        Input:
            index: an integer representing the index to sink from
        
        Output:
            None

        Time Complexity: O(1)

        Time Complexity Analysis:
            The method iterates over a constant 3 elements leading to O(3), O(1) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            The method uses a constant amount of space to store the index and the temporary variable, leading to O(1) space complexity.
        
            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        for i in range(2-index):
            self.ranking[2-i] = self.ranking[1-i]

    def append(self, other_ranking):
        """
        Function Description: Appends the ranks from another ranking object to the end current ranking object.

        Approach Description: This method appends the ranks from another ranking object to the end current ranking object. The method iterates over each word in the other ranking object and appends the word to the current ranking object if the word is not already in the ranking list.

        Input:
            other_ranking: a Ranking object representing the ranking object to append to the current ranking object

        Output:
            None

        Time Complexity: O(1)

        Time Complexity Analysis:
            The for loop iterates over each word in the other_ranking object leading to O(3), O(1) time complexity.
            The nested for loop to check if the word is already in the ranking list has a constant time complexity of O(3) leading to O(3*3), O(1) time complexity.
            The rest of the method has a constant time complexity of O(1) leading to O(3*1), O(1) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            The method uses a constant amount of space to store the other_ranking object, leading to O(1) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        # Iterates over each word in the other ranking object
        for word in other_ranking.ranking:
            if not word[2]:
                break
            if self.rank_count == 3:
                return True
            # Check if the word is already in the ranking list
            wordExistsAlready = False
            for i in range(3):
                if word[2] == self.ranking[i][2]:
                    wordExistsAlready = True
                    break
            # If the word is already in the ranking list, continue to the next word
            if wordExistsAlready:
                continue
            # If there are no more words in the ranking list or if the current ranking list is full, break
            # If not, insert the word into the ranking list and increment the rank count
            self.ranking[self.rank_count] = word
            self.rank_count += 1

    def __getitem__(self, indicies):
        return self.ranking[indicies]
    
class SpellChecker:
    def __init__(self, file_name):
        """
        Function Description: Initialises the SpellChecker object by loading words from the input file

        Approach Description: The SpellChecker object is initialised by creating a Trie object and loading words from the input file. The load_words function is used to clean and split the input line into words, which are then inserted into the Trie object.

        Input:
            file_name: a string representing the name of the input file

        Output:
            None

        Time Complexity: O(T) where T is the number of characters in the input file

        Time Complexity Analysis: O(T), where T is the number of characters in the input file

        """
        self.trie = Trie()
        self.load_words(file_name)

    def load_words(self, file_name):
        """
        Function Description: Loads words from the input file

        Approach Description: This method loads words from the input file by opening the file and reading each line. The method then cleans and splits the line into words using the clean_and_split method. The method then inserts the words into the Trie object.

        Input:
            file_name: a string representing the name of the input file

        Output:
            None

        Time Complexity: O(T) where T is the number of characters in the input file, N is the number of lines in the input file, W is the number of words in each line

        Time Complexity Analysis: O(T), where T is the number of characters in the input file
            The open method has a constant time complexity of O(1).
            The first for loop iterates over each line in the input file leading to O(N) time complexity.
            The clean_and_split method has a time complexity of O(W) leading to O(N*W), O(T) time complexity.
            The nested for loop iterates over each word in the line leading to O(N*(W+W)), O(N*W) time complexity.
            The insert method called in the for loop has a constant time complexity of O(W) leading to O(N*(W+W)), O(N*W) time complexity.
            The amount of lines multipled by the amount of words in each line is equal to the amount of characters in the input file leading to O(T) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Space Complexity: O(W) where W is the number of characters in each line

        Space Complexity Analysis:
            The space for the words list is proportional to the number of characters in each line leading to O(W) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
            
        Auxiliary Space Complexity: O(1)

        Auxiliary Space Complexity Analysis:
            The auxiliary space complexity is equal to space complexity - input size, therefore the auxiliary space complexity is O(W) - O(W) = O(1).

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        # Load words from the input file
        with open(file_name, 'r') as file:
            for line in file:
                # Clean and split the line into words
                words = self.clean_and_split(line)
                for word in words:
                    self.trie.insert(word)

    def clean_and_split(self, line):
        """
        Function Description: Cleans and splits a line into words

        Approach Description: This method cleans and splits a line into words by iterating over each character in the line. The method ignores non-alphanumeric characters and appends alphanumeric characters to a word. The method then appends the word to a list of words.

        Input:
            line: a string representing the line to be cleaned and split into words

        Output:
            words: a list of strings representing the words in the line

        Time Complexity: O(W) where W is the number of characters in the input line

        Time Complexity Analysis: O(W), where W is the number of characters in the input line
            The for loop iterates over each character in the input line leading to O(W) time complexity.
            The append method called in the for loop has a constant time complexity of O(1) leading to O(W*1), O(W) time complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Space Complexity: O(W)

        Space Complexity Analysis:
            The space for the word list is proportional to the number of characters in the input line leading to O(W) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity: O(1)

        Auxiliary Space Complexity Analysis:
            The auxiliary space complexity is equal to space complexity - input size, therefore the auxiliary space complexity is O(W) - O(W) = O(1).

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        # Initialise the word list and a string to concatenate characters to form a word
        word = ""
        words = []
        for char in line:
            # Ignore non-alphanumeric characters
            if char.isalnum():
                word += char 
            # If it is the end of a word, append the word to the list of words
            else:
                if word:
                    words.append(word)
                    word = ""
        # If there is a word at the end of the line, append the word to the list of words
        if word:
            words.append(word)
        return words


    def check(self, input_word):
        """
        Function Description: Checks for suggestions based on the input word

        Approach Description: This method checks for suggestions based on the input word by searching for the input word in the Trie object. The method then returns the top 3 words based on prefix similarity, frequency and ASCCI character value.

        Input:
            input_word: a string representing the word to check for suggestions

        Output:
            suggestions: a list of strings representing the top 3 words based on prefix similarity, frequency and ASCCI character value

        Time Complexity: O(M) where M is the number of characters in the input word

        Time Complexity Analysis: O(M), where M is the number of characters in the input word
            The search method called in the method has a time complexity of O(M) leading to O(M) time complexity.
            Iterating over the ranking list has a constant time complexity of O(3) leading to O(3), O(1) time complexity.
            
            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios

        Auxiliary Space/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            The space for the suggestions list is fixed at a costant 3 elements leading to O(1) space complexity.

            The big Θ notation is the same as the big O notation as the time complexity is the same in the best and worst case scenarios
        """
        # Check for suggestions based on the input word
        ranking = self.trie.search(input_word)
        if not ranking:
            return []
        return [word[2] for word in ranking.ranking if word[2]]
    
class PreferenceManager:
    def __init__(self, preferences, places):
        """
        Function Description: This function initialises the PreferenceManager object with the given preferences and places.

        Approach Description: The function initialises the preferences, number of people, places, number of places, place nodes, and edges in the graph. It then creates the network for the Ford-Fulkerson algorithm and sets up the graph.

        Input:
            preferences (list): A list of lists representing the preferences of each participant for each activity.
            places (list): A list of integers representing the number of places available in each activity.

        Output:
            None

        Time Complexity: O(n * m), where n is the number of people and m is the number of places
        """
        self.preferences = preferences
        self.num_people = len(preferences)
        self.places = places
        self.num_places = len(places)
        self.place_nodes = [None for _ in range(self.num_places)]
        self.edges = self.create_network()
        self.graph_setup()
        self.calculate_path()

    def create_network(self):
        """
        Function Description: This function creates the network for the Ford-Fulkerson algorithm.

        Approach Description: The function calculates the index boundaries for the leader, people, places, and sink nodes in the graph. It then adds the people, preferences, leaders, non-leaders, and sink edges to the graph.

        Input:
            None

        Output:
            people_edges + preference_edges + leaders_edges + non_leadeer_edges + sink_edges (list): A list of tuples representing the edges in the graph.

        Time Complexity: O(n * m), where n is the number of people and m is the number of places

        Time Complexity Analysis:
            The calculate_boundaries function calculates the index boundaries for the leader, people, places, and sink nodes in the graph, leading to O(1) time complexity.
            The people edges, node addition, preference edges, leader edges, non-leader edges, and sink edges are added to the graph, leading to O(n + m + n * m + m + m + m) time complexity.
            Since n * m is the dominant term, the overall time complexity is O(n * m)

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(n * m), where n is the number of people and m is the number of places
        
        """
        # Calculate the index boundaries for the leader, people, places, and sink nodes in the graph
        boundary_leader, boundary_people, boundary_places, boundary_sink = self.calculate_boundaries()
        # Add the people, preferences, leaders, non-leaders, and sink edges to the graph
        people_edges = self.add_people_edges()
        self.add_place_nodes(boundary_leader, boundary_people)
        preference_edges = self.add_preferences(boundary_leader, boundary_people)
        leaders_edges = self.add_leader_edges(boundary_leader, boundary_places)
        non_leadeer_edges = self.add_non_leader_edges(boundary_people, boundary_places, boundary_leader)
        sink_edges = self.add_sink_edges(boundary_places, boundary_sink)
        # Return the edges in the graph
        return people_edges + preference_edges + leaders_edges + non_leadeer_edges + sink_edges

    def calculate_boundaries(self):
        """
        Function Description: This function calculates the beginning index of the leader, people, places, and sink nodes in the edges list.

        Approach Description: The boundary for the leader accounts for the nodes for each person and the source node. The boundary for the people accounts for the nodes for each person, the source node, and the leader nodes. The boundary for the places accounts for the nodes for each person, the source node, the leader nodes, and the people nodes. The boundary for the sink accounts for the nodes for each person, the source node, the leader nodes, the people nodes, and the places nodes.

        Input:
            None

        Output:
            boundary_leader (int): The beginning index of the leader nodes in the edges list.
            boundary_people (int): The beginning index of the people nodes in the edges list.
            boundary_places (int): The beginning index of the places nodes in the edges list.
            boundary_sink (int): The beginning index of the sink nodes in the edges list.

        Time Complexity: O(1)

        Time Complexity Analysis:
            The addition and multiplication operations to calculate the boundaries take O(1) time.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis:
            No additional space is used to calculate the boundaries, leading to an auxiliary space complexity of O(1).

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Calculate the boundaries for the leader, people, places, and sink nodes
        return self.num_people + 1,\
            self.num_people + self.num_places + 1, \
            2 * self.num_places + self.num_people + 1, \
            3 * self.num_places + self.num_people + 1

    def add_sink_edges(self, boundary_places, boundary_sink):
        """
        Function Description: This function adds the sink edges to the graph.

        Approach Description: The function iterates over each activity and adds an edge from the activity node to the sink node with the capacity of the activity.

        Input:
            boundary_places (int): The boundary for the places in the graph.
            boundary_sink (int): The boundary for the sink in the graph.

        Output:
            sink_edges (list): A list of tuples representing the sink edges in the graph.

        Time Complexity: O(m), where m is the number of places

        Time Complexity Analysis:
            The function iterates over each activity and adds an edge from the activity node to the sink node with the capacity of the activity. Therefore, the time complexity is O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(m), where m is the number of places

        Auxiliary Space/Space Complexity Analysis:
            The function creates a list of tuples representing the sink edges in the graph, leading to an auxiliary space complexity of O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialise a fixed size list for the sink edges
        sink_edges = [None for _ in range(self.num_places)]
        # Iterate over each activity and add an edge from the activity node to the sink node with the capacity of the activity
        for activity_index in range(self.num_places):
            sink_edges[activity_index] = ((boundary_places + activity_index, boundary_sink, self.places[activity_index]))
        return sink_edges

    def add_non_leader_edges(self, boundary_people, boundary_places, boundary_leader):
        """
        Function Description: This function adds the non-leader edges to the graph.

        Approach Description: The function iterates over each activity and adds edges from the people and leader nodes to the activity node with the capacity of the activity minus 2.

        Input:
            boundary_people (int): The boundary for the people in the graph.
            boundary_places (int): The boundary for the places in the graph.
            boundary_leader (int): The boundary for the leader in the graph.

        Output:
            people_edges (list): A list of tuples representing the non-leader edges in the graph.

        Time Complexity: O(m), where m is the number of places

        Time Complexity Analysis:
            The function iterates over each activity and adds edges from the people and leader nodes to the activity node with the capacity of the activity minus 2. Therefore, the time complexity is O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(m), where m is the number of places

        Auxiliary Space/Space Complexity Analysis:
            The function creates a list of tuples representing the non-leader edges in the graph, leading to an auxiliary space complexity of O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialise a fixed size list for the non-leader edges
        people_edges = [None for _ in range(2 * self.num_places)]
        # Iterate over each activity and add edges from the people and leader nodes to the activity node with the capacity of the activity minus 2
        for activity_index in range(self.num_places):
            people_edges[2 * activity_index] = ((boundary_people + activity_index, boundary_places + activity_index, self.places[activity_index] - 2))
            people_edges[2 * activity_index + 1] = ((boundary_leader + activity_index, boundary_people + activity_index, self.places[activity_index] - 2))
        return people_edges

    def add_leader_edges(self, boundary_leader, boundary_places):
        """
        Function Description: This function adds the leader edges to the graph.

        Approach Description: The function iterates over each activity and adds an edge from the leader node to the activity node with a capacity of 2.

        Input:
            boundary_leader (int): The boundary for the leader in the graph.
            boundary_places (int): The boundary for the places in the graph.

        Output:
            leader_edges (list): A list of tuples representing the leader edges in the graph.

        Time Complexity: O(m), where m is the number of places

        Time Complexity Analysis:
            The function iterates over each activity and adds an edge from the leader node to the activity node with a capacity of 2. Therefore, the time complexity is O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(m), where m is the number of places

        Auxiliary Space/Space Complexity Analysis:
            The function creates a list of tuples representing the leader edges in the graph, leading to an auxiliary space complexity of O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialise a fixed size list for the leader edges
        leader_edges = [None for _ in range(self.num_places)]
        # Iterate over each activity and add an edge from the leader node to the activity node with a capacity of 2
        for activity_index in range(self.num_places):
            leader_edges[activity_index] = ((boundary_leader + activity_index, boundary_places + activity_index, 2))
        return leader_edges

    def add_people_edges(self):
        """
        Function Description: This function adds the people edges to the graph.

        Approach Description: The function iterates over each person and adds an edge from the source node to the person node with a capacity of 1.

        Input:
            None

        Output:
            people_edges (list): A list of tuples representing the people edges in the graph.

        Time Complexity: O(n), where n is the number of people

        Time Complexity Analysis:
            The function iterates over each person and adds an edge from the source node to the person node with a capacity of 1. Therefore, the time complexity is O(n), where n is the number of people.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(n), where n is the number of people

        Auxiliary Space/Space Complexity Analysis:
            The function creates a list of tuples representing the people edges in the graph, leading to an auxiliary space complexity of O(n), where n is the number of people.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialise a fixed size list for the people edges
        people_edges = [None for _ in range(self.num_people)]
        # Iterate over each person and add an edge from the source node to the person node with a capacity of 1
        for people_index in range(self.num_people):
            people_edges[people_index] = ((0, people_index + 1, 1))
        return people_edges
    
    def add_place_nodes(self, boundary_leader, boundary_people):
        """
        Function Description: Adds references to the leader and people nodes in the graph.

        Approach Description: Iterates over each place and adds the leader and people nodes to the list of nodes.

        Input:
            boundary_leader (int): The boundary for the leader in the graph.
            boundary_people (int): The boundary for the people in the graph.

        Output:
            None
        
        Time Complexity: O(m), where m is the number of places

        Time Complexity Analysis:
            The function iterates over each place and adds the leader and people nodes to the list of nodes. Therefore, the time complexity is O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(m), where m is the number of places

        Auxiliary Space/Space Complexity Analysis:
            The function adds the leader and people nodes to the list of nodes, leading to an auxiliary space complexity of O(m), where m is the number of places.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Iterate over each place and add the leader and people nodes to the list of nodes
        for place_index in range(self.num_places):
            leader = boundary_leader + place_index
            people = boundary_people + place_index
            self.place_nodes[place_index] = ((leader,people))

    def add_preferences(self, boundary_leader, boundary_people):
        """
        Function Description: This function adds the preference edges to the graph.

        Approach Description: The function iterates over each person and their preferences for each activity. It then adds an edge from the person node to the activity node with a capacity of 1 if the person is interested in the activity and a capacity of 2 if the person is interested in leading the activity.

        Input:
            boundary_leader (int): The boundary for the leader in the graph.
            boundary_people (int): The boundary for the people in the graph.

        Output:
            preferences_edges (list): A list of tuples representing the preference edges in the graph.

        Time Complexity: O(n * m), where n is the number of people and m is the number of activities

        Time Complexity Analysis:
            The counting of the amont of edges needed for the preferences takes O(n * m) time, where n is the number of people and m is the number of activities.
            Initialising the preferences_edges list takes O(n * m) time as the list is of the same size as the amount of edges needed for the preferences.
            The function iterates over each person and their preferences for each activity. Therefore, the time complexity is O(n * m), where n is the number of people and m is the number of activities.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: 
            Best Case: O(n), where n is the number of people
            Average/Worst Case: O(n * m), where n is the number of people and m is the number of activities

        Auxiliary Space/Space Complexity Analysis:
            The preference_edge_count variable takes up O(1) space.

            Best Case:
                The preferences_edges list will at a minimum have a size of n because each participant will have at least one preference. Therefore, the auxiliary space complexity is O(n), where n is the number of people.

            Average/Worst Case:
                The preferences_edges list will have a size of n * m because each participant will have m preferences. Therefore, the auxiliary space complexity is O(n * m), where n is the number of people and m is the number of activities.
        """
        # Find the amount of edges needed for the preferences
        preferences_edge_count = 0
        for preference in self.preferences:
            # Count the amount of 1's and 2's in the preference list
            preferences_edge_count += preference.count(1)
            preferences_edge_count += preference.count(2)
        # Initialise a fixed size list for the preference edges
        preferences_edges = [None for _ in range(preferences_edge_count)]
        # Create an index to keep track of the current edge
        preference_edge_index = 0
        # Iterate over each person and their preferences for each activity
        for person_index, preference in enumerate(self.preferences):
            # Iterate over each activity and add an edge from the person node to the activity node with a capacity of 1 if the person is interested in the activity and a capacity of 2 if the person is interested in leading the activity
            for activity_index, interest in enumerate(preference):
                # Add an edge from the person node to the activity node with a capacity of 1 if the person is interested in the activity or leading the activity
                if interest == 1:
                    preferences_edges[preference_edge_index] = ((person_index + 1, boundary_people + activity_index, 1))
                    preference_edge_index += 1
                # If the person is interested in leading the activity,change the boundary to the leader node
                elif interest == 2:
                    preferences_edges[preference_edge_index] = ((person_index + 1, boundary_leader + activity_index, 1))
                    preference_edge_index += 1
        return preferences_edges

    def graph_setup(self):
        """
        Function Description: This function sets up the graph for the Ford-Fulkerson algorithm.

        Approach Description: The function initializes the source and sink vertices and the number of vertices in the graph. It then creates an adjacency list representation of the graph and adds the edges to the graph.

        Input:
            None

        Output:
            None
        
        Time Complexity:
            Best Case: O(n * m), where n is the number of people and m is the number of activities
            Average/Worst Case: O(n * m), where n is the number of people and m is the number of activities

        Time Complexity Analysis:
            The for loop iterates over each edge in the input list to find the maximum vertex value. Therefore, the time complexity is O(E), where E is the number of edges.
            The graph initilisation creates a list of lists for each vertex, leading to O(V) time complexity, where V is the number of vertices.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(V), where V is the number of vertices

        Auxiliary Space/Space Complexity Analysis:
            The function uses a list of lists to represent the graph, leading to an auxiliary space complexity of O(V), where V is the number of vertices.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Find the maximum vertex value
        vertex_max = 0
        # Iterate over the edges to find the maximum vertex value
        for start, end, _ in self.edges:
            vertex_max = max(vertex_max, start, end)
        # Set the source and sink vertices
        self.source = 0
        self.sink = vertex_max
        # Set the number of vertices in the graph
        self.vertices = vertex_max + 1
        # Create an adjacency list representation of the graph
        self.graph = [[] for _ in range(self.vertices)]
        # Add all edges to the graph
        self.add_edges()
    
    def calculate_path(self):
        self.ford_fulkerson()
        self.reconstructed_graph = self.reconstruct_graph()

    def add_edges(self):
        """
        Function Description: This function adds edges to the graph, representing roads with capacities.

        Approach Description: The graph is an adjacency list, where each index represents a location. Each location contains a list of edges, where each edge is represented by a list containing the destination and the capacity of the road. For each edge in the input list, the function adds a forward edge with the given capacity and a backward edge with zero capacity to the graph.

        Input:
            None

        Output: 
            None
        
        Time Complexity: O(E), where E is the number of edges

        Time Complexity Analysis: 
            The function iterates over each edge in the input list to add it to the graph. Therefore, the time complexity is O(E), where E is the number of edges.
            The append operation for adding an edge to the adjacency list takes O(1) time leading to O(E + 1), O(E).

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        
        Auxiliary Space Complexity/Space Complexity: O(1)

        Auxiliary Space/Space Complexity Analysis: 
            The function uses a constant amount of extra space for variables, resulting in an auxiliary space complexity of O(1).

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        for start, end, capacity in self.edges:
            self.graph[start].append([end, capacity])
            self.graph[end].append([start, 0])

    def bfs(self, parent):
        """
        Function Description: This function performs a breadth-first search to find a path from the source to the sink in the graph.

        Approach Description: The function initializes a list to keep track of visited vertices and a queue to store the vertices to visit. It then iterates over the queue, visiting each vertex and adding its neighbors to the queue if they have not been visited and have a positive capacity. If the sink is reached, the function returns True. Otherwise, it returns False.

        Input:
            parent (list): A list to store the parent of each vertex in the path

        Output:
            True if a path from the source to the sink is found, False otherwise

        Time Complexity: O(n^2), where n is the number of participants

        Time Complexity Analysis:
            The initialisation of teh visited list takes O(V) time, where V is the number of vertices.
            The time complexity of the breadth-first search function is O(V + E), where V is the number of vertices and E is the number of edges.
            The number of vertices is equal to the the source (1), the number of participants (n), the sink (1), the number of places (m), the number of leaders (m), and the number of people (m), leading to a total of V = 3m + 2n + 2 vertices.
        
        Auxiliary Space Complexity/Space Complexity: O(V), where V is the number of vertices
        
        Auxiliary Space/Space Complexity Analysis:
            The function uses a list to keep track of visited vertices and a queue to store the vertices to visit, leading to an auxiliary space complexity of O(V), where V is the number of vertices.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialize a list to keep track of visited vertices
        visited = [False] * self.vertices
        # Initialize a queue to store the vertices to visit
        queue = [self.source]
        # Mark the source vertex as visited
        visited[self.source] = True

        # Iterate over the queue
        while queue:
            # Get the current vertex
            current = queue.pop()
            # For each neighbor of the current vertex
            for neighbor, capacity in self.graph[current]:
                # If the neighbor has not been visited and has a positive capacity
                if not visited[neighbor] and capacity > 0:
                    # Set the parent of the neighbor to the current vertex
                    parent[neighbor] = current
                    # If the neighbor is the sink, return True
                    if neighbor == self.sink:
                        return True
                    # If the neighbor is not the sink, mark it as visited and add it to the queue
                    queue.append(neighbor)
                    visited[neighbor] = True
        # If none of the verticies with positive capacity reach the sink, return False
        return False

    def ford_fulkerson(self):
        """
        Function Description: This function implements the Ford-Fulkerson algorithm to find the maximum flow in the graph.

        Approach Description: The function initializes a parent list to store the augmenting path and the max flow to zero. It then checks if there is a path from the source to the sink using the breadth-first search function. If a path is found, the function initializes the path flow to infinity and the current node to the sink. It then finds the path from the source to the sink with the minimum flow and updates the residual capacities of the edges on the path. The function returns the max flow.

        Input:
            None

        Output:
            max_flow (int): The maximum flow in the graph

        Time Complexity: O(n^3), where n the number of participants

        Time Complexity Analysis:
            The initialisatin of the parent list takes O(V) time, where V is the number of vertices.
            The time complexity of the breadth-first search function is O(V + E), where V is the number of vertices and E is the number of edges.
            The amount of 

        Auxiliary Space Complexity/Space Complexity: O(V), where V is the number of vertices

        Auxiliary Space/Space Complexity Analysis:
            The function uses a list to store the augmenting path of length V and the max flow, leading to an auxiliary space complexity of O(V), where V is the number of vertices.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialize parent list to store the augmenting path and max flow
        parent = [-1] * self.vertices
        max_flow = 0
        # Check if there is a path from source to sink
        while self.bfs(parent):
            # Initialize path flow to infinity and the current node to the sink
            path_flow = float("Inf")
            current_node = self.sink

            # Find the path from source to sink with minimum flow
            while current_node != self.source:
                prev_node = parent[current_node]
                # Find the edge that connects current node and previous node with minimum capacity
                for edge in self.graph[prev_node]:
                    if edge[0] == current_node:
                        path_flow = min(path_flow, edge[1])
                current_node = prev_node

            # Add the minimum capacity to the max flow
            max_flow += path_flow

            # Update the residual capacities of the edges on the path
            current_node = self.sink
            while current_node != self.source:
                prev_node = parent[current_node]

                # Decrease capacity of the forward edge
                for edge in self.graph[prev_node]:
                    if edge[0] == current_node:
                        edge[1] -= path_flow

                # Increase capacity of the backward edge
                for edge in self.graph[current_node]:
                    if edge[0] == prev_node:
                        edge[1] += path_flow

                current_node = prev_node

        return max_flow

    def reconstruct_graph(self):
        """
        Function Description: This function reconstructs the graph with only the forward edges used in the flow.

        Approach Description: The function creates a new graph with the same number of vertices as the original graph. It then iterates over each vertex in the original graph and each edge in the adjacency list of the vertex. If the capacity of the edge is zero, the function adds the destination vertex to the reconstructed graph.

        Input:
            None

        Output:
            reconstructed_graph (list): A list of lists representing the reconstructed graph with only the forward edges used in the flow

        Time Complexity: O(n^2), where n is the number of participants

        Time Complexity Analysis:
            The function creates a new graph with the same number of vertices as the original graph, leading to O(V) time complexity.
            The function iterates over each vertex in the original graph and each edge in the adjacency list of the vertex, leading to O(V + E) time complexity.
            The amount of vertices is equal to 3m + 2n + 2. The amount of of edges is at worst n * m, leading to O((3m + 2n + 2) + n * m), O(n * m).
            The number of activities is equal to at most n/2, leading to O(n * n / 2), O(n^2).

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(n^2), where V is the number of vertices and E is the number of edges

        Auxiliary Space/Space Complexity Analysis:
            The function creates a new graph with the same number of vertices as the original graph and iterates over each vertex in the original graph and each edge in the adjacency list of the vertex, leading to an auxiliary space complexity of O(V + E), where V is the number of vertices and E is the number of edges.
            Described in terms of the number of participants, the auxiliary space complexity is O(n^2), where n is the number of participants.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Create a new graph with the same number of vertices as the original graph
        reconstructed_graph = [[] for _ in range(self.vertices)]
        # Iterate over each vertex in the original graph
        for start in range(self.vertices):
            # Iterate over each edge in the adjacency list of the vertex
            for edge in self.graph[start]:
                # If the capacity of the edge is zero, add the destination vertex to the reconstructed graph
                if edge[1] == 0:
                    reconstructed_graph[start].append(edge[0])
        return reconstructed_graph

        return "\n".join(result)
    
    def assign(self):
        """
        Function Description: This function assigns participants to activities based on their preferences and the number of places available in each activity.

        Approach Description: The function initialises the result list of fixed size and creates a list of the current index for each place. It then reconstructs the path of maximum flow and assigns the participants to the activities based on the leader and non-leader nodes for each place.

        Input:
            None

        Output:
            result (list): A list of lists representing the participants assigned to each activity, or None if it is not possible to assign everyone.

        Time Complexity: O(n^2), where n is the number of participants

        Time Complexity Analysis:
            The initialisation of the result list takes at most O(n^2) time, where n is the number of participants.
            The function reconstructs the path of maximum flow, leading to O(n^2) time complexity.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

        Auxiliary Space Complexity/Space Complexity: O(n^2), where n is the number of participants

        Auxiliary Space/Space Complexity Analysis:
            The function initialises the result list of fixed size and creates a list of the current index for each place, leading to an auxiliary space complexity of O(n^2), where n is the number of participants.

            The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
        """
        # Initialise the result list of fixed size
        result = [[None] * people_allowed for people_allowed in self.places]
        # Create a list of the current index for each place
        place_indexs = [0] * self.num_places
        # Reconstruct the path of maximum flow
        path = self.reconstructed_graph
        # Only get the edges from each person to the places
        people_assignments = path[1:self.num_people + 1]
        # Iterate over each place getting the leader and non leader nodes for each place
        for place_index, place in enumerate(self.place_nodes):
            # Iterate over each person and their assigned place
            for person_index, person in enumerate(people_assignments):
                # Check if the person is assigned to the leader node of the place or the non-leader node of the place
                for i in range(2):
                    if person[0] == place[i]:
                        # Assign the person to the place
                        result[place_index][place_indexs[place_index]] = (person_index)
                        place_indexs[place_index] += 1

        # Check if all places have been assigned
        for place_index in range(self.num_places):
            # If a place has less people than the number of places available, return None
            if place_indexs[place_index] < self.places[place_index]:
                return None
        return result


def assign(preferences, places):
    """
    Function Description: This function assigns participants to activities based on their preferences and the number of places available in each activity.

    Approach Description: The function creates a preference manager object with the given preferences and places. It then assigns the participants to the activities using the Ford-Fulkerson algorithm, implemented with a bredth first saerch and returns who is assigned to each activity if it is possible to assign everyone, otherwise it returns None.

    Input:
        preferences (list): A list of lists representing the preferences of each participant for each activity.
        places (list): A list of integers representing the number of places available in each activity.

    Output:
        result (list): A list of lists representing the participants assigned to each activity, or None if it is not possible to assign everyone.

    Time Complexity: O(n^3), where n is the number of participants and m is the number of activities

    Time Complexity Analysis:
        The function creates a preference manager object with the given preferences and places, leading to O(n * m) time complexity.
        The function assigns the participants to the activities using the Ford-Fulkerson algorithm, implemented with a bredth first search, leading to O(n^3) time complexity.

        The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios

    Auxiliary Space Complexity/Space Complexity: O(n^2), where n is the number of participants

    Auxiliary Space/Space Complexity Analysis:
        The function creates a preference manager object with the given preferences and places, leading to an auxiliary space complexity of O(n * m), where n is the number of participants and m is the number of activities.
        The function assigns the participants to the activities using the Ford-Fulkerson algorithm, implemented with a bredth first search, leading to an auxiliary space complexity of O(n^2), where n is the number of participants.

        The big Θ notation is the same as the big O notation as the auxiliary space complexity is the same in the best and worst case scenarios
    """
    # Create the graph and preference manager
    preference_manager = PreferenceManager(preferences, places)
    return preference_manager.assign()