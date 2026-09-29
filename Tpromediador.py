def crear_promediador_filtrado(filtro_ruido_lambda):
  valores = []

  def agregar(valor):
    nonlocal valores
    if filtro_ruido_lambda(valor):
      valores.append(valor)
    if not valores:
      return 0.0
    return sum(valores) / len(valores)

  return agregar