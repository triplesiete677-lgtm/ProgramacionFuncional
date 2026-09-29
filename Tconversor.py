def crear_conversor(tasa, margen_lambda):
  def convertir(monto):
    monto_base = monto * tasa
    margen = margen_lambda(monto_base)
    return monto_base + margen

  return convertir