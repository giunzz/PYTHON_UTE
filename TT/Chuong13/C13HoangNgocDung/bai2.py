words = ["hello", "world", "how", "are", "you"]
def add_excitement(words):
    for i in range(len(words)):
        words[i] += "!"
  
add_excitement(words)

def add_exclamation(words):
  
  excited_words = []
  for word in words:
    excited_words.append(word + "!")
  return excited_words

# Example usage:
words = ["hello", "world", "how", "are", "you"]
excited_words = add_exclamation(words)
print(words)  # Output: ['hello', 'world', 'how', 'are', 'you']
print(excited_words)  # Output: ['hello!', 'world!', 'how!', 'are!', 'you!']