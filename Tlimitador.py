def crear_limitador_avanzado(max_intentos, fn_alerta):
  intentos = 0

  def verificar():
    nonlocal intentos
    intentos += 1
    if intentos > max_intentos:
      fn_alerta(intentos)
      return False
    return True

  return verificar