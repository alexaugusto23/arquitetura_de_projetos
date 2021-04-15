import time
from sequencia_fibonacci import fib
from def_list1 import f1
from def_list2 import f2
from def_list3 import f3

inicio = time.time()
#print('Testando Sequência Fibonacci')
#print(fib(10))
print(f1([48,49,50,51,52,53,54,55,56,57,48,49,50,51,52,53,54,55,56,57,48,49,50,51,52,53,54,55,56,57]))
print(f2([48,49,50,51,52,53,54,55,56,57,48,49,50,51,52,53,54,55,56,57,48,49,50,51,52,53,54,55,56,57]))
print(f3([48,49,50,51,52,53,54,55,56,57,48,49,50,51,52,53,54,55,56,57,48,49,50,51,52,53,54,55,56,57]))


fim = time.time()
tempo_de_execucao = fim - inicio 
print(f"{tempo_de_execucao*1000}") # milissegundos 
print(f"{tempo_de_execucao}") # segundos 
print(f"{tempo_de_execucao/60}") # minutos 