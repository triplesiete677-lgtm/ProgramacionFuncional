def crear_consultor(campo):
  def filtrar(lista, fn_condicion):
    return [item for item in lista if fn_condicion(item.get(campo))]

  return filtrar