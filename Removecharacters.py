# Define remove_chars
def remove_characters(word1, n):
    print("Original word", word1)
    removed1 = word1[n:]
    return removed1


# Print Remove first n characters from a string
print("Remove first 'n' characters from a string")
print(remove_characters("pynative", 4))
print(remove_characters("pynative", 2))
