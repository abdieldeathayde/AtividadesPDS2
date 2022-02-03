import sqlite3

conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes (''id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Pedro de Assis", 80.5)')

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)
    
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    indice, nome, peso = linha
    
    print(indice, nome, peso)
    
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria Conceição', 30.5 ))
conexao.commit()

cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None,'nome': 'Joao Pedro', 'peso':61})
conexao.commit()

#alterando dados:
cursor.execute('UPDATE clientes SET nome=? WHERE id=:id',('Maria', 1))
conexao.commit()

#deletando dados:
cursor.execute('UPDATE clientes SET nome=? WHERE id=:id', ('Maria',1))
conexao.commit()

#consultando dados; não funcionou pra mim

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 150.00})
conexao.commit()

cursor.close()
conexao.close()