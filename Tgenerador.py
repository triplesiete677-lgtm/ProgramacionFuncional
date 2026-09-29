def crear_generador_sufijos(patron_lambda):
  def generar(nombre):
    return patron_lambda(nombre)

  return generar