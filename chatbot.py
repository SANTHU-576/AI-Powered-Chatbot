import json
import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

patterns = []
responses = []
intent_data = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern.lower())
        responses.append(random.choice(intent["responses"]))
        intent_data.append(intent)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
    return text.strip()


def get_response(user_input):

    user_input = clean_text(user_input)

    # Exact/keyword match
    for intent in intent_data:
        for pattern in intent["patterns"]:
            if clean_text(pattern) == user_input:
                return random.choice(intent["responses"])

    # TF-IDF fallback
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, X)

    index = similarity.argmax()
    score = similarity[0][index]

    if score >= 0.6:
        return responses[index]

    return "Sorry, I couldn't understand that. Can you please rephrase your question?"