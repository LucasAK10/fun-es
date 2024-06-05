
import math

def calcular_equacao_primeiro_grau():
    print("Equação do primeiro grau: ax + b = 0")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    
    if a == 0:
        if b == 0:
            print("A possui infinitas soluções.")
        else:
            print("A equação não possui solução.")
    else:
        x = -b / a
        print("A solução da equação é x =", x)

def calcular_equacao_segundo_grau():
    print("Equação do segundo grau: ax² + bx + c = 0")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("As soluções da equação são x1 =", x1, "e x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("A única solução da equação é x =", x)
    else:
        valor_real = -b / (2*a)
        valor_imaginario = math.sqrt(abs(delta)) / (2*a)
        print("As soluções da equação são complexas:")
        print("x1 =", valor_real, "+", valor_imaginario, "i")
        print("x2 =", valor_real, "-", valor_imaginario, "i")

def main():
    print("Escolha o tipo de equação que deseja calcular:")
    print("1 - Equação do primeiro grau")
    print("2 - Equação do segundo grau")
    escolha = int(input("Digite a opção desejada: "))
    
    
    if escolha == 1:
        calcular_equacao_primeiro_grau()
    elif escolha == 2:
        calcular_equacao_segundo_grau()
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")
        return

if __name__ == "__main__":
    main()
    

