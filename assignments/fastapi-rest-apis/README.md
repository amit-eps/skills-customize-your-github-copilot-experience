# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build a REST API for a small book catalog using FastAPI and Pydantic. Practice defining routes, validating request data, and returning appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the Book API

#### Description
Use the provided starter code to explore the FastAPI app, then complete the endpoint for retrieving one book by its ID.

#### Requirements
Completed program should:

- From the assignment folder, install dependencies with `pip install -r requirements.txt` and start the API with `uvicorn starter-code:app --reload`.
- Return all books from `GET /books` and return one matching book from `GET /books/{book_id}`.
- Return HTTP 404 when a requested book ID does not exist.
- Show the available endpoints in the interactive API documentation at `/docs`.

### 🛠️ Add Book Management Endpoints

#### Description
Add endpoints that let API clients create, update, and delete books in the in-memory catalog.

#### Requirements
Completed program should:

- Accept a book title and author with `POST /books`, assign the new book a unique ID, and return it with HTTP 201.
- Update the title and author of an existing book with `PUT /books/{book_id}` and return HTTP 404 if the ID does not exist.
- Delete an existing book with `DELETE /books/{book_id}` and return HTTP 204; return HTTP 404 if the ID does not exist.
- Keep changes in memory while the server is running; a database is not required.