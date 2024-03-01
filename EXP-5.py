from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonder","Programmer","Programing","Programed","Programder"]
for w in example_words:
    print(w + " : " +ps.stem(w))
