def main():
    # Escribe tu código abajo de esta línea
Ana=str(input("Tirada de Ana: ", ))
Juan=str(input("Tirada de Juan: ", ))
    
if len(Ana)>1 or len(Juan)>1:
    print ('Las tiradas deben ser de un caracter')  
elif Ana == "a" and Juan== "p": 
    print ("Gana Juan")
elif Ana == "p" and Juan== "t": 
    print ("Gana Juan")
elif Ana == "t" and Juan== "a": 
    print ("Gana Juan")
elif Ana == "a" and Juan== "a":
    print ("Empate")
elif Ana == "t" and Juan== "t": 
    print ("Empate")
elif Ana == "p" and Juan== "p": 
    print ("Empate")
elif Ana == "t" and Juan== "p": 
    print ("Gana Ana")
elif Ana == "p" and Juan== "a": 
    print ("Gana Ana")
elif Ana == "a" and Juan== "t": 
    print ("Gana Ana")
else:
    print('Tirada incorrecta')

if __name__ == '__main__':
    main()
