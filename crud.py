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
    comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
    cursor.execute(comando, (nome_produto, valor))
    conexao.commit()
    print('Produto cadastrado com sucesso!!')


#read
def read_produto():
    comando = 'SELECT * FROM vendas;'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('Produtos: ')
    for produto in resultado:
        print(produto)
    print()

#update
def update_produtos(nome_produto, valor):
    comando = 'UPDATE vendas SET valor = %s WHERE nome_produto = %s'

    cursor.execute(comando, (valor, nome_produto))
    conexao.commit()
    print("Preço do produto atualizado com sucesso!\n")


#delete
def deleatar_produtos(nome_produto):
    comando = ('DELETE FROM vendas WHERE nome_produto = %s')

    cursor.execute(comando, (nome_produto,))
    conexao.commit()

def menu():
    print("Escolha uma opção: ")
    print("1. Cadastrar um produto: ")
    print("2. Imprimir produtos: ")
    print("3. Atualizar um produto: ")
    print("4. Deletar um produto: ")
    print("5. Fechar Menu ")

def main():
    while True:
        menu()
        escolha = input('Escolha uma opção de 1-5:\n')
        
        match escolha:
            case '1':
                 nome_produto = input('Digite o nome do produto: ')
                 valor = int(input(f'Digite o valor do {nome_produto}: '))
                 add_produto(nome_produto, valor)
            
            case '2':
                read_produto()
            
            case '3':
                nome_produto = input('Digite o nome do produto que deseja mudar o valor: ')
                valor = int(input('Digite o novo valor: '))
                update_produtos(nome_produto, valor)

            case '4':
                nome_produto = input('Digite o nome do produto irá ser deletado: ')
                deleatar_produtos(nome_produto)

            case '5':
                print('fechando...')
                break

            case _:
                print('Opção Invalida,  tente um numero de 1 a 5')

main()
cursor.close()
conexao.close()

