Project Description:
=====================

Amazon Product Search API using Flask and BeautifulSoup
------------------------------------------------------

This is a Python-based web application that utilizes Flask and BeautifulSoup to create an API that performs product searches on Amazon. The API allows users to send a search query (keyword) as a JSON payload, and in response, it fetches product details such as title, price, description, image URL, availability, average rating, and the number of reviews related to the search query. The application interacts with the Amazon website (www.amazon.in) to extract the desired information from the search results.

Features:
---------

- **Amazon Product Search**: Users can perform a product search by providing a keyword through the API.

- **Data Retrieval**: The application fetches relevant product details including title, price, description, image URL, availability, average rating, and the number of reviews from the search results.

- **Flask Web Framework**: The API is built using Flask, a lightweight web framework that allows easy handling of HTTP requests and responses.

- **Web Scraping with BeautifulSoup**: BeautifulSoup is used to parse the HTML content of the Amazon search results and extract the necessary product details.

- **Amazon Product Advertising API (Optional)**: If required, users can integrate their own Amazon Product Advertising API credentials to access product data legally and efficiently.

Instructions for Use:
---------------------

1. Install the required libraries by running the following command:

   ```
   pip install Flask requests beautifulsoup4
   ```

2. Run the Flask application by executing the `main.py` file:

   ```
   python main.py
   ```

3. The Flask API will be accessible at `http://localhost:5000/api/search`.

4. To search for a product, make a POST request to the API with a JSON payload containing the keyword:

   ```
   POST http://localhost:5000/api/search
   {
       "keyword": "your_search_query"
   }
   ```

   Replace `"your_search_query"` with the desired product keyword.

5. The API will respond with a JSON containing the product details related to the search query.


This project allows users to easily access Amazon product details through a simple API, making it useful for various applications, including price comparison, product research, and data analysis.
