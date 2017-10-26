def remover_duplicados_consecutivos(pila):
	if pila.esta_vacia():
		return None
	
	lista = [pila.desapila()]
	
	while not pila.esta_vacia():
		value = pila.desapila()
		if value not in lista:
			lista.append(value)
		
	for i in range(len(lista)):
		pila.apila(lista.pop())
			
		
