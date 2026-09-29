def crear_operador(factor, operacion_lambda):
  def operar(x):
    return operacion_lambda(x, factor)

  return operar