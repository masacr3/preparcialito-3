def suma_acumulativa(self):
	if not self.primero:
		return None
	
	lista_nueva = ListaEnlazada(self.primero.value)
	
	if not self.primero.sig:
		return lista_nueva
	
	acumulador = self.primero.value
	actual = self.primero.sig
	
	while actual:
		acumulador += actual.value
		lista_nueva.push(acumulador)
	
	return lista_nueva
	
	
	
	

		
