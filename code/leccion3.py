""" Añadimos los numeros del 1 al 10 a la lista: "lista"

    Args:

        x(int): valor tipo int

        lista(list): objeto tipo lista

"""

x=1
lista=[]

while x<=10:
    lista.append(x)
    x += 1

lista.sort(reverse=True)

print(lista)

"""Creamos un diccionario con emails y nombres

    Args:
        Variable(_type_): objeto tipo diccionario
"""


emails = {
    "Fran" : "Fran@hotmail.com",
    "Juan" : "Juan@hotmail.com",
    "Jose" : "Jose@hotmail.com",
    "Maria" : "Maria@hotmail.com",
}



"""Funcion para añadir nombres al diccionario
    Atributos de la funcion:

    **elemento 1**:
        Nombre de la persona

    **elemento 2**:
        email de la persona
"""
def añadir_nombre(nombre, email):
    emails[nombre]=email

