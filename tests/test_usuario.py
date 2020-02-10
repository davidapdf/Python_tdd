from dominio import Usuario, Leilao
import pytest

from execoes import LanceInvalido


@pytest.fixture
def david():
    return Usuario("David",100)
@pytest.fixture
def leilao():
    return Leilao("Celular")

def test_deve_subtrarir_valor_da_carteira_do_usuario_quando_este_propor_um_lance(david,leilao):
    david.propoe_lance(leilao,50.0)

    assert david.carteira == 50.0

def test_deve_permiter_fazer_um_lance_quando_o_valor_e_menor_que_a_carteira(david,leilao):
    david.propoe_lance(leilao,50)

    assert david.carteira ==50
def test_deve_permitir_propor_lance_quando_valor_e_igual_ao_valor_da_carteira(david,leilao):
    david.propoe_lance(leilao,100)

    assert david.carteira == 0
def test_onde_nao_deve_permitir_lance_com_valor_maior_do_que_na_carteira(david,leilao):
    with pytest.raises(LanceInvalido):
        david.propoe_lance(leilao,200)

