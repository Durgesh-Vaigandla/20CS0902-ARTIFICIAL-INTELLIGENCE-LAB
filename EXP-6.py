import nltk

# Download NLTK resources (run this once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(sentence):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Perform POS tagging
    pos_tags = nltk.pos_tag(words)

    return pos_tags

# Example sentence
input_sentence = "NLTK provides tools for natural language processing."

# Perform POS tagging
pos_tags_result = pos_tagging(input_sentence)

# Display results
print("Original Sentence:")
print(input_sentence)
print("\nPOS Tagging Result:")
print(pos_tags_result)