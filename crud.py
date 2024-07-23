import mysql.connector

conexao = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    password = 'vitor',
    database = 'bdcrud.py',

)

#create
cursor = conexao.cursor()
nome_produto = input('Digite o nonme do produto: ')
valor = input(f'digite o valor do {nome_produto}: ')

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

#read

comando = f'SELECT * FROM vendas;'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)


cursor.close()
conexao.close()

