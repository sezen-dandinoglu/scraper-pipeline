# from database_sqlite import get_books, get_price_summary, create_table
from database_postgres import get_books_filtered, get_price_summary, create_table
from fastapi import FastAPI, HTTPException, status, Query
from main import main

app = FastAPI()

@app.on_event("startup")
def startup():
    create_table()
    main()

@app.get("/health")
def health():
    return{"status": "ok"}    

@app.get("/summary")
def show_price_summary() -> dict:

    summary = get_price_summary()

    if summary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No summary data available")

    return summary

@app.get("/books")
def show_books_filtered(
    rating: int | None = None,
    price_min: float | None = None,
    price_max: float | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort: str | None = None
) -> list:
    
    filtered_books = get_books_filtered(rating, price_min, price_max, page, limit, sort)
    
    return filtered_books