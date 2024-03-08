## Named Entity Recognition and Word Analysis

This project is a Streamlit web application for performing Named Entity Recognition (NER) and generating Word Clouds based on user input text or text extracted from a URL.

### Features
- **Named Entity Recognition (NER):** Utilizes spaCy's NLP model to identify named entities in the input text and displays the recognized entities along with their labels.
- **Word Cloud Generation:** Generates a word cloud visualization based on the input text to highlight the most frequent words.
- **URL Text Extraction:** Allows users to input a URL to extract text content from the webpage and analyze it using NER or generate a word cloud.

### Technologies Used
- Python
- Streamlit
- spaCy
- WordCloud
- Matplotlib
- Requests
- BeautifulSoup

### How to Use
1. **Install Dependencies:** Make sure you have Python installed. You can install the required dependencies using pip:
   ```
   pip install streamlit spacy wordcloud matplotlib requests beautifulsoup4
   python -m spacy download en_core_web_sm
   ```
2. **Run the Application:** Execute the `named_entity.py` script to run the Streamlit application:
   ```
   streamlit run named_entity.py
   ```
3. **Use the Application:**
   - Enter text directly into the input field or provide a URL to extract text.
   - Select the type of visualization (NER or Word Cloud) from the sidebar.
   - Click the "Fetch and Convert" button to extract text from the URL (if provided).
   - Click the "Perform Visualization" button to trigger the NER analysis or generate a word cloud.
   
### Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests on [GitHub](https://github.com/Muhammedashfaqullasharif/Techsaksham_project).

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
