import pandas as pd


def calcular_salario_por_hora(file_path):

    try:

        df = pd.read_csv(file_path)

        colunas_necessarias = ['Nome', 'Salario', 'Horas Trabalhadas']
        for coluna in colunas_necessarias:
            if coluna not in df.columns:
                raise KeyError(f"A coluna '{coluna}' não foi encontrada no arquivo CSV!")

        # Calcular o salário por hora
        df['SalarioPorHora'] = df['Salario'] / df['Horas Trabalhadas']

        df_resultado = df[['Nome', 'SalarioPorHora']]

        return df_resultado

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return None
    except KeyError as e:
        print(f"Erro: {e}")
        return None
    except ZeroDivisionError:
        print("Erro: Foi encontrada uma divisão por zero na coluna 'Horas Trabalhadas'.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

file_path = r'C:\Users\Administrator\PycharmProjects\PythonProject1\pessoas_salarios.csv'


tabela_salario_hora = calcular_salario_por_hora(file_path)

if tabela_salario_hora is not None:

    print("\nTabela:")
    print(f"{'Nome':<20}{'Salário por Hora (R$)':<25}")
    print("-" * 45)
    for _, row in tabela_salario_hora.iterrows():
        print(f"{row['Nome']:<20}{row['SalarioPorHora']:<25.2f}")


    file_name = 'tabela_salario_por_hora.txt'
    with open(file_name, 'w') as file:
        file.write(f"{'Nome':<20}{'Salario por Hora (R$)':<25}\n")
        file.write("-" * 45 + "\n")
        for _, row in tabela_salario_hora.iterrows():
            file.write(f"{row['Nome']:<20}{row['SalarioPorHora']:<25.2f}\n")

    print(f"\nTabela salva em '{file_name}'!")
