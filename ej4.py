def suma_acumulativa(self):
	if not self.primero:
		return None
	
	lista_nueva = ListaEnlazada()
	lista_nueva.push(self.primero.value)
	
	if not self.primero.sig:
		return lista_nueva
	
	acumulador = self.primero.value
	actual = self.primero.sig
	
	while actual:
		acumulador += actual.value
		lista_nueva.push(acumulador)
		actual = actual.sig
	
	return lista_nueva
	
	
	
	

		
