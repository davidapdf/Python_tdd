from dominio import Usuario,Lance,Leilao,Avaliador

david = Usuario("David")
Ana = Usuario("Ana")

lance_david = Lance(david,200)
lance_ana = Lance(Ana,120)

leilao = Leilao("Bicicleta")

leilao.lances.append(lance_ana)
leilao.lances.append(lance_david)

for lance in leilao.lances:
    print('O Usuario: {} fez o lance de {}:'.format(lance.usuario.nome,lance.valor))

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')


