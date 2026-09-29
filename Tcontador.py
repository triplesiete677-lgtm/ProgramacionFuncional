def crear_contador_paso(fn_paso):
  cuenta = 0

  def incrementar():
    nonlocal cuenta
    cuenta = fn_paso(cuenta)
    return cuenta

  return incrementar