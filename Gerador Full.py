import pandas as pd
import random


def gerar_tabela_aleatoria(quantidade):

    nomes = [
        "João", "Maria", "Pedro", "Ana", "Carlos", "Clara", "Paulo", "Fernanda",
        "Lucas", "Juliana", "Gabriel", "Mariana", "Rafael", "Cecília", "Ricardo",
        "Aline", "Andre", "Bianca", "Felipe", "Sofia"
    ]


    if quantidade > len(nomes) + 1:
        raise ValueError("A quantidade de linhas excede o número de nomes únicos disponíveis (incluindo 'Virgínia').")


    nomes_selecionados = ["Virgínia"] + random.sample(nomes, quantidade - 1)


    dados = {
        "Nome": nomes_selecionados,
        "Salario": [round(random.uniform(1500.00, 10000.00), 2) for _ in range(quantidade)],
        "Horas Trabalhadas": [random.randint(80, 200) for _ in range(quantidade)],
    }
    df = pd.DataFrame(dados)
    return df


def exibir_tabela(df):
    print("\nTabela:")
    print(f"{'Nome':<15}{'Salario (R$)':<15}{'Horas Trabalhadas':<20}")
    print("-" * 50)

    for _, row in df.iterrows():
        print(f"{row['Nome']:<15}{row['Salario']:<15.2f}{row['Horas Trabalhadas']:<20}")


def salvar_tabela_com_espacamento(df, file_path):
    with open(file_path, 'w') as f:
        # Cabeçalhos com espaçamento
        f.write(f"{'Nome':<15}{'Salario (R$)':<15}{'Horas Trabalhadas':<20}\n")
        f.write("-" * 50 + "\n")
        # Dados da tabela
        for _, row in df.iterrows():
            f.write(f"{row['Nome']:<15}{row['Salario']:<15.2f}{row['Horas Trabalhadas']:<20}\n")

    print(f"\nTabela salva com sucesso no arquivo {file_path}!")


if __name__ == "__main__":
    quantidade_linhas = 10
    arquivo_saida = "Tabela.txt"

    try:
        tabela = gerar_tabela_aleatoria(quantidade_linhas)
        exibir_tabela(tabela)
        salvar_tabela_com_espacamento(tabela, arquivo_saida)
    except ValueError as e:
        print(f"Erro: {e}")
