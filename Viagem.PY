distancia=float(input("Qual a distancia da sua viagem? "))
print("Voce esta preste de começar sua viagem de {} km".format(distancia))
if distancia <=200 :
    preco=distancia* 0.50
else:
    preco=distancia*0.45
print("sua viagem custara R$ {} reais ! boa viagem ".format(preco))