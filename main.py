from scraper import fetch_page, parse_books
from database import create_table, insert_books, get_books, get_price_summary
from pathlib import Path
import csv



def main() -> None:

    URL='https://books.toscrape.com/'

    create_table()
    html = fetch_page(URL)
    books = parse_books(html)
    insert_books(books)
    
    print(f"{len(books)} books processed.")

    data = get_books()
    export_books_to_csv(data)

    print_summary()
    export_summary_to_csv()

def export_books_to_csv(books):

    if not books:
        print("No books to export!")
        return
    
    file_path = Path(__file__).parent / "books_sample.csv"

    field_names = list(books[0].keys())

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        
        writer = csv.DictWriter(file, fieldnames= field_names)
        writer.writeheader()
        writer.writerows(books)

def print_summary():

    summary = get_price_summary()

    if summary:
        print("\nPrice Summary:")
        print(f"Max Price: £{summary['max_price']}")
        print(f"Min Price: £{summary['min_price']}")
        print(f"Avg Price: £{summary['avg_price']}")
    else:
        print("No data available.")

def export_summary_to_csv():

    summary_list=[]
    file_path = Path(__file__).parent / "summary_sample.csv"

    summary = get_price_summary()
    if not summary:
        print("No summary data to export.")
        return

    for key, value in summary.items():

        summary_list.append({"metric": key, "value": value})
        
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        
        writer = csv.DictWriter(file, fieldnames = ["metric", "value"])
        writer.writeheader()
        writer.writerows(summary_list)

if __name__ == "__main__":
    
    main()