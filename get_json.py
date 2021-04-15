import requests
import json
import time
from unittest import TestCase, main

class Blog:
    def __init__(self, nome):
        self.nome = nome 
        self.versao = 1 
 
    def posts(self):
        endereco = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(endereco)
        return response.json()

    def __repr__(self):
        return f'Blog: {self.nome}'

class Testes(TestCase):

    def teste_download(self):
        start = time.time()
        blog = Blog("Teste")
        result = blog.posts()
        with open('pessoas.json', 'w') as json_file:
            json.dump(result, json_file)
        
        end = time.time()
        execution_time = end - start 
        print(f"{blog.nome} {blog.versao} tempo de execução: {execution_time * 1000:0.2f} ms")

        self.assertIsNotNone(result)
        self.assertIsInstance(result[0], dict)

if __name__ == '__main__':
    main()