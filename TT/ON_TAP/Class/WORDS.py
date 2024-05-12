class Wordplay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, length):
        return [word for word in self.words if len(word) == length]

    def starts_with(self, s):
        return [word for word in self.words if word.startswith(s)]

    def ends_with(self, s):
        return [word for word in self.words if word.endswith(s)]

    def palindromes(self):
        return [word for word in self.words if word == word[::-1]]

    def only(self, L):
        return [word for word in self.words if set(word).issubset(set(L))]

    def avoids(self, L):
        return [word for word in self.words if not set(word).intersection(set(L))]

# Example usage:
wp = Wordplay(["racecar", "python", "level", "world", "radar", "apple", "cherry", "anaconda", "bob"])
print(wp.words_with_length(5))
print(wp.starts_with('a'))
print(wp.ends_with('n'))
print(wp.palindromes())
print(wp.only(['a', 'b', 'c', 'r', 'e'])) #returns a list of the words that contain only those letters in 
print(wp.avoids(['a', 'b', 'c'])) #giao