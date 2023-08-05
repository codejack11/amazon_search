import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

def search_amazon(keyword):
    url = 'https://www.amazon.in/s?k={}'.format(keyword)
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.in/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    response = requests.get(url, headers=headers)
    results = dict()
    if response.status_code == 200:
        try:
            results[keyword] = []
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('div', {'data-component-type': 's-search-result'})

            if not products:
                print("No products found.")
                return

            for product in products:
                title = product.find('span', {'class': 'a-text-normal'}).text.strip()
                price_element = product.find('span', {'class': 'a-offscreen'})
                price = price_element.text.strip() if price_element else 'N/A'

                description = product.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'})
                description = description.text.strip() if description else 'N/A'
                image_element = product.find('img', {'class': 's-image'})
                image_url = image_element['src'] if image_element else 'N/A'

                availability = product.find('span', {'class': 'a-size-medium a-color-success'})
                availability = availability.text.strip() if availability else 'N/A'
                rating_element = product.find('span', {'class': 'a-icon-alt'})
                rating = re.search(r'\d.\d', rating_element.text.strip()).group() if rating_element else 'N/A'
                reviews_element = product.find('span', {'class': 'a-size-base'})
                reviews = re.search(r'\d+', reviews_element.text.strip()).group() if reviews_element else 'N/A'



                results[keyword].append({"Product": title, "Price": price, "Description": description, "Image": image_url, "Availability": availability, "Rating": rating, "Reviews": reviews})

        except requests.exceptions.RequestException as e:
            print("Error accessing Amazon. Please check your internet connection or try again later.")
            print(f"Error message: {e}")
        finally:
            return results
    else:
        print('Error fetching data from Amazon')

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    if not data or 'keyword' not in data:
        return jsonify({"error": "Invalid payload. Please provide a 'keyword'."}), 400

    keyword = data['keyword']
    result = search_amazon(keyword)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

