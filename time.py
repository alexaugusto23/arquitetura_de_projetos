import time

inicio = time.time()
print('testando')
fim = time.time()
tempo_de_execucao = fim - inicio 
print(f"{tempo_de_execucao*1000:0.8f}") # milissegundos 
print(f"{tempo_de_execucao:0.8f}") # segundos 
print(f"{tempo_de_execucao/60:0.8f}") # minutos 