salarioHora = float (input('Quanto você ganha por hora?'))
horasTrabalhadas = int (input('Quantas horas voce trabalha por mês?'))
salarioBruto = salarioHora * horasTrabalhadas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print ('SALARIO BRUTO = R$', salarioBruto)
print ('IMPOSTO DE RENDA = R$', impostoRenda)
print ('INSS = R$', inss)
print ('SINDICATO = R$', sindicato)
print ('SALARIO LIQUIDO = R$', salarioLiquido)