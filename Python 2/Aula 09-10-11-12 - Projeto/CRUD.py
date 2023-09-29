# CRUD - CREATE - READ - UPDATE - DELETE

#importar SQLite3
import sqlite3

#criar conexão
try:
    con = sqlite3.connect(('cadastro_alunos.db'))
    print('Conexao com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

#Trabalhando com tabela de cursos ----------------------

#Criar cursos (CREATE - C)

def criar_cursos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, DURACAO, preco) VALUES(?,?,?)"
        cur.execute(query, i)


#Ver todos os cursos (Selecionar R)
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos') #Selecione tudo da tabela cursos
        linha = cur.fetchall()#Busca todas as linhas de uma consulta e retorna uma lista de tuplas

        for i in linha:
            lista.append(i)
    return lista


#Atualizar os Cursos (Update U)

def atualizar_cursos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.execute(query, i)

#atualizar_cursos(['Python', 'Duas Semanas', 50.0, 1])

#Deletar Cursos (Delete D)
def deletar_cursos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id =?"
        cur.execute(query, i)


#lembrar de passar a ID dentro de uma lista, mesmo tendo um unico valor
#deletar_cursos([1])

#Trabalhando com tabela de Turmas ----------------------

#Criar turmas (Inserir)
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)


#Ver todas as turmas (Read R)
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#Atualizar as Turmas (Update U)
def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Turmas SET nome=?, curso_nome=?, data_inicio=? WHERE id=?"
        cur.execute(query, i)


#Deletar Turmas (DELETE D)
def deletar_turmas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query,i)


#Tabela Alunos ------------------------------

# Criar Alunos (CREATE C)
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, CPF, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Ver todos os alunos (Read R)
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


# Atualizar os Alunos (Update U)
def atualizar_alunos(i):
    with con:
        cur = con.cursor()
        query = "UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, CPF=?, turma_nome=? WHERE id=?"
        cur.execute(query, i)


# Deletar Alunos (DELETE D)
def deletar_alunos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query, i)
