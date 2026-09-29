def crear_validador_multiple(*lambdas_criterios):
  def validar(objeto):
    return all(criterio(objeto) for criterio in lambdas_criterios)

  return validar