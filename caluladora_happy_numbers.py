def NumFeliz(n):    
    res = sum = 0    
    while(n > 0):    
        res = n % 10 
        sum = sum + (res * res)    
        n = n // 10   
    return sum    
        
num = int(input("Ingresá un número para saber si es o no feliz: "))    
resultado = num    
     
while(resultado != 1 and resultado != 4):    
    resultado = NumFeliz(resultado)   
     
if(resultado == 1):    
    print(num, "es un número feliz :)")   
else:    
    print(num, "no es un número feliz :(")
