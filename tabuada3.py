
while True:
    num=int(input("Digite um numero para sua Tabuada : "))
    print("-"*30)
    if num < 0 :
        break
    for c in range (1,11):
        print(f" {num} x {c}={num*c} ")
        
    print("-"*30)

print("PROGRAMA DE TABUADA ENCERRADO. volte sempre ! ")