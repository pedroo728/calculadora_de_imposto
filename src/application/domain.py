from src.application.config import IMPOSTO_IR, IMPOSTO_INSS, IMPOSTO_SINDICATO

def calcular_dados_usuario(salario_hora, horas_mensal):
    salario_bruto = salario_hora * horas_mensal
    return salario_bruto
    
def calcular_impostos(salario_bruto):
    ir = salario_bruto * IMPOSTO_IR
    inss = salario_bruto * IMPOSTO_INSS
    sindicato = salario_bruto * IMPOSTO_SINDICATO
    return ir, inss, sindicato

def calcular_resultados(salario_bruto, ir, inss, sindicato):
    salario_liquido = salario_bruto - ir - inss - sindicato
    deducoes = ir + inss + sindicato
    return salario_liquido, deducoes



