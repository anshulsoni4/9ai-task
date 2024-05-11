To run this code, you'll need to have FastAPI, Pydantic, and pymongo installed. You can install them using pip:

css
Copy code
pip install fastapi[all] pymongo
Make sure you have MongoDB running on your local machine.

Then, you can run the FastAPI server using uvicorn:

css
Copy code
uvicorn main:app --reload
This will start the server, and you can access the API documentation at http://localhost:8000/docs.
----------------

# Blog Platform RESTful API

This is a simple RESTful API built using Python's FastAPI framework for a blogging platform. It allows users to create, read, update, and delete blog posts, comment on posts, and like/dislike them. Data is stored in a MongoDB database.

## Setup Instructions

1. Clone this repository:

    ```
    git clone <repository-url>
    ```

2. Install dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

3. Make sure MongoDB is running on your local machine.

4. Run the FastAPI server using uvicorn:

    ```
    uvicorn main:app --reload
    ```

5. Access the API documentation at http://localhost:8000/docs.

## API Usage

### Endpoints

- `POST /posts/`: Create a new blog post.
- `GET /posts/{post_id}`: Retrieve a specific blog post by ID.
- `PUT /posts/{post_id}`: Update an existing blog post.
- `DELETE /posts/{post_id}`: Delete a blog post.
- `POST /posts/{post_id}/comments/`: Add a comment to a blog post.
- `POST /posts/{post_id}/like/`: Like or dislike a blog post.

### Data Models

#### Post

```json
{
  "title": "string",
  "content": "string"
}
