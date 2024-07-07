# Health_chatBot

This Health Chatbot is a Python-based application designed to provide users with information and advice on various health-related topics. Built using tkinter for the GUI, this chatbot leverages nltk for natural language processing, spacy for advanced text processing, and TextBlob for sentiment analysis. The chatbot responds to user queries by matching input to a predefined dataset of health topics and provides relevant advice. If you have any health-related questions or need information on topics such as physical development, nutrition, mental health, and more, this chatbot is here to assist.

**Features**
Natural Language Processing: Utilizes nltk and spacy for tokenization, stopword removal, and similarity calculations.
Sentiment Analysis: Uses TextBlob to analyze the sentiment of user inputs and tailor responses accordingly.
Extensive Health Dataset: Contains information on a wide range of health topics including exercise, nutrition, mental wellness, chronic diseases, and more.
User-friendly Interface: Built with tkinter, providing a simple and interactive chat experience.
**Getting Started**
Install Dependencies: Ensure you have the necessary libraries installed (tkinter, nltk, spacy, sklearn, numpy, textblob).
Download NLTK Data: Run the following commands to download required NLTK datasets:


import nltk
nltk.download('punkt')
nltk.download('stopwords')
Load spaCy Model: Download and load the spaCy model using:
bash

python -m spacy download en_core_web_md
Run the Application: Execute the script to launch the chatbot interface.
Usage
Simply type your health-related questions into the chat window and receive informative responses.
The chatbot also provides related topics and advice based on your queries.
**Example Queries**
"What are the benefits of regular exercise?"
"Can you tell me about mental health tips?"
"What should I do if I have a fever?"
