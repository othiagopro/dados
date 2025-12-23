import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute(
#     """
#         SELECT * FROM estudantes    
#     """
# )


cursor.execute(
    """
        SELECT * FROM estudantes
    """
)

# disciplinas = cursor.fetchall()

# for disciplina in disciplinas:
#     print(disciplina)


conn.commit()

estudantes = cursor.fetchall()

for estudante in estudantes:
    print(estudantes)

conn.close()
