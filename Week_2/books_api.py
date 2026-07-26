from fastapi import APIRouter
from database import setup_database

router=APIRouter()


@router.get("/")
def home():
    return "Welcome to Prijal's Bookstore!!!"

@router.get("/books")
def get_all_books():
    conn=setup_database()
    cursor= conn.cursor()

    cursor.execute(""" SELECT * FROM books""")

    books= cursor.fetchall()
    conn.close()
    return [dict(book) for book in books]



@router.post("/books/add_new")
def add_new_books(title:str, availability:bool):
    conn=setup_database()
    cursor=conn.cursor()

    cursor.execute(
        """
        SELECT * FROM books
        WHERE title = ?
        """,
        (title,)
    )
    existing_book=cursor.fetchone()

    if existing_book:
        conn.close()
        return {"Message": "Book already exists"}


    cursor.execute(""" INSERT INTO books(title, availability)
                                   VALUES (?, ?)
    """, (title, availability))

    conn.commit()
    conn.close()

    return {"Message": "Added new books"}


@router.put("/books/replace/{id}")
def replace_book(id:int, title:str, availability:bool):
    conn=setup_database()
    cursor=conn.cursor()

    cursor.execute("""UPDATE books
                      SET title=? , availability=?
                       WHERE id=? """, (title, availability, id))
    conn.commit()
    conn.close()

    return {"Message": "Replaced new book"}

@router.delete("/books/delete/{id}")
def remove_specific_book(id:int):
    conn=setup_database()
    cursor= conn.cursor()

    cursor.execute("""DELETE FROM books where id =? """, (id, ))
    conn.commit()

    if cursor.rowcount == 0:
     conn.close()
     return {"message": f"Book with id {id} not found"}

    conn.close()

    return {"message": f"Successfully deleted book of id: {id}"}
    


@router.delete("/books/deleteall")
def remove_all_books():
    conn=setup_database()
    cursor= conn.cursor()

    cursor.execute(""" DELETE FROM books""")
    conn.commit()
    conn.close()

    return {"Message": "All books are deleted"}

