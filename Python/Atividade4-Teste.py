QTD_notas = int(input("Quantas notas voce tem: ")) 

soma_notas = 0  

# vai verificar a qi
for i in range(QTD_notas):
    nota  = float(input(f"Digite a  {i+1} nota"))
    soma_notas += nota

    media_simples = soma_notas / QTD_notas

print(f"A sua media é: {media_simples}")
