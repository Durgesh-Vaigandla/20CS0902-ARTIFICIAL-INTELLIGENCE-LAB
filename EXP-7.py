import nltk
nltk.download('WordNetLemmatizer')
from nltk.stem import WordNetLemmatizer

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(text)
    lemmatized_text = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_text)

# Example usage
text = "The cats are playing with the mice"
lemmatized_text = lemmatize_text(text)
print(lemmatized_text)
