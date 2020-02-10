from execoes import LanceInvalido


class Usuario:

    def __init__(self, nome,carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome
    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self,leilao,valor):
        if not self._valor_e_valirdo(valor):
            raise LanceInvalido("Valor Maior que o da carteira")
        else:
            lance = Lance(self,valor)
            leilao.propoe(lance)
            self.__carteira -= valor

    def _valor_e_valirdo(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def propoe(self, lance:Lance):
        if self.lance_e_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return  True
        raise LanceInvalido("O Usuario não pode dar 2 lances seguidos")

    def valor_maior_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        raise LanceInvalido("O Valor do Lance deve ser maior que o anterior!")

    def lance_e_valido(self,lance):
        return not self._tem_lances() or (self._usuarios_diferentes(lance)
                                          and self.valor_maior_lance_anterior(lance))


