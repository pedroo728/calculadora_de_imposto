from src.application.input import entrada_de_dados
from src.application.output import mostra_todos_resultados
from src.application.domain import calcular_dados_usuario, calcular_impostos, calcular_resultados

if __name__ == '__main__':
    salario_hora, horas_mensal = entrada_de_dados()
    salario_bruto = calcular_dados_usuario(salario_hora, horas_mensal)
    ir, inss, sindicato = calcular_impostos(salario_bruto)
    salario_liquido, deducoes = calcular_resultados(salario_bruto, ir, inss, sindicato)
    mostra_todos_resultados(salario_bruto, ir, inss, sindicato, deducoes, salario_liquido)