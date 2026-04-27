from database import get_books, get_price_summary
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/books")
def show_books() -> list:
    
    books = get_books()
    
    return books


@app.get("/summary")
def show_price_summary() -> dict:

    summary = get_price_summary()

    if summary is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No summary data available")

    return summary