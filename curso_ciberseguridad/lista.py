pais = ['Colombia', 'Japon', 'Italia', 'España', 'Mexico']
print("lista de string:", pais)

print("primer elemento de la lista:", pais[0])
print("segundo elemento de la lista:", pais[1])
print("tercer y cuarto elemento de la lista:", pais[2],pais[3])
print("elementos entre el primero y el ultimo de la lista:", pais[0:-1])

paises_nuevos = ['Chile', 'peru', 'Rusia']
nueva_lista = pais+paises_nuevos
print("lista con nuevos elementos:", nueva_lista)
nueva_lista.append('Alemania')
print("lista con Alemania", nueva_lista)

print("longitud de la lista:", len(nueva_lista))

nueva_lista.remove('España')
print("lista con el elemento eliminado:", nueva_lista)
print("eliminar elemento de la posicion x:", nueva_lista.pop(1))
print("lista sin el elemento eliminado de la posicion x:", nueva_lista)
