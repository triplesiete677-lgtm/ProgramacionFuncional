from functools import wraps


def memoizar_avanzado(fn_costosa, max_items):
  cache = {}

  @wraps(fn_costosa)
  def memoizada(*args):
    if args in cache:
      return cache[args]
    if len(cache) >= max_items:
      primer_key = next(iter(cache))
      del cache[primer_key]
    resultado = fn_costosa(*args)
    cache[args] = resultado
    return resultado

  return memoizada