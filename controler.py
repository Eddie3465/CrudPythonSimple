import sqlite3 as sql

def crearDB():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def crearTabla():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers(
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()

"""

def insertarRow(nombre,followers,subs): #inserta una fila
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()

    instruccion = f"INSERT INTO streamers VALUES('{nombre}',{followers},{subs})"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()"""

##
def insertarRows(): #inserta varias fila


    nom = input("ingrese nombre: ")
    foll = int(input("ingrese cantidad de followers: "))
    subs = int(input("ingrese cantidad de subs: "))

    try:
        conn = sql.connect("streamers.db")
        cursor = conn.cursor()


        cursor.execute('''INSERT  INTO streamers (name,followers,subs) VALUES ('%s','%s','%s')'''%(nom,foll,subs))
        print("Fila agregada con exito")
        conn.commit()
        conn.close()
    except:
        print("error")
def leerRows():


    conn = sql.connect("streamers.db")
    cursor = conn.cursor()

    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()

    conn.commit()
    conn.close()

    print(datos)



"""
def eliminarRow(): #elimina una fila
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()

    instruccion = f"DELETE FROM streamers WHERE name = 'marcelo'"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()
"""

def eliminarRows():  # elimina varias fila

    nom = input("ingrese el nombre a eliminar: ")
    try:
        conn = sql.connect("streamers.db")
        cursor = conn.cursor()

        instruccion = f"DELETE FROM streamers WHERE name = '{nom}'"
        cursor.execute(instruccion)
        print(f"{nom} fue eliminado con exito")
        conn.commit()
        conn.close()
    except:
        print("error")

def actualizarRow():
    act = input("ingrese el nombre que desea actualizar: ")
    nue = input("ingrese nuevo nombre: ")
    try:
        conn = sql.connect("streamers.db")
        cursor = conn.cursor()

        instruccion = f"UPDATE streamers SET name = '{nue}' WHERE name = '{act}'"
        cursor.execute(instruccion)
        print("Actuializado con exito")
        conn.commit()
        conn.close()
    except:
        print("error")


"""if __name__ == "__main__":
    actualizarRow()
    pass"""