from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Ash",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]


# now we are trying to create a home routes that responds to GET requests at the root URL. 
@app.get("/", response_class=HTMLResponse, include_in_schema=True)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=True)#this is decorator
#function for decorating
def home():
    return f"<h1> {posts[0]['title']}</h1>"


#create a new route here, it is not root route
#instead of rot, it is (/api/posts)
@app.get("/api/posts")
#function for decorating
def get_posts():
    return posts








#in terminal using "uv run" before fastAPI dev is to make things automatically updating, we can use just fastapi run,
# we use pip, not uv