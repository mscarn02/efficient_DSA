import sys
from trie import Trie

def without_trie(strings):

    total_memory = sys.getsizeof(strings)
    for string in strings:
        total_memory += sys.getsizeof(string)

    return total_memory

def with_trie(strings):
    trie = Trie()

    for string in strings:
        trie.insert(string)

    total_memory = sys.getsizeof(trie)
    total_memory += sum(sys.getsizeof(word) for word in trie.getAllWords())

    return total_memory

# Example strings
strings = ["axy", "abxy", "bca", "bxta"]

# Memory usage without compressed Trie
memory_usage_without_trie = without_trie(strings)

# Memory usage with compressed Trie
memory_usage_with_trie = with_trie(strings)

# Comparison
print("Memory usage without compressed Trie:", memory_usage_without_trie, "bytes")
print("Memory usage with compressed Trie:", memory_usage_with_trie, "bytes")
print("Reduction in memory usage by using compressed Trie:", memory_usage_without_trie - memory_usage_with_trie, "bytes")