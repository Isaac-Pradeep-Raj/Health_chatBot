import tkinter as tk
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tkinter import scrolledtext, ttk, messagebox
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from textblob import TextBlob
# Copyright (c) 2024 Isaac Pradeep Raj

# Download NLTK data
nltk.download('punkt')            #these functions return a boolean values
nltk.download('stopwords')

# Initializing stopwords
stop_words = set(stopwords.words('english'))

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Mock machine learning model for response generation
class HealthChatbotModel:
    def __init__(self):
        # data set
        self.data = {
            "hello": "Hello! How can I assist you with your health today?",
            "physical development": "Physical development involves activities that improve your body's health and fitness. Examples include exercise, proper nutrition, and adequate sleep.",
            "mental development": "Mental development involves cognitive exercises that enhance your intellectual capabilities. Reading, puzzles, and learning new skills are good practices.",
            "emotional development": "Emotional development focuses on understanding and managing your emotions. Practices include mindfulness, therapy, and healthy relationships.",
            "spiritual development": "Spiritual development is about finding purpose and meaning in life. This can be through religion, meditation, or personal reflection.",
            "social development": "Social development involves improving your interpersonal skills. Activities include socializing, teamwork, and community involvement.",
            "exercise benefits": "Regular exercise helps improve cardiovascular health, strengthens muscles, boosts mental health, and enhances overall well-being.",
            "nutrition importance": "Proper nutrition is essential for maintaining good health, providing energy, and supporting bodily functions.",
            "sleep benefits": "Adequate sleep is crucial for physical and mental health, aiding in recovery, memory consolidation, and mood regulation.",
            "hydration": "Staying hydrated is essential for maintaining bodily functions, regulating temperature, and supporting digestion. Aim to drink at least 8 glasses of water a day.",
            "stress management": "Stress management techniques include mindfulness, meditation, deep breathing exercises, and engaging in hobbies or physical activities.",
            "mental health tips": "Some tips for maintaining good mental health include regular physical activity, a balanced diet, adequate sleep, socializing with friends and family, and seeking professional help when needed.",
            "chronic diseases": "Chronic diseases such as diabetes, hypertension, and heart disease can often be managed through a combination of medication, lifestyle changes, and regular medical check-ups.",
            "healthy eating": "Healthy eating involves consuming a variety of foods, including fruits, vegetables, whole grains, lean proteins, and dairy, while limiting sugars, salt, and unhealthy fats.",
            "immunization": "Immunization is a vital part of preventive healthcare. Vaccines protect against various infectious diseases, reducing their spread and severity.",
            "mental wellness": "Mental wellness involves maintaining emotional, psychological, and social well-being. It includes managing stress, building resilience, and seeking support when needed.",
            "screening tests": "Regular screening tests can help detect diseases early. Common tests include blood pressure, cholesterol levels, mammograms, and colonoscopies, depending on age and risk factors.",
            "smoking cessation": "Quitting smoking can significantly reduce the risk of heart disease, cancer, and respiratory illnesses. Consider seeking support from healthcare providers, support groups, or smoking cessation programs.",
            "physical activity": "Engaging in at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity activity per week is recommended for adults.",
            "hydration importance": "Staying hydrated is vital for maintaining bodily functions, including temperature regulation, joint lubrication, and nutrient transportation.",
            "benefits of yoga": "Yoga improves flexibility, muscle strength, and mental clarity. It also helps with stress management and overall well-being.",
            "importance of regular check-ups": "Regular check-ups can help detect health issues early, monitor existing conditions, and maintain overall health.",
            "healthy diet": "A healthy diet includes a variety of fruits, vegetables, whole grains, and lean proteins. It's important to limit processed foods and sugars.",
            "heart health tips": "To maintain heart health, engage in regular physical activity, eat a balanced diet, avoid smoking, and manage stress effectively.",
            "immune system boosting": "Boost your immune system with a balanced diet, regular exercise, adequate sleep, and proper hygiene practices.",
            "fitness routines": "Consistency is key. Create a balanced routine that includes cardiovascular exercise, strength training, and flexibility exercises.",
            "mindfulness": "Mindfulness involves paying full attention to what’s happening in the present moment. Techniques include meditation, deep breathing, and mindful movement like yoga.",
            "healthy relationships": "Healthy relationships are built on trust, respect, and communication. It’s important to listen actively, express yourself clearly, and support each other.",
            "anxiety management": "To manage anxiety, practice relaxation techniques, stay physically active, maintain a healthy lifestyle, and seek professional help if necessary.",
            "depression support": "If you or someone you know is struggling with depression, it's important to seek professional help. Talking to a therapist and reaching out to supportive friends and family can also make a big difference.",
            "mental health resources": "There are many resources available for mental health support, including therapists, support groups, hotlines, and online communities.",
            "dietary supplements": "Dietary supplements can provide additional nutrients that may be lacking in your diet, but it's important to consult with a healthcare provider before starting any new supplement.",
            "weight management": "Maintaining a healthy weight involves a balance of regular physical activity and a healthy diet. Avoid fad diets and aim for gradual, sustainable weight loss.",
            "healthy aging": "Healthy aging involves staying physically active, eating a nutritious diet, staying socially connected, and keeping the mind engaged through lifelong learning and hobbies.",
            "children's health": "Children's health includes ensuring proper nutrition, regular physical activity, adequate sleep, immunizations, and routine check-ups.",
            "women's health": "Women's health encompasses reproductive health, breast health, bone health, and overall well-being. Regular screenings and a healthy lifestyle are key.",
            "men's health": "Men's health includes prostate health, heart health, mental health, and maintaining a healthy lifestyle. Regular check-ups and screenings are important.",
            "sexual health": "Sexual health involves safe sexual practices, regular screenings for sexually transmitted infections (STIs), and open communication with partners.",
            "sleep disorders": "Sleep disorders such as insomnia, sleep apnea, and restless legs syndrome can affect overall health. Consult a healthcare provider for diagnosis and treatment options.",
            "bone health": "Bone health is crucial for preventing conditions like osteoporosis. Ensure adequate intake of calcium and vitamin D, and engage in weight-bearing exercises.",
            "skin health": "Skin health can be maintained by protecting against UV rays, staying hydrated, eating a healthy diet, and using appropriate skincare products.",
            "eye health": "Eye health can be maintained through regular eye exams, protecting eyes from UV light, and consuming a diet rich in fruits and vegetables.",
            "hearing health": "Protect hearing by avoiding prolonged exposure to loud noises, using ear protection, and getting regular hearing check-ups.",
            "digestive health": "Digestive health can be supported through a diet high in fiber, staying hydrated, and regular physical activity. Probiotics may also help.",
            "allergies": "Allergies can be managed by avoiding known allergens, taking prescribed medications, and consulting an allergist for treatment options.",
            "respiratory health": "Maintain respiratory health by avoiding smoking, staying active, and reducing exposure to pollutants and allergens.",
            "flu prevention": "Prevent the flu by getting an annual flu vaccine, practicing good hand hygiene, and avoiding close contact with sick individuals.",
            "covid-19": "COVID-19 prevention includes getting vaccinated, wearing masks in crowded places, practicing good hand hygiene, and maintaining social distancing when necessary.",
            "mental resilience": "Build mental resilience through positive thinking, stress management techniques, maintaining a support network, and seeking professional help when needed.",
            "first aid basics": "Basic first aid includes knowing how to treat cuts, burns, sprains, and performing CPR. Consider taking a certified first aid course.",
            "fever": "Fever is often a sign of the body fighting an infection. It's important to rest, stay hydrated, and monitor your temperature. If it persists or is accompanied by severe symptoms, seek medical attention."
            # Copyright (c) 2024 Isaac Pradeep Raj

        }

        self.questions = list(self.data.keys())
        self.answers = list(self.data.values())
        self.question_vectors = [nlp(question).vector for question in self.questions]

    def get_response(self, user_input):
        # Tokenize and preprocess the user input
        user_vector = nlp(user_input).vector
        similarities = cosine_similarity([user_vector], self.question_vectors)
        best_match_idx = np.argmax(similarities)
        best_match_score = similarities[0][best_match_idx]

        # Thresholds for determining response relevance
        high_threshold = 0.5
        low_threshold = 0.3
        # Copyright (c) 2024 Isaac Pradeep Raj


        if best_match_score > high_threshold:
            return self.answers[best_match_idx]
        elif best_match_score > low_threshold:
            # Get related topics based on keywords in the user input
            related_topics = self.get_related_topics(user_input)
            return "I don't have specific information on that, but here is something related: " + related_topics
        else:
            return "I'm sorry, I don't have information on that right now."

    def get_related_topics(self, user_input):
        # Tokenize user input
        tokens = word_tokenize(user_input.lower())
        # Filter out stop words
        filtered_tokens = [word for word in tokens if word not in stop_words]

        # Find related topics in the dataset
        related_responses = []
        for token in filtered_tokens:
            for question, answer in self.data.items():
                if token in question:
                    # Copyright (c) 2024 Isaac Pradeep Raj

                    related_responses.append(answer)
        
        # Return the top 3 related responses or a default message if none are found
        if related_responses:
            return " ".join(related_responses[:3])
        else:
            return "I don't have additional related information."

# Tkinter GUI application
class HealthChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Chatbot")
        # Copyright (c) 2024 Isaac Pradeep Raj

        self.chat_history = scrolledtext.ScrolledText(root, width=50, height=20)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_label = ttk.Label(root, text="User Input:")
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.user_input = ttk.Entry(root, width=40)
        self.user_input.grid(row=1, column=1, padx=10, pady=10)

        self.send_button = ttk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Initialize the machine learning model
        self.model = HealthChatbotModel()

        self.chat_history.tag_config('user', foreground='#040D12')
        self.chat_history.tag_config('bot', foreground='#2155CD')

    def send_message(self):
        user_text = self.user_input.get().strip()
        if user_text:
            self.chat_history.insert(tk.END, f"You: {user_text}\n", 'user')

            # Call the machine learning model to get response
            response = self.get_response(user_text)

            # Analyze the sentiment of the user's input
            sentiment = TextBlob(user_text).sentiment
            if sentiment.polarity < 0:
                response = "It seems like you're feeling down. " + response
            elif sentiment.polarity > 0:
                response = "I'm glad to hear that! " + response

            self.chat_history.insert(tk.END, f"Health Bot: {response}\n", 'bot')
            self.user_input.delete(0, tk.END)
            self.chat_history.see(tk.END)

    def get_response(self, user_input):
        return self.model.get_response(user_input)

if __name__ == "__main__":
    # Copyright (c) 2024 Isaac Pradeep Raj

    root = tk.Tk()
    app = HealthChatbotApp(root)
    root.mainloop()
