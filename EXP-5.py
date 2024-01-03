import nltk
from nltk.stem import PorterStemmer

# Download NLTK resources (run this once)
nltk.download('punkt')

def stemming(sentence):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()

    # Apply stemming to each word
    stemmed_words = [porter_stemmer.stem(word) for word in words]

    # Join the stemmed words to form the stemmed sentence
    stemmed_sentence = ' '.join(stemmed_words)

    return stemmed_sentence

# Example sentence
input_sentence = "Stemming is an important technique for natural language processing."

# Perform stemming
output_sentence = stemming(input_sentence)

# Display results
print("Original Sentence:")
print(input_sentence)
print("\nStemmed Sentence:")
print(output_sentence)
