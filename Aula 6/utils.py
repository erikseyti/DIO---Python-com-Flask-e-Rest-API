from models import Pessoas

# insere dados na tabela pessoa
def insere_pessoa():
    """
    Insere dados na tabela pessoa.
    """
    pessoa = Pessoas(nome='Rafael', idade=27)
    pessoa.salvar()
    # db_session.add(pessoa)

# realiza uma consulta na tabela pessoa
def consulta_pessoas():
    """
    Reliza uma consulta na tabela pessoa.
    """
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

# altera dados na tabela pessoa
def altera_pessoa():
    """
    Altera dados na tabela pessoa
    """
    pessoa = Pessoas.query.filter_by(nome='Erik').first()
    pessoa.nome = 'Felipe'
    pessoa.salvar()

# exclui dados na tabela pessoa
def exclui_pessoa():
    """
    Exclui dados na tabela pessoa
    """
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.excluir()

if __name__ == '__main__':
    insere_pessoa()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()
