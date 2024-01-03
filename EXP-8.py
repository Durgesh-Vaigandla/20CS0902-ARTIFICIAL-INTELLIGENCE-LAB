# Import the necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Define the sentence to be classified
sentence = "This is an example sentence for text classification."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Lemmatize the tokens
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

# Convert the tokens to a string
processed_sentence = " ".join(lemmatized_tokens)

# Define the training data
training_data = [
    ("This is a positive sentence.", "positive"),
    ("This is a negative sentence.", "negative"),
    ("This is a neutral sentence.", "neutral")
]

# Extract the features from the training data
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform([data[0] for data in training_data])
y_train = [data[1] for data in training_data]

# Train the classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Classify the sentence
X_test = vectorizer.transform([processed_sentence])
predicted_class = classifier.predict(X_test)[0]

# Print the predicted class
print("Predicted class:", predicted_class)
