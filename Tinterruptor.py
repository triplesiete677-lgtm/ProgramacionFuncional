def crear_conmutador(lista_estados):
  indice = 0

  def siguiente():
    nonlocal indice
    if not lista_estados:
      return None
    estado = lista_estados[indice]
    indice = (indice + 1) % len(lista_estados)
    return estado

  return siguiente