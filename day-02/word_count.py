sentence = "apple orange apple banana"
words = sentence.split()

for word in set(words):
    print(word + ":", words.count(word))
