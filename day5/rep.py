from collections import Counter
sentence = "apple banana orange apple" 
count = Counter(sentence.split()) 
for word in count:
    print(word, ":", count[word]) 