from enum import Enum

#resultados a retornar en formato clase (enum)
class Numero(Enum):
    PERFECTO = 1
    ABUNDANTE = 2
    DEFECTIVO = 3

def Ejercicio1(zNum):
	#hasta la mitad
    ToFor = zNum // 2 + 1
	
    Acum = 0
	
	#loop
    for i in range(1, ToFor):
		#es divisible?
        if zNum % i == 0:
			#voy sumando divisibles
            Acum += i
    
	#es el mismo valor que el número
    if Acum == zNum:
        return Numero.PERFECTO
    
	#es mayor que el número
    if Acum > zNum:
        return Numero.ABUNDANTE
    
	#sinó la opción restante
    return Numero.DEFECTIVO
        
#llamada
print("Resultado: ", Ejercicio1(12))