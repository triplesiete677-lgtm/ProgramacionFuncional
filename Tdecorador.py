import time


def auditar_ejecucion(fn_objetivo, fn_logger):
  def wrapper(*args, **kwargs):
    inicio = time.time()
    resultado = fn_objetivo(*args, **kwargs)
    duracion = time.time() - inicio
    fn_logger({"funcion": fn_objetivo.__name__, "duracion": duracion})
    return resultado

  return wrapper