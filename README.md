# Movie Title Scraper & Recommender

The "Movie Title Scraper & Recommender" project is a Python-based web scraping and recommendation system designed to gather movie titles from Rotten Tomatoes and provide recommendations based on movie genres.

## Components:

### 1. Web Scraper (Scrapy Spider):
- Utilizes Scrapy, a powerful web crawling and scraping framework, to extract movie titles from the Rotten Tomatoes website.
- Collects movie titles from multiple pages, processes the extracted data, and stores it in a CSV file for further analysis.

### 2. Data Processing and Analysis:
- Utilizes pandas for data manipulation and cleaning.
- Processes extracted movie titles to remove whitespace and any special characters for consistency.
- Stores the cleaned data in a structured format, ready for analysis.

### 3. Recommendation System:
- Implements a content-based recommendation system based on movie genres.
- Computes cosine similarity between movie genres to identify similar movies.
- Allows users to input a movie title and receive recommendations for similar movies based on genre similarities.

The "Movie Title Scraper & Recommender" project provides a comprehensive solution for gathering movie data, processing it, and offering personalized movie recommendations based on genre preferences. It provides opportunities for further enhancements such as user interface development, additional data sources, and integration with external movie databases.
