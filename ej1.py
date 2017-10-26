def reemplazar(pila,nuevo,viejo):
	
	if pila.esta_vacia():
		return None
	
	_pila = PILA()
	
	while not pila.esta_vacia():
		value = pila.desapila()
		_pila.apila( nuevo if value == viejo else value )
	
	while not _pila.esta_vacia():
		pila.apila(_pila.desapila())
	
