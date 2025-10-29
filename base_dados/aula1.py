# https://www.techonthenet.com/sqlite/index.php
# https://www.sqlite.org/doclist.html
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL - INSERT SELECT UPDATE DELETE

# CUIDADO: fazedo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name= "{TABLE_NAME}"'
)
connection.commit()

# Cria tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weigth REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injetcion
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weigth) '
    'VALUES '
    '(?, ?)'
)
# cursor.execute(sql, ['joana', 4])
cursor.executemany(sql, [['joana', 4], ['allan', 5]])
connection.commit()
print(sql)

cursor.close()
connection.close()
