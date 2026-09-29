def ejecutar_y_rastrear(fn_tarea, n):
  historial = []

  def ejecutar():
    nonlocal historial
    for _ in range(n):
      res = fn_tarea()
      historial.append(res)
    return historial

  return ejecutar