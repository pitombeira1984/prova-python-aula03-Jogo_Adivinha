def jogoadivinha():
    
    contador = 0
    while True:
        numero = int(input(f'Digite um numero de 0 a 10: '))
    
        if numero == 7:
            print('Você ganhou!')
            break
        else:
            print('Tente novamente!')
            
        contador += 1
            
        if contador == 3:
            print('Você perdeu!')
            break
           
jogoadivinha()            
    
