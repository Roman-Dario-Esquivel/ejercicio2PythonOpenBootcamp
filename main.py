def determina_anio(anio):
    if (anio%4)==0:
        print("Es año biciesto")
    else:
        print("No es año biciesto")
    
    
determina_anio(int(input("Ingrese año: ")))