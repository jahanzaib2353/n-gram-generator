import streamlit as st
import nltk
from nltk.util import ngrams
from bs4 import BeautifulSoup

nltk.download('punkt')  

def generate_ngrams(text, n=2):
    # Clean and tokenize the text
    soup = BeautifulSoup(text, 'html.parser')
    text = nltk.word_tokenize(soup.get_text())

    # Generate n-grams
    ngrams_list = list(ngrams(text, n))

    # Convert n-grams to a string
    ngrams_string = "\n".join([" ".join(ngram) for ngram in ngrams_list])

    return ngrams_string

# Streamlit app
def main():
    st.title("N-Gram Generator")

    # Input text from user
    user_text = st.text_area("Enter text:", "")

    # Select n for n-grams
    n_value = st.slider("Select n for n-grams:", 2, 5, 2)

    if st.button("Generate N-Grams"):
        # Perform n-gram generation when the user clicks the "Generate N-Grams" button
        result = generate_ngrams(user_text, n_value)
        st.text(result)

if __name__ == "__main__":
    main()
