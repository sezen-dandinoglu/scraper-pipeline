from bs4 import BeautifulSoup
import requests

def fetch_page(url) -> str:

    try:
        response = requests.get(url, timeout=5)
        
        response.raise_for_status()

        return response.text
        
    except requests.exceptions.ConnectionError:
        raise
    except requests.exceptions.Timeout:
        raise
    except requests.exceptions.HTTPError:
        raise
    except requests.exceptions.RequestException:
        raise

def parse_books(html) -> list:

    book_list =[]

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    soup = BeautifulSoup(html, 'html.parser')

    rows = soup.find_all('article', class_='product_pod')
    
    for row in rows:
        
        rating = 0
        h3 = row.find('h3')
        title = h3.find('a').get('title')
        link = h3.find('a').get('href')

        price_text = row.find('p', class_='price_color').text
        price_text = price_text.replace("Â£", "").replace("£", "")
        price = float(price_text)

        in_stock = row.find('p', class_='instock availability').text.strip()

        rating_elements = row.select_one('p[class^="star-rating"]')
        if rating_elements:
            rating_in_text = rating_elements['class'][1]
            rating = rating_map.get(rating_in_text, 0)
        
        product_dict={
            "title": title,
            "price": price,
            "rating": rating,
            "in_stock": in_stock,
            "link": link
        }

        book_list.append(product_dict)
    
    return book_list






