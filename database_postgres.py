import os
from dotenv import load_dotenv
import psycopg2
from datetime import datetime

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    return psycopg2.connect(DATABASE_URL)

def create_table() -> None:

    create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY, 
        title VARCHAR(255) NOT NULL,
        price FLOAT,
        rating INTEGER,
        in_stock VARCHAR(15),
        link VARCHAR(500) UNIQUE,
        scraped_at TIMESTAMP
        );
        """
    
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)

def insert_books(books: list) -> None:

    scraped_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    books_tuple = [(book['title'], book['price'], book['rating'], book['in_stock'], book['link'], scraped_at) for book in books]
    
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.executemany(
                    "INSERT INTO books (title, price, rating, in_stock, link, scraped_at) \n"
                    "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (link) DO NOTHING  \n", books_tuple
            )

def get_books() -> list:
    
    books = []
    select_query="""SELECT * FROM books;"""
    
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(select_query)     
            data = cursor.fetchall()
    
    columns = [d[0] for d in cursor.description]

    for row in data:
        books_dict = dict(zip(columns, row))
        books.append(books_dict)

    return books     


def get_average_rating() -> float | None:
     
    query = """SELECT AVG(rating) FROM books;"""

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            avg_values = cursor.fetchone() 
    
    if avg_values and avg_values[0] is not None:
        avg_price = avg_values[0]
    
    return avg_price
    
def get_max_price() -> float | None:
     
    query = """SELECT MAX(price) FROM books;"""

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            max_values = cursor.fetchone()

    if max_values and max_values[0] is not None:
        max_price = max_values[0]
    
    return max_price
          

def get_min_price() -> float | None:
     
    min_price = None
     
    query = """SELECT MIN(price) FROM books;"""

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            min_values = cursor.fetchone()

    if min_values and min_values[0] is not None:
        min_price = min_values[0]
    
    return min_price
    
def get_average_price() -> float | None:
     
    query = """SELECT AVG(price) FROM books;"""

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            avg_values = cursor.fetchone()
    
    if avg_values and avg_values[0] is not None:
        avg_price = avg_values[0]

    return avg_price

def get_price_summary() ->  dict | None:
    
    query = """SELECT MAX(price), MIN(price), AVG(price) FROM books;"""
    
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

    if not row or row[0] is None:
        return None

    return{
        "max_price": round(row[0], 2) if row[0] is not None else None,
        "min_price": round(row[1], 2) if row[1] is not None else None,
        "avg_price": round(row[2], 2) if row[2] is not None else None,
    }