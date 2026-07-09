#Aquí validaremos los procesos

def validar_texto(texto):
    return len(texto.strip()) > 0

def validar_duracion(duracion_min):
    try:
        valor = int(duracion_min)
        if valor > 0:
            return valor
        else:
            print("Debe ingresar valores mayores que cero.")
    except ValueError:
        print("Debe ingresar valores numéricos enteros.")

def validar_clasificacion(clas):
    return clas.strip().upper() in ['A','B','C']

def validar_es_3d(es_3d):
    return es_3d.lower() in ['s','n']

def validar_precio(precio_str):
    try:
        valor = int(precio_str)
        if valor > 0:
            return valor
        else:
            print("Debe ingresar valores mayores que cero.")
    except ValueError:
        print("Debe ingresar valores numéricos enteros.")

def validar_cupos(cupos_str):
    try:
        valor = int(cupos_str)
        if valor >= 0:
            return valor
        else:
            print("Debe ingresar un numero mayor o igual que cero.")
    except ValueError:
        print("Debe ingresar valores numéricos enteros.")

def buscar_codigo(cartelera,codigo):
    return codigo.strip().upper() in cartelera


#Aquí haremos las funciones de operación

def cupos_genero(peliculas,genero,cartelera):

    total_cupos = 0
    encontrado = False
    encontrado_buscar = cartelera.items()

    for cod, datos_pel in peliculas.items():
        datos_pel[1]

        encontrado = True
        total_cupos += cartelera[cod][1]
    pass

def busqueda_peliculas(cartelera,peliculas,p_min,p_max):

    for cod, datos_car in cartelera.items():
        cod = datos_car[0]
        cod = datos_car[1]
    pass

def actualizar_precio(cartelera,codigo,nuevo_precio):

    cod_upper = codigo.strip().upper()
    if buscar_codigo(cartelera,cod_upper):
        return False

def agregar_pelicula(peliculas,cartelera,codigo,titulo,genero,duracion_min,clasificacion,idioma,es_3d,precio,cupos):

    resultados = []

    cod_upper = codigo.strip().upper()
    if buscar_codigo(cartelera,codigo):
        return False

    if resultados:
        resultados.sort()

    peliculas[cod_upper] = [
        titulo.strip,
        genero.strip,
        duracion_min,
        clasificacion.strip,
        idioma.strip,
        es_3d.strip,
    ]

    cartelera[cod_upper] = int(precio), int(cupos)

def eliminar_pelicula(peliculas,codigo,cartelera):

    cod_upper = codigo.strip().upper()
    if buscar_codigo(cartelera,codigo):
        del peliculas[cod_upper]
        del cartelera[cod_upper]
        return True
    return False

def mostrar_menu():
    print("""\n========== MENÚ PRINCIPAL ==========
1. Cupos por género
2. Búsqueda de películas por rango de precio
3. Actualizar precio de película
4. Agregar película
5. Eliminar película
6. Salir
=====================================""")

def leer_opcion():
    try:
        opcion = int(input("Ingrese opción: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Recuerde ingresar una opción de 1 a 6.")
    except ValueError:
        print("Debe ingresar una opción de numero entero.")


#Aquí completaremos con el menú principal

def main():
    peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }

    cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
    }

    print("¡¡Bienvenido CineMax!!")

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            codigo = input("Ingrese género a consultar: ")
            pass
        elif opcion == 2:
            p_min=int(input("ingrese precio mínimo: "))
            p_max=int(input("Ingrese precio máximo: "))
        elif opcion == 3:
            repetir = 's'
            codigo = input("Ingrese código de la película: ")
            if buscar_codigo(cartelera,codigo):
                print("")

            while repetir == 's':
                
                pass

            repetir = input("¿Desea actualizar otro precio (s/n)?: ")
        elif opcion == 4:
            codigo = input("ingrese código de película: ")
            if buscar_codigo(cartelera,codigo):
                print("Esa codigo ya esta asociada a una pelicula.")
            else:
                titulo = input("Ingrese título: ")
                if not validar_texto(titulo):
                    continue

                genero = input("Ingrese género: ")
                if not validar_texto(genero):
                    continue

                duracion = input("ingrese duración (minutos): ")
                if not validar_duracion(duracion):
                    continue

                clasificacion = input("Ingrese clasificación: ")
                if not validar_clasificacion(clasificacion):
                    continue

                idioma = input("Ingrese idioma: ")
                if not validar_texto(idioma):
                    continue

                es_3d = input("¿Es 3D? (s/n): ")
                if not validar_es_3d(es_3d):
                    continue

                precio = int(input("Ingrese precio: "))
                if not validar_precio(precio):
                    continue

                cupos = int(input("Ingrese cupos: "))
                if not validar_cupos(cupos):
                    continue

                exito = agregar_pelicula(peliculas,cartelera,codigo,titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos)

                if exito:
                    print("Película agregada")
                else:
                    print("Error inesperado.")

        elif opcion == 5:
            codigo = input("Ingrese el codigo de la pelicula que desea eliminar: ")
            if buscar_codigo(cartelera,codigo):
                print("Ya existe una pelicula con ese codigo.")
            else:
                eliminar_pelicula(peliculas,cartelera,codigo)
                print("Pelicula eliminada con éxito.")
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__=="__main__":
    main()