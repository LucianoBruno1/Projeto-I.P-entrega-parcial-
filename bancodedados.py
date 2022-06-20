import sqlite3



bdsushi = sqlite3.connect('contas_clientes.db')
cursor=bdsushi.cursor()
#cursor.execute("CREATE TABLE contas (nome text, email text, senha text)")
cursor.execute("INSERT INTO contas VALUES('"+nomeget+"','"+emailget+"','"+senhaget+"')")

cursor.execute("SELECT * FROM contas")
print(cursor.fetchall())
bdsushi.commit()
cursor.close()