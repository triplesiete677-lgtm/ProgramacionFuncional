from functools import reduce


def crear_pipeline(*funciones_transformacion):
  def ejecutar(dato_inicial):
    return reduce(lambda acc, f: f(acc), funciones_transformacion, dato_inicial)

  return ejecutar