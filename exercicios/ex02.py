print ("─=≡Σᕕ( ͡° ͜ʖ ͡°)ᕗ Hospital Hiroshima ─=≡Σᕕ( ͡° ͜ʖ ͡°)ᕗ")
nome = input("Informe o nome do paciente \n").title()
idade = int(input("Informe a idade paciente \n"))
asmStt = input("O paciente possui quadro de asma ? SIM ou NÃO \n")
if asmStt != "SIM" or asmStt != "NAO":
    asmStt = input("Informe somente sim ou não \n").upper()

if idade > 60:
    paciente = ("EM RISCO")
elif asmStt == ("SIM"):
    paciente = ("EM RISCO")
elif idade < 15:
    paciente = ("EM RISCO")
else:
    paciente = ("Normal, continua na fila").upper()
print (paciente)
