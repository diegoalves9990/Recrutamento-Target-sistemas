#Resposta para a 2° questão do recrutamento:
#A sequência de Fibonacci é uma sequência de números, onde o número 1 é o primeiro e segundo termo da ordem e os demais são originados pela soma de seus antecessores. 

n = int(input('Quantas você quer que eu mostre? '))
n1 = 0
n2 = 1 
cont = 3
print('{} -> {} -> '.format(n1, n2), end='')

while cont <= n:
    n3 = n1 + n2
    print('{} -> '.format(n3), end='')
    n1 = n2
    n2 = n3
    cont +=1
print(' Fim do curso.')
