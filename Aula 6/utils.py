from models import Pessoas

def insere_pessoa():
    pessoa = Pessoas(nome='Erik', idade=27)
    pessoa.salvar()
    # db_session.add(pessoa)


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Erik').first()
    pessoa.nome = 'Felipe'
    pessoa.salvar()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.excluir()

if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
