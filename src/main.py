def formatear_nombre(nombre: str, apellido1: str, apellido2: str) -> str:
    """
    Formatea el nombre de una persona

    :param: nombre
    :param: apellido1
    :param: apellido2
    """

    nombre = nombre.title().strip()
    apellido1 = apellido1.title().strip()
    apellido2 = apellido2.title().strip()

    return f"{nombre} {apellido1} {apellido2}"

def main():

    nombre = input("Introduce el nombre: ")
    apellido1 = input("Introduce el primer apellido: ")
    apellido2 = input("Introduce el segundo apellido: ")

    nombre_completo = formatear_nombre(nombre, apellido1, apellido2)
    print("Nombre completo: ", nombre_completo)

if __name__ == "__main__":
    main()