import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources (run this once)
nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def process_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            passage = file.read()
            return passage
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def main():
    file_path = 'EXP4.txt'  # Replace with the path to your text file
    passage = process_text_file(file_path)

    if passage:
        processed_passage = remove_stopwords(passage)
        print("Original Passage:")
        print(passage)
        print("\nPassage after removing stop words:")
        print(processed_passage)

if __name__ == "__main__":
    main()