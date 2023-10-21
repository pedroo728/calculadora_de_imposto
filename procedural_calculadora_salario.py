IMPOSTO_IR = 0.11
IMPOSTO_INSS = 0.08
IMPOSTO_SINDICATO = 0.05

salario_hora = float(input("Quanto voce ganha de salario por hora?: "))
horas_mensal = float(input("Quantas horas voce trabalha por mes?: "))

salario_bruto = salario_hora * horas_mensal
ir = salario_bruto * IMPOSTO_IR
inss = salario_bruto * IMPOSTO_INSS
sindicato = salario_bruto * IMPOSTO_SINDICATO
salario_liquido = salario_bruto - ir - inss - sindicato
deducoes = ir + inss + sindicato

print(f"Salário Bruto : R${salario_bruto:.2f}")
print(f"Imposto de Renda(11%) : R$ {ir:.2f}")
print(f"INSS(8%) : R$ {inss:.2f}")
print(f"Sindicato(5%) : R$ {sindicato:.2f}")
print(f"Deducoes Total : R$ {deducoes}")
print(f"Salario Liquido : R$ {salario_liquido}")