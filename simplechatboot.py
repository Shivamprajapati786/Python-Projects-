import nltk
import string

# Optional: Download NLTK data if preprocessing is used
# nltk.download('punkt')

def preprocess(text):
    """Lowercase, remove punctuation, tokenize."""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    return tokens

def chatbot():
    print("🤖 Hello! I'm your Tamizhan Skills assistant. Ask me anything about our courses.\n(Type 'bye' to exit)\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! 😊 Have a great day.")
            break

        # Preprocess input
        tokens = preprocess(user_input)
        
        # Define rule-based responses
        if "course" in tokens or "courses" in tokens:
            print("Bot: We offer courses in Python, Web Development, AI, and more!")
        elif "python" in tokens:
            print("Bot: Our Python course covers basics to advanced topics with hands-on projects.")
        elif "fees" in tokens or "cost" in tokens or "price" in tokens:
            print("Bot: Most courses range between ₹999 to ₹4999. Visit our website for details.")
        elif "certificate" in tokens or "certification" in tokens:
            print("Bot: Yes! You get a certificate upon successful course completion.")
        elif "duration" in tokens:
            print("Bot: Most courses last 4 to 12 weeks, depending on the topic.")
        elif "contact" in tokens or "support" in tokens:
            print("Bot: You can contact us at support@tamizhanskills.in")
        else:
            print("Bot: I'm sorry, I didn't understand that. Can you rephrase or ask about courses, fees, or duration?")

# Run the chatbot
chatbot()
 