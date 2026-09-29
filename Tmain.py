if __name__ == "__main__":
  print("--- PRUEBAS NIVEL 1 ---")
  fmt = crear_formateador(
      "[DOC]: ", lambda s: s.strip().upper()
  )
  print(fmt("  informe técnico  "))

  op = crear_operador(10, lambda x, f: x * f)
  print(op(5))

  desc = crear_descuento_dinamico(lambda p: p > 100)
  print(desc(150, 0.20))  # Aplica descuento
  print(desc(80, 0.20))  # No aplica

  gen_suf = crear_generador_sufijos(lambda n: f"{n}_v1.pdf")
  print(gen_suf("reporte"))

  conv = crear_conversor(0.92, lambda m: m * 0.05)  # 5% comisión adicional
  print(conv(100))

  print("\n--- PRUEBAS NIVEL 2 ---")
  contador = crear_contador_paso(lambda c: c + 3)
  print(contador())  # 3
  print(contador())  # 6

  acum = crear_acumulador_validado(lambda v: v > 0)
  print(acum(10))
  print(acum(-5))  # Ignorado
  print(acum(20))  # Total 30

  prom = crear_promediador_filtrado(lambda v: 0 <= v <= 100)
  print(prom(80))
  print(prom(90))
  print(prom(150))  # Filtrado por ruido

  lim = crear_limitador_avanzado(
      2, lambda intentos: print(f"¡Alerta! Intentos excedidos: {intentos}")
  )
  print(lim())  # True
  print(lim())  # True
  print(lim())  # False (Dispara alerta)

  conm = crear_conmutador(["Apagado", "En Espera", "Encendido"])
  print(conm())
  print(conm())
  print(conm())
  print(conm())  # Cíclico

  print("\n--- PRUEBAS NIVEL 3 ---")
  res_proc = procesar_coleccion(
      [1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0, lambda x: x ** 2
  )
  print(res_proc)  # [4, 16, 36]

  datos_agrupar = [
      {"categoria": "A", "val": 1},
      {"categoria": "B", "val": 2},
      {"categoria": "A", "val": 3},
  ]
  print(agrupar_por(datos_agrupar, lambda d: d["categoria"]))

  ejecutor = ejecutar_y_rastrear(lambda: "OK", 3)
  print(ejecutor())

  comp = componer_dos(lambda x: x + 1, lambda x: x * 2)
  print(comp(5))  # (5 * 2) + 1 = 11


  @auditar_ejecucion
  def tarea_lenta():
    time.sleep(0.1)
    return "Hecho"


  # Auditoría con logger personalizado
  auditor = auditar_ejecucion(
      lambda: sum(range(1000000)), lambda inf: print(f"LOG: {inf}")
  )
  auditor()

  print("\n--- PRUEBAS NIVEL 4 ---")
  validador = crear_validador_multiple(
      lambda x: x > 0, lambda x: x % 2 == 0, lambda x: x < 100
  )
  print(validador(42))  # True
  print(validador(105))  # False


  @memoizar_avanzado, 2
  def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


  # Nota: para memoización manual con HOF:
  def fib_costosa(n):
    return n if n < 2 else fib_costosa(n - 1) + fib_costosa(n - 2)


  fib_memo = memoizar_avanzado(fib_costosa, max_items=10)
  print(fib_memo(10))

  pipeline = crear_pipeline(
      lambda x: x + 2, lambda x: x * 3, lambda x: x - 1
  )
  print(pipeline(5))  # ((5 + 2) * 3) - 1 = 20

  suscribir, emitir = crear_sistema_eventos()
  suscribir(lambda ev: print(f"Listener 1 recibió: {ev}"))
  suscribir(lambda ev: print(f"Listener 2 recibió: {ev}"))
  emitir("¡Inicio de sesión exitoso!")

  inventario = [
      {"nombre": "Laptop", "precio": 1200},
      {"nombre": "Mouse", "precio": 25},
      {"nombre": "Teclado", "precio": 45},
  ]
  consultor = crear_consultor("precio")
  print(consultor(inventario, lambda p: p > 40))