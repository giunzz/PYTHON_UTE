cursed_words = ["darn", "dang", "freakin", "heck", "shoot"]

user_text = input("Enter some text: ")
words = user_text.split()

censored_words = ['*' * len(word) if word.lower() in cursed_words else word for word in words]
censored_text = ' '.join(censored_words)
print(censored_text)
