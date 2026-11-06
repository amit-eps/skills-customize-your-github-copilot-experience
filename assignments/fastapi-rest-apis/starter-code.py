from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookInput(BaseModel):
    title: str
    author: str


books = {
    1: Book(id=1, title="The Hobbit", author="J.R.R. Tolkien"),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle"),
}


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return list(books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Return the book with this ID, or raise HTTP 404 if it is missing.
    pass


@app.post(
    "/books",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book_input: BookInput) -> Book:
    # TODO: Assign an unused ID, store the new book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    # TODO: Update the matching book, or raise HTTP 404 if it is missing.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    # TODO: Delete the matching book, or raise HTTP 404 if it is missing.
    pass