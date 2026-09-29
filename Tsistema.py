def crear_sistema_eventos():
  suscriptores = []

  def suscribir(fn_listener):
    suscriptores.append(fn_listener)

  def emitir(evento):
    for listener in suscriptores:
      listener(evento)

  return suscribir, emitir