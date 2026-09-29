def crear_acumulador_validado(criterio_lambda):
  total = 0

  def acumular(valor):
    nonlocal total
    if criterio_lambda(valor):
      total += valor
    return total

  return acumular