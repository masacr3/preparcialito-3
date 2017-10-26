def es_palindromo(cola,n_elementos):
	""" pre: se asume que la cola no esta vacia y n_elementos es el 
		numero de elementos 
	"""     
	pila = PILA()
	for i in range(n_elementos // 2):
		pila.apila(cola.desencola())
	
	for i in range(n_elementos // 2):
		Letra,letra2 = cola.desencolar(),pila.desapilar()
		if letra != letra2:
			return False
	
	return True
	
		
