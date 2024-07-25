import mysql.connector

conexao = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = 'vitor',
    database = 'bdcrud.py',

)
cursor = conexao.cursor()

#create
def add_produto(nome_produto, valor):
    cursor = conexao.cursor()

    nome_produto = input('Digite o nonme do produto: ')
    valor = input(f'digite o valor do {nome_produto}: ')
    comando = (f'INSERT INTO vendas (nome_produto, valor) VALUES (?, ?)' , (nome_produto, valor))
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    print('Produto cadastrado com sucesso!!')


#read
def read_produto():
    cursor = conexao.cursor()

    comando = f'SELECT * FROM vendas;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conexao.close()
    print('produtos: ')
    for produtos in resultado:
        print(resultado)
    print()

#update
def update_produtos(nome_produto):
    cursor = conexao.cursor()

    produto_find = input('Digite o nome do produto que será atualizado: ')
    if(produto_find == nome_produto):
        novo_valor = input(f'Digite o novo valor do(a) {produto_find}: ')
        comando = f'UPDATE vendas SET valor = {novo_valor} WHERE nome_produto = "{produto_find}"'

    else:
        ('produto não encontrado')

    cursor.execute(comando)
    conexao.commit()
    conexao.close()

#rever o código


#delete
def deleatar_produtos():
    cursor = conexao.cursor()

    delete_produtos = input('Qual produto deseja deletar? ')
    comando = f'DELETE FROM vendas WHERE nome_produto = "{delete_produtos}"'

    cursor.execute(comando)
    conexao.commit()
    conexao.close()

cursor.close()
conexao.close()

