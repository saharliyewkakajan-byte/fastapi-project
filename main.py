from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from graph import get_connection
import os
import uvicorn


app = FastAPI()

# Şu ýoly üýtget
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/")
def home(request: Request):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM hereketler ORDER BY id DESC")
    hereketler = cur.fetchall()

    cur.execute("SELECT SUM(Cykdayjy) FROM hereketler")
    jemi = cur.fetchone()[0] or 0

    cur.execute("SELECT SUM(Girdeyjy) FROM girdeyjy")
    girdeyjy_jemi = cur.fetchone()[0] or 0

    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "hereketler": hereketler,
            "jemi": jemi,
            "girdeyjy_jemi": girdeyjy_jemi,
            "galyndy": jemi - girdeyjy_jemi,
            "name": "Kakajan"
        }
    )

@app.post("/add_hereket")
def add_hereket(request: Request, sebap: str = Form(), cykdayjy: int = Form()):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO hereketler (Sebap, Cykdayjy) VALUES (%s, %s)",
        (sebap, cykdayjy)
    )
    conn.commit()
    conn.close()
    return RedirectResponse("/", status_code=303)




@app.post("/add_income")
def add_income(request: Request, girdeyjy: int = Form()):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO girdeyjy (Girdeyjy) VALUES (%s)",
        (girdeyjy,)
    )
    conn.commit()
    conn.close()
    return RedirectResponse("/", status_code=303)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# "Log in we FastAPI ulanyjy login sahypasyny gormek we login etmek"

# from fastapi import FastAPI, Form, HTTPException, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
# import uvicorn

# app = FastAPI()

# @app.get("/login", tags=["Ulanyjy"], summary="Ulanyjy login", response_class=HTMLResponse)
# def login():
#     return """
#     <html>
#         <head>
#             <title>Login</title>
#         </head>
#         <body>
#             <h1>Login</h1>
#             <form action="/login" method="post">
#             <input type="text" name="username" placeholder="Username"><br><br>
#             <input type="password" name="password" placeholder="Password"><br><br>
#             <input type="submit" value="Login">
#             </form>
#         </body>
#     </html>
 
#             """

# @app.post("/login", response_class=HTMLResponse)
# def login_post(username: str=Form(), password: str=Form()):
#     if username == "admin" and password == "123":
#         return """
#         <h1>Welcome, admin!</h1>
#        """
#     else:
#         return """
#         <h1>Login failed!</h1>
#         """

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)



# "Log in we FastAPI ulanyjy login sahypasyny gormek we login etmek"




    # books = [
#     {
#         "id": 1,
#         "name": "Python",
#         "author": "Kakajan"

#     },
#     {
#         "id": 2,
#         "name": "Java",
#         "author": "Kakajan"
#     }
# ]

# @app.get(path="/", summary="Gosmaca", tags=["Bas sahypa"])
# def root():
#     return "Hello, Kakajan!!!"


# @app.get("/books",tags=["Kitaplar"],summary="Hemme kitaplary gormek")
# def get_books():
#     return books


# @app.get("/books/{book_id}",tags=["Kitaplar"],summary="Gerekli kitap almak")
# def get_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             return book
    # raise HTTPException(status_code=404, detail="Kitap tapylmady!")