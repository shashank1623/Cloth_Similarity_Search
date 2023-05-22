import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

# Load preprocessed data from CSV file
df = pd.read_csv('preprocessed_data.csv')

# Get the preprocessed descriptions as a list
preprocessed_descriptions = df['cleaned_description'].tolist()

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed descriptions
tfidf_matrix = vectorizer.fit_transform(preprocessed_descriptions)

# Function to compute similarity between input text and database texts
def compute_similarity(input_text,N):
    # Preprocess the input text
    cleaned_input_text = input_text

    # Transform the input text using the fitted TF-IDF vectorizer
    input_tfidf = vectorizer.transform([cleaned_input_text])

    # Compute cosine similarity between the input text and database texts
    similarity_scores = cosine_similarity(input_tfidf, tfidf_matrix)

    # Get indices of top-N most similar items
    top_indices = similarity_scores.argsort()[0][-N:][::-1]

    # Get URLs of top-N most similar items
    top_urls = df.loc[top_indices, 'url'].tolist()

    return top_urls

# Initialize Flask application
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
# Define the API route for your function
@app.route('/compute_similarity', methods=['POST'])
def compute_similarity_api():
    # Parse the JSON payload
    data = request.get_json()
    input_text = data['input_text']
    N = data['N']

    # Compute similarity and get top-N most similar item URLs
    similar_item_urls = compute_similarity(input_text,N)

    # Create JSON response
    response = {'similar_item_urls': similar_item_urls}

    return jsonify(response)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
