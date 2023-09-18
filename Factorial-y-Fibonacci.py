def fibo(nfi):
    F1 = 0
    F2 = 1
    
    for uwu in range(nfi):
        nfi = F2+F1
        F1 = F2
        F2 = nfi
    print(nfi)

def factos(nfa):
    resultados = []
    facto = 1
    for x in range(1,nfa+1):
        facto*=x
        
    print(facto)


def main():
    print("Seleccione un método de búsqueda:")
    print("1] Fibonacci")
    print("2] Factorial")
    
    elec = int(input())
    
    if elec not in [1, 2]:
        print("Opción inválida")
        return
    
    if elec == 1:
        nfi = int(input("Ingrese el valor de n: "))
        fibo(nfi)

    elif elec == 2:
        nfa = int(input("Ingrese el dato a calcular: "))
        factos(nfa)
        

if __name__ == "__main__":
    main()
