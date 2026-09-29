def crear_formateador(prefijo, fn_transformacion):
  def formatear(texto):
    return f"{prefijo}{fn_transformacion(texto)}"

  return formatear