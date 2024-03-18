text = input("Enter some text:")
text = text.lower()
words = text.split()
num_articles = 0
num_articles = sum([1 for i in words if i =="a" or i == "an" or i =="the" ])
print(num_articles)