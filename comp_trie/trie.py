class Node:
    # Define a class representing a node in the Trie
    def __init__(self, data=None):
        # Constructor method for Node class
        self.data = data  # Store a character at the node
        self.children = {}  # Dictionary to store child nodes
        self.leaf = False  # Flag indicating if this node represents the end of a word
    
class Trie:
    # Define a class representing a Trie data structure
    def __init__(self):
        # Constructor method for Trie class
        self.root = Node()  # Initialize the root node of the Trie
        self.count = 0  # Counter to keep track of the number of words in the Trie
                
    def insert(self, word):
        # Method to insert a word into the Trie
        curr = self.root  # Start from the root node
        for letter in word:
            # Traverse through each character of the word
            if letter not in curr.children:
                # If the character is not present in the current node's children
                curr.children[letter] = Node()  # Create a new node for the character
            curr = curr.children[letter]  # Move to the child node
        curr.leaf = True  # Mark the last node as the end of a word
        self.count += 1  # Increment the word count
        print(f"Inserted '{word}' into Trie.")  # Print a message indicating the insertion
    
    def getAllWords(self):
        # Method to retrieve all words stored in the Trie
        allWords = []  # List to store all words
        self.getAllWordsFromSubtree(self.root, "", allWords)  # Recursively get all words
        return allWords
    
    def getAllWordsFromSubtree(self, node, prefix, allWords):
        # Helper method to recursively get all words from a subtree
        if node.leaf:
            # If the current node represents the end of a word
            allWords.append(prefix)  # Add the word formed so far to the list
        for letter, child in node.children.items():
            # Traverse through each child node
            self.getAllWordsFromSubtree(child, prefix + letter, allWords)  # Recursively get words
    
    def getAllPrefixes(self, prefix):
        # Method to retrieve all words with a given prefix
        node = self.root  # Start from the root node
        for letter in prefix:
            # Traverse through each character of the prefix
            if letter not in node.children:
                # If any character is not present in the Trie, return an empty list
                return []
            node = node.children[letter]  # Move to the child node
        allWords = []  # List to store words with the given prefix
        self.getAllWordsFromSubtree(node, prefix, allWords)  # Recursively get words with prefix
        return allWords
    
    def search(self, word):
        # Method to search for a word in the Trie
        node = self.root  # Start from the root node
        for letter in word:
            # Traverse through each character of the word
            if letter not in node.children:
                # If any character is not present in the Trie, return False
                return False
            node = node.children[letter]  # Move to the child node
        return node.leaf  # Return True if the last node represents the end of a word, False otherwise
    
    def delete(self, word):
        # Method to delete a word from the Trie
        if not self.search(word):
            # If the word is not present in the Trie, return False
            return False
        self._delete(self.root, word, 0)  # Call the helper method to perform deletion
        self.count -= 1  # Decrement the word count
        print(f"Deleted '{word}' from Trie.")  # Print a message indicating the deletion
        return True
    
    def _delete(self, node, word, index):
        # Helper method to perform deletion recursively
        if index == len(word):
            # If all characters of the word have been processed
            node.leaf = False  # Mark the current node as not representing the end of a word
            return len(node.children) == 0  # Return True if the current node has no children, False otherwise
        char = word[index]  # Get the character at the current index
        child = node.children[char]  # Get the child node corresponding to the character
        should_delete = self._delete(child, word, index + 1)  # Recursively delete from child node
        if should_delete:
            # If the child node should be deleted
            del node.children[char]  # Delete the child node
            return len(node.children) == 0  # Return True if the current node has no children, False otherwise
        return False  # Return False if the current node should not be deleted

def main():
    # Main function to demonstrate usage of Trie class
    trie = Trie()  # Create a Trie object
    
    # Insert words into the Trie
    words = ["axy", "abxy", "bca", "bxta"]
    for word in words:
        trie.insert(word)
    
    # Print all words in the Trie
    print("\nAll words in Trie:")
    print(trie.getAllWords())
    
    # Print all words with prefix 'b'
    print("\nAll words with prefix 'b':")
    print(trie.getAllPrefixes("b"))
    
    # Search for a word in the Trie
    word_to_search = "abxy"
    print(f"\nSearching for '{word_to_search}':")
    print(trie.search(word_to_search))
    
    # Delete a word from the Trie
    word_to_delete = "axy"
    print(f"\nDeleting '{word_to_delete}':")
    trie.delete(word_to_delete)
    
    # Print all words in the Trie after deletion
    print("\nAll words in Trie after deletion:")
    print(trie.getAllWords())

if __name__ == "__main__":
    main()
