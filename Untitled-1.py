num=int(input("digite um numero inteiro :"))
print('''Escolha umas das bases para converçao :
[1] converte para binario :
[2] converter para octal :
[3]converter para HEXADECIMAL:
''')
opcao=int(input("sua opção "))
if opcao==1:
    print(" {} convertido para binario é igual {}".format(num,bin(num)))
elif opcao==2:
    print("{} convertido para octal é igual {}".format(num,oct(num)))
elif opcao==3:
    print("{} convertido para Hexadecimal e igual {}".format(num,hex(num)))
else:
    print("Opçao incorreta tente novamente  ")