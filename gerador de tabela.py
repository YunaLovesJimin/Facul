import pandas as pd
import random

def criar_csv_aleatorio(file_path, quantidade):

    nomes = [
        "João", "Maria", "Pedro", "Ana", "Carlos", "Clara", "Paulo", "Fernanda",
        "Lucas", "Juliana", "Gabriel", "Mariana", "Rafael", "Cecília", "Ricardo",
        "Aline", "André", "Bianca", "Felipe", "Sofia"
    ]

    dados = {
        "Nome": [random.choice(nomes) for _ in range(quantidade)],
        "Salario": [round(random.uniform(1500, 10000), 2) for _ in range(quantidade)],
        "Horas Trabalhadas": [random.randint(80, 200) for _ in range(quantidade)]
    }

    df = pd.DataFrame(dados)

    df.to_csv(file_path, index=False)
    print(f"Arquivo criado com sucesso!")

file_path = r'C:\Users\Administrator\PycharmProjects\PythonProject1\pessoas_salarios.csv'
quantidade_linhas = 20

criar_csv_aleatorio(file_path, quantidade_linhas)
