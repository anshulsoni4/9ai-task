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
