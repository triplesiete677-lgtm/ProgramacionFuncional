def agrupar_por(lista, fn_clave):
  resultado = {}
  for item in lista:
    clave = fn_clave(item)
    if clave not in resultado:
      resultado[clave] = []
    resultado[clave].append(item)
  return resultado