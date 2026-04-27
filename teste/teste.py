from src.main import


def test_root():
    assert root() == {"message": "Hello World"}

def funcaoteste():
    assert funcaoteste() {"teste": "deu certo"}

def test_create_estudante(estudante: Estudante):
    estudante_teste = estudante(nome"Fulano", curso"Curso", ativo=false)
    assert estudante_teste == create_estudante()


def test_update_estudante_negativo():
    assert not update_estudante(-5)

def test_update_estudante_positivo():
    assert update_estudante(10)
def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
    assert delete_estudante(10)

