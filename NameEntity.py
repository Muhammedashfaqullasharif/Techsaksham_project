import streamlit as st
import spacy
from spacy import displacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfReader
from docx import Document

# Load spaCy NLP model
nlp = spacy.load('en_core_web_sm')

# Function to perform Named Entity Recognition
def perform_ner(text):
    doc = nlp(text)
    return doc

# Function to generate Word Cloud
def generate_wordcloud(text):
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()

# Function to fetch HTML content from URL and convert to text
def fetch_html_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

# Function to read PDF file
def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to read DOCX file
def read_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

# Function to count words
def count_words(text):
    words = text.split()
    return len(words)

# Streamlit app
def main():
    st.title("Named Entity Recognition and Word Analysis for Analysing Text and Documents")
    st.sidebar.title("Settings")

    # Settings options in the sidebar
    st.sidebar.markdown("<h3 style='text-align: center; font-size: 20px;'>Select Visualization Type:</h3>", unsafe_allow_html=True)
    visualization_type = st.sidebar.radio("", ["Named Entity Recognition (NER)", "Word Cloud (DEP)"])

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload File", type=["pdf", "docx"])

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "pdf":
            text = read_pdf(uploaded_file)
        elif file_extension == "docx":
            text = read_docx(io.BytesIO(uploaded_file.read()))
        else:
            st.sidebar.error("Unsupported file format.")
            return
        st.sidebar.success("File successfully uploaded and processed.")
        word_count = count_words(text)
        st.sidebar.info(f"Word count: {word_count}")

    else:
        text = st.text_area("Enter text:", "Type or paste your text here.")

    # Perform NER and generate Word Cloud when the user clicks the button
    if st.button("Perform Visualization"):
        st.subheader("Visualization Results:")
        if visualization_type == "Named Entity Recognition (NER)":
            # Perform NER
            doc = perform_ner(text)

            # Display recognized entities and labels
            html = displacy.render(doc, style="ent", page=True)
            st.write(html, unsafe_allow_html=True)  # Use write function with unsafe_allow_html=True

        elif visualization_type == "Word Cloud (DEP)":
            # Generate word cloud
            st.subheader("Word Cloud:")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            generate_wordcloud(text)

    # Add "Presented by" and "Guided by" sections with two person names below the settings
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Presented by:")
    st.sidebar.markdown("-M Ashfaqulla Sharif - sk university - ECE")
    st.sidebar.markdown("- S Md Zubair - sk university - ECE")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Guided by:")
    st.sidebar.markdown("- Abdul Aziz Md, Master Trainer, Edunet Foundation.")
   

if __name__ == "__main__":
    main()
