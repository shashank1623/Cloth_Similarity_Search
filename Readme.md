# Clothing Item Similarity

This project aims to find similar clothing items based on their descriptions using machine learning techniques. It collects and preprocesses data, measures similarity, and returns ranked results.

## Problem Statement

The problem is to develop a system that can find similar clothing items based on their descriptions. The system should collect data from multiple e-commerce websites, preprocess the text data, extract useful features, compute similarity between the input text and the database, and return a ranked list of similar item URLs.

## Solution

The solution involves the following steps:

1. **Collect and preprocess data:**
   - Web scrape multiple e-commercelike amazon , flipkart and nykaa fashion websites to gather clothing(Mens : Shirts,T-shirts , jeans  Womens : One Piece , Tops) item descriptions and their corresponding URLs.
   - To keep the datasets balance we have gathered equal amaount of entries from the above stated e-commerce websites.
   - Preprocess the text data by cleaning it, removing special characters, lowercasing, etc., and apply text normalization techniques like stemming or lemmatization.

2. **Measure similarity:**
   - Extracted useful features from the text descriptions using techniques like TF-IDF .
   - Implement a method to compute the similarity between the input text and the texts in the database using cosine similarity.

3. **Return ranked results:**
   - Designed a function that accepts a text string, extracts its features, computes similarities with the items in the database, ranks them based on similarity, and returns the URLs of the top-N most similar items.
4. **Deploy the function:**
   - Containerize the application using Docker.
   - Deploy the function on AWS EC2 (Although GCP was recommened due to technical isssues i was not able to access my free trail account but in future we will deploy of function to GCP Function).
   - The function is accepting a JSON payload with the input text and return a JSON response with the ranked list of similar item URLs.


video_link : https://youtu.be/EUFEDruCOvM

I usally love feebacks and suggestion 
Contact Us:- shashankbhardwaj2030@gmai.com (Hope this repo found it usefull to you then please give a star to this repo).

If you want to contribute to this project feel free to contact me or just genrate a issue .
Note : There is a lot of potential in this project in future we will adding more data and other properties to suggest more accurately .

Thanks
❤️❤️❤️ shashank Bhardwaj(the_ghost) ❤️❤️❤️❤️
