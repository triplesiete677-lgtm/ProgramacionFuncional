def componer_dos(f, g):
  def compuesta(x):
    return f(g(x))

  return compuesta