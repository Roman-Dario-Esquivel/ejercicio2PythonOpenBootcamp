def determina_anio(dias):
    if dias==366:
        print("Es año biciesto")
    else:
        print("No es año biciesto")
    
    
determina_anio(int(input("ingrese cantidad de dias que tiene el año:")))