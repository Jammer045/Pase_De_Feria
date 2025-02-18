def verificar_ingreso():
    nombre = input("Ingrese su nombre: ").strip().capitalize()
    pase = input("Ingrese tipo de pase (vip o normal): ").strip().lower()
    tiene_entrada = input("¿Posee entrada? (si/no/s/n/true/false): ").strip().lower()

    if tiene_entrada in ['si', 's', 'true']:
        tiene_entrada = True
    else:
        tiene_entrada = False
    if nombre == "Julio" or pase == "vip":
        print("¡Bienvenido! Tienes ingreso libre.")
    elif tiene_entrada:
        usar_entrada = input("¿Desea utilizar su entrada? (si/no): ").strip().lower()
        if usar_entrada in ['si', 's']:
            print("¡Bienvenido! Has utilizado tu entrada.")
        else:
            print("Entrada no utilizada. Continuando con el proceso...")
    else:
        comprar_entrada = input("¿Desea comprar una entrada? (si/no): ").strip().lower()
        if comprar_entrada in ['si', 's']:
            dinero_disponible = float(input("Ingrese la cantidad de dinero disponible: $"))
            if dinero_disponible >= 1000:
                print("¡Venta de entrada exitosa! ¡Bienvenido!")
            else:
                print("Dinero insuficiente. Venta de entrada rechazada.")
        else:
            print("Gracias por visitarnos. ¡Hasta luego!")

verificar_ingreso()