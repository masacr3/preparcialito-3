#pila TDA con todas sus primitivas

def invertir_lista(self):
	if not self.primero or not self.primero.sig :
		return None
	
	primero = self.primero
	recorrer = self.primero
	pila = PILA()
	
	while recorrer:
		pila.apila(recorrer)
		recorrer = recorrer.sig
	
	primero = pila.desapila()
	
	while not pila.esta_vacia():
		primero.sig = pila.desapila()
		primero = primero.sig
	
	primero.sig = None
	


