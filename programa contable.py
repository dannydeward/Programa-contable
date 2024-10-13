import datetime

# Función para registrar una transacción
def registrar_transaccion(registros, cantidad, descripcion, tipo):
    fecha_actual = datetime.date.today()
    if fecha_actual not in registros:
        registros[fecha_actual] = []
    registros[fecha_actual].append((cantidad, descripcion, tipo))

# Función para calcular el balance general del día
def balance_general_dia(registros, fecha):
    if fecha in registros:
        transacciones = registros[fecha]
        ingresos = sum(cantidad for cantidad, _, tipo in transacciones if tipo == 'ingreso')
        gastos = sum(cantidad for cantidad, _, tipo in transacciones if tipo == 'gasto')
        balance_dia = ingresos - gastos
        return balance_dia
    else:
        return 0

# Función para calcular el balance general de la semana
def balance_general_semana(registros, fecha):
    inicio_semana = fecha - datetime.timedelta(days=fecha.weekday())
    fin_semana = inicio_semana + datetime.timedelta(days=6)
    balance_semana = sum(balance_general_dia(registros, d) for d in registros if inicio_semana <= d <= fin_semana)
    return balance_semana

# Función para calcular el balance general del mes
def balance_general_mes(registros, fecha):
    inicio_mes = datetime.date(fecha.year, fecha.month, 1)
    fin_mes = datetime.date(fecha.year, fecha.month, 28) + datetime.timedelta(days=4)
    fin_mes = fin_mes - datetime.timedelta(days=fin_mes.day)
    balance_mes = sum(balance_general_dia(registros, d) for d in registros if inicio_mes <= d <= fin_mes)
    return balance_mes

# Función para imprimir el balance general
def imprimir_balance(registros):
    fecha_actual = datetime.date.today()
    print(f"--- Balance General ---")
    print(f"Balance del día ({fecha_actual}): {balance_general_dia(registros, fecha_actual)}")
    print(f"Balance de la semana ({fecha_actual}): {balance_general_semana(registros, fecha_actual)}")
    print(f"Balance del mes ({fecha_actual}): {balance_general_mes(registros, fecha_actual)}")

# Función principal
def main():
    registros = {}

    # Menú de opciones
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Transacción")
        print("2. Imprimir Balance General")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cantidad = float(input("Ingrese la cantidad: "))
            descripcion = input("Ingrese la descripción: ")
            tipo = input("¿Es un ingreso o un gasto? (ingreso/gasto): ").lower()
            registrar_transaccion(registros, cantidad, descripcion, tipo)
        elif opcion == '2':
            imprimir_balance(registros)
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

    # Guardar los registros en un archivo
    with open("registros.txt", "w") as archivo:
        for fecha, transacciones in registros.items():
            archivo.write(f"{fecha}:\n")
            for cantidad, descripcion, tipo in transacciones:
                archivo.write(f"{cantidad}, {descripcion}, {tipo}\n")

if __name__ == "__main__":
    main()
