# Gestión de inventarios


Productos=[]
id_producto=0



def comprobar_si_hay_productos():
    if len(Productos)==0:
        return False
    else:
        return True

def agregar_producto():
    print("----------AGREGANDO PRODUCTO---------")
    id_producto=len(Productos)+1
    nombre_producto=input("NOMBRE: ")
    cantidad_producto=int(input("CANTIDAD: "))
    while cantidad_producto <= 0:
        print("ERROR -> CANTIDAD NO VALIDAD -> INGRESE DE NUEVO")
        cantidad_producto=int(input("CANTIDAD: "))
    precio_producto=float(input("PRECIO: S/. "))
    while precio_producto<=0:
        print("ERROR -> DIGITE UN PRECIO VALIDO")
        precio_producto=float(input("PRECIO: S/. "))

    Productos.append([id_producto,nombre_producto,cantidad_producto,precio_producto])

def ver_productos():
    global Productos
    global id_producto

    if comprobar_si_hay_productos:
        print("-------------------------PRODUCTOS--------------------")
        for producto in Productos:
            print(f"ID: {producto[0]}, NOMBRE: {producto[1]}, CANTIDAD: {producto[2]}, PRECIO: S/. {producto[3]}")
    else:
        print("ERROR LISTA VACIA")

def actualizar_producto():
    global Productos

    if comprobar_si_hay_productos():
        print("---------ACTUALIZANDO PRODUCTO----------")
        id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
        producto_encontrado = False

        for producto in Productos:
            if producto[0] == id_actualizar:
                producto_encontrado = True
                print("Producto encontrado. Ingrese los nuevos datos:")
                nombre_producto = input("NOMBRE: ")
                cantidad_producto = int(input("CANTIDAD: "))
                while cantidad_producto <= 0:
                    print("ERROR -> CANTIDAD NO VALIDA -> INGRESE DE NUEVO")
                    cantidad_producto = int(input("CANTIDAD: "))
                precio_producto = float(input("PRECIO: S/. "))
                while precio_producto <= 0:
                    print("ERROR -> DIGITE UN PRECIO VALIDO")
                    precio_producto = float(input("PRECIO: S/. "))

                producto[1] = nombre_producto
                producto[2] = cantidad_producto
                producto[3] = precio_producto

                print("Producto actualizado exitosamente.")
                break

        if not producto_encontrado:
            print("No se encontró ningún producto con el ID proporcionado.")
    else:
        print("ERROR - LISTA VACIA")





def eliminar_producto():
    global Productos

    comprobar_si_hay_productos()
    ver_productos()
    print("---------ELIMINANDO PRODUCTO-----------")

    producto_eliminar=input("NOMBRE DEL PRODUCTO: ")
    producto_a_eliminar=[producto for producto in Productos if producto[1]==producto_eliminar]

    if len(producto_a_eliminar)==0:
        print("NO SE ENCONTRARON CONCIDENCIAS")
    else:
        print("SE ENCONTRARON CONCIDENCIAS -> MOSTRANDO: ")
        Productos=[producto for producto in Productos if producto[2]!=producto_eliminar]
        print(f"PRODUCTO: {producto_eliminar} -> ELIMINADO CON EXITO")


def buscar_producto_por_id_o_por_nombre():
    global Productos
    global id_producto

    
    if comprobar_si_hay_productos():
        print("--------BUSCANDO PRODUCTO----------")
        while True:
            print("¿COMO DESEA BUSCAR?")
            print("1. POR ID")
            print("2. POR NOMBRE")
            print("3. SALIR")
            opcion=int(input("OPCION (1-3): "))

            while 1 > opcion >3:
                print("ERROR. -> INGRESE UNA OPCION CORRECTA")
                opcion=int(input("OPCION (1-3): "))
            if opcion== 1:
                print("--------BUSCANDO PRODUCTO POR ID------")
                id_producto_buscar=int(input("ID: "))
                while id_producto_buscar < 0:
                    print("ERROR ID INCONRRECTO -> INGRESE UN ID VALIDO")
                    id_producto_buscar=int(input("ID: "))
                producto_encontrado_por_id=[producto for producto in Productos if producto[0]==id_producto_buscar]
                if len(producto_encontrado_por_id)==0:
                    print("NO SE ENCONTRARON CONCIDENCIAS")
                else:
                    print("SE ENCONTRARON CONSIDENCIAS")
                    for producto in producto_encontrado_por_id:
                        print(f"ID: {producto[0]}, NOMBRE: {producto[1]}, CANTIDAD: {producto[2]}, PRECIO: S/. {producto[3]}")
            elif opcion == 2:
                print("--------BUSCANDO PRODUCTO POR NOMBRE---------")
                nombre_producto_buscar=input("NOMBRE: ")
                producto_encontrado_por_nombre=[producto for producto in Productos if producto[1]== nombre_producto_buscar]
                if len(producto_encontrado_por_nombre) == 0:
                    print("NO SE ENCONTRARON CONCIDENCIAS")
                else:
                    print("SI SE ENCONTRARON CONCIDENCIAS -> MOSTRANDO: ")
                    for producto in producto_encontrado_por_nombre:
                        print(f"ID: {producto[0]}, NOMBRE: {producto[1]}, CANTIDAD: {producto[2]}, PRECIO: {producto[3]}")
            elif opcion==3:
                break
    else: 
        print("ERROR LISTA VACIA")

def calcular_valor_total_inventario():
    global Productos
    global id_producto

    valor_total=0
    if comprobar_si_hay_productos():

        for producto in Productos:
            valor_total+=producto[2]*producto[3]
            print(f"EL VALOR TOTAL ES: {valor_total}")
    else: 
        print("ERROR - LISTA VACIA")
    


def mostrar_menu():
    print("1. AGREGAR PRODUCTO")
    print("2. ELIMINAR PRODUCTO")
    print("3. VER PRODUCTOS")
    print("4. ACTUALIZAR PRODUCTO")
    print("5. BUSCAR PRODUCTO POR ID O NOMBRE")
    print("6. CALCULAR VALOR TOTAL DEL INVENTARIO")
    print("7. SALIR")


def main_productos():
    while True:
        mostrar_menu()
        opcion=int(input("OPCION: "))

        if opcion==1:
            agregar_producto()
        elif opcion==2:
            eliminar_producto()
        elif opcion==3:
            ver_productos()
        elif opcion==4:
            actualizar_producto()
        elif opcion==5:
            buscar_producto_por_id_o_por_nombre()
        elif opcion ==6:
            calcular_valor_total_inventario()
        elif opcion==7:
            break
        else:
            print("ERROR -> OPCION INVALIDA -> VUELVA A INTRODUCIR UNA OPCION")
            opcion=int(input("OPCION: "))
    
main_productos()

