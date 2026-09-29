def procesar_coleccion(lista, fn_predicado, fn_transformacion):
  return list(map(fn_transformacion, filter(fn_predicado, lista)))