
from controler import insertarRows,eliminarRows,leerRows,actualizarRow

def menu():
    print("1- Insertar")
    print("2- Eliminar")
    print("3- Leer")
    print("4- Actualizar")
    print("6- Salir")



menu()
op = int(input("ingrese una opcion: "))
while(op != 6):
    if(op == 1):
        insertarRows()
        menu()
        op = int(input("ingrese una opcion: "))
    elif(op == 2):
        eliminarRows()
        menu()
        op = int(input("ingrese una opcion: "))
    elif (op == 3):
        leerRows()
        menu()
        op = int(input("ingrese una opcion: "))
    elif (op == 4):
        actualizarRow()
        menu()
        op = int(input("ingrese una opcion: "))
    else:
        op = int(input("ingrese una opcion: "))

