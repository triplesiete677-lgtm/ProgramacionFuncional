def crear_descuento_dinamico(regla_condicional_lambda):
  def calcular(precio, descuento_fijo):
    if regla_condicional_lambda(precio):
      return precio * (1 - descuento_fijo)
    return precio

  return calcular