# importando módulos do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from CRUD import *
from tkcalendar import Calendar, DateEntry
from datetime import date

#cores
# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co66 = "#003452"   # azul escuro
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde


#Criando a Janela

janela = Tk()
janela.title("Programa da Ju")
janela.geometry('850x620')
janela.configure(background=co1)
#janela.resizable(width=False, height=False) # Para que a altura e largura não possam ser alteradas

style = Style(janela)
style.theme_use("clam")
#janela.mainloop() # executar e depois deixar como comentário

##1_#Criando frames da janela, separar...

frame_logo = Frame(janela, width=850, height=52, bg=co6) #cria o frame da janela
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW) #adiciona o frame a janela
        #sticky é posiçao que vai ficar atraves de coordenadas           #padx largura da borda externa
ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680) #ipadxlargura da borda interna
#Local aonde pode aleternar entre as abas
frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3,columnspan=1, ipadx=680)
#Local que vai ter a opção do por nome, preço e etc...
frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=100, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


#Trabalhando no frame logo ----------------------------------
#importando pillow - aqui ou lá em cima
from PIL import ImageTk, Image

app_logo = Image.open('logo.png') #abrir a imagem
app_logo = app_logo.resize((50,50)) #Redimensionar o tamanho da imagem
app_logo = ImageTk.PhotoImage(app_logo) # Formatar para que possa ser usado dentro do tkinter
app_LG = Label(frame_logo, image=app_logo, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 25 bold'), bg=co6, fg=co1)
app_LG.place(x=0, y=0)

#part3: Função de cadastrar alunos -------------------
def cadastro():
    """PARTE FINAL CRIANDO FUNÇÃO PARA OS BOTÕES E VINCULANDO AO BANCO DE DADOS"""
    def novo_aluno():
        #variáveis globais para escolher imagem
        global imagem, imagem_string, l_imagem

        #1 fazer get de todas as entradas e criar variaveis com seus nomes
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_telefone.get()
        sexo = c_sexo.get()
        imagemtxt = imagem_string
        data = data_inicio.get()
        cpf = e_cpf.get()
        turma = c_turma.get()

        # .get() funçao parar pegar o que tem digitado no campo

        lista_novo_aluno = [nome, email, telefone, sexo, imagemtxt, data, cpf, turma]

        # para veririficar se tem algum valor vazio
        for i in lista_novo_aluno:
            if i == "":  # campo vazio
                messagebox.showerror("Erro", "Preencha todos os campos")
                return

        # inserindo os dados função CRUD de criar ALUNO
        criar_alunos(lista_novo_aluno)

        # mostrando mensagem de sucesso

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        #para limpar cada um dos campos
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        c_sexo.delete(0, END)
        data_inicio.delete(0, END)
        e_cpf.delete(0, END)
        c_turma.delete(0, END)


        # Mostrando os valores na tabela
        mostrar_alunos()  # para atualizar tabela alunos
        #cadastro()  #Para atualizar a tela

    def update_aluno():
        #Trazer vaiáveis globais pra cá
        global imagem, imagem_string, l_imagem

        try:
            itens_tabela = tabela_aluno.focus()
            tabela_dicionario = tabela_aluno.item(itens_tabela)
            lista_tabela = tabela_dicionario['values']

            valor_id = lista_tabela[0]

            #limpando os campos de entrada (sem o imagem)
            e_nome.delete(0, END)
            e_email.delete(0, END)
            e_telefone.delete(0, END)
            c_sexo.delete(0, END)
            data_inicio.delete(0, END)
            e_cpf.delete(0, END)
            c_turma.delete(0, END)

            #Inserindo os valores nos campos de entrada
            e_nome.insert(0, lista_tabela[1])
            e_email.insert(0, lista_tabela[2])
            e_telefone.insert(0, lista_tabela[3])
            c_sexo.insert(0, lista_tabela[4])

            data_inicio.insert(0, lista_tabela[6])
            e_cpf.insert(0, lista_tabela[7])
            c_turma.insert(0, lista_tabela[8])

            #para exibir imagem ao clicar no botão
            imagem = lista_tabela[5]
            imagem_string = imagem

            #abrindo a imagem (copiei o mesmo comando)
            imagem = Image.open(imagem)
            imagem = imagem.resize((130, 130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
            l_imagem.place(x=300, y=10)

            def update():
                #copiar e colar função novo aluno #Lembrar de mudar função CRUD para atualizar alunos

                #1 fazer get de todas as entradas e criar variaveis com seus nomes
                nome = e_nome.get()
                email = e_email.get()
                telefone = e_telefone.get()
                sexo = c_sexo.get()
                imagemtxt = imagem_string
                data = data_inicio.get()
                cpf = e_cpf.get()
                turma = c_turma.get()

                # .get() funçao parar pegar o que tem digitado no campo

                lista_novo_aluno = [nome, email, telefone, sexo, imagemtxt, data, cpf, turma, valor_id]

                # para veririficar se tem algum valor vazio
                for i in lista_novo_aluno:
                    if i == "":  # campo vazio
                        messagebox.showerror("Erro", "Preencha todos os campos")
                        return

                # atualizando os dados função CRUD de atualizar ALUNO
                atualizar_alunos(lista_novo_aluno)

                # mostrando mensagem de sucesso

                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                #para limpar cada um dos campos
                e_nome.delete(0, END)
                e_email.delete(0, END)
                e_telefone.delete(0, END)
                c_sexo.delete(0, END)
                data_inicio.delete(0, END)
                e_cpf.delete(0, END)
                c_turma.delete(0, END)


                # Mostrando os valores na tabela
                mostrar_alunos()  # para atualizar tabela alunos
                #cadastro()#Para atualizar a tela


                #destruindo botão salvar_update após salvar
                botao_salvar_update.destroy()

            #COPIAR E COLAR BOTÃO SALVAR
            botao_salvar_update = Button(frame_detalhes, command=update, anchor=CENTER, text='SALVAR ATUALIZAÇÃO', width=8,overrelief=RIDGE, font=('Yvi 7 bold'), bg=co3, fg=co1)
            botao_salvar_update.place(x=727,y=130)  # place é o gerenciador de geometria, organiza widgets colocando em uma posiçao especifica

            #após tudo isso conectar funçao update_aluno ao botão atualizar

        except IndexError:
            messagebox.showerror('Erro', 'Seleciona um dos alunos na tabela')

    def apagar_aluno():
        try:
            itens_tabela = tabela_aluno.focus()
            tabela_dicionario = tabela_aluno.item(itens_tabela)
            lista_tabela = tabela_dicionario['values']

            valor_id = lista_tabela[0]

            #deletar os dados no banco de dados
            deletar_alunos([valor_id])

            #Mostrando a mensagem de sucesso
            messagebox.showinfo("Sucesso", "Aluno deletado com sucesso")

            #atualizando valores na tabela
            mostrar_alunos()

        except IndexError:
            messagebox.showerror("Erro", "Seleciona um aluno na tabela")



    """Criando campos de entrada(Copiar do que já foi feito em adicionar)"""
    #1 nome e campo
    local_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_nome.place(x=4, y=10)  # Para configurar e escolher o título do campo de preenchimento
    e_nome = Entry(frame_detalhes, width=34, justify='left', relief='solid')  # justify é o local por onde a digitação do usuário irá aparecer no campo
    #renomear para e_nome de entrada
    e_nome.place(x=7, y=40)  # para configurar o campo de preenchimento

    #2 email e campo
    local_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_email.place(x=4, y=70)  # Para configurar e escolher o título do campo de preenchimento
    e_email = Entry(frame_detalhes, width=34, justify='left', relief='solid')  # justify é o local por onde a digitação do usuário irá aparecer no campo
    #renomear para e_nome de entrada
    e_email.place(x=7, y=100)  # para configurar o campo de preenchimento

    #3Telefone
    local_telefone = Label(frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_telefone.place(x=4, y=130)  # Para configurar e escolher o título do campo de preenchimento
    e_telefone = Entry(frame_detalhes, width=15, justify='left', relief='solid')  # justify é o local por onde a digitação do usuário irá aparecer no campo
    #renomear para e_nome de entrada
    e_telefone.place(x=7, y=160)  # para configurar o campo de preenchimento

    #4Sexo e combobox
    local_sexo = Label(frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_sexo.place(x=170, y=130) #Para configurar e escolher o título do campo de preenchimento
    #Vamos criar a combo box, nesse caso deixa a lista com os sexos disponíveis
    sexos = ['Masculino', 'Feminino']
    #ele usou for i in cursos:
                #curs.append(i) mas achei desnecessaŕio

    #4.1Criar a combo box, que é aquele menu de opções
    c_sexo = ttk.Combobox(frame_detalhes, width=13, font=('Ivy 8 bold'))
    c_sexo['values'] = (sexos)
    c_sexo.place(x=173, y=160)

    #5Botão Carregar Imagem
    #Nessa parte além do botão tem a imagem para carregar, para isso vamos criar uma função que carrega as imagens

    global imagem, imagem_string, l_imagem

    def escolher_imagem():
        global imagem, imagem_string, l_imagem

        imagem = fd.askopenfilename() # é a função que me permite escolher um arquivo dentro das minhas pastas
        imagem_string = imagem # variavel que vai salvar o caminho onde a imagem se encontra

        # abrindo e configurando a imagem
        imagem = Image.open(imagem)
        imagem = imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=co1, fg=co4)
        l_imagem.place(x=300, y=10)

        botao_carregar_imagem['text'] = 'TROCAR DE FOTO'



    botao_carregar_imagem = Button(frame_detalhes,command=escolher_imagem, compound=CENTER, anchor=CENTER, text='CARREGAR FOTO', width=20, overrelief=RIDGE, font=('Ivy 7'),bg=co1, fg=co0)
    botao_carregar_imagem.place(x=300, y=160)

    #6Data de Nascimento
    lt_data_nascimento = Label(frame_detalhes, text="Data de Nascimento *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    lt_data_nascimento.place(x=460, y=10)
    #instalar tk calendar - pip install tkcalendar
    #importar lá em cima
    #from tkcalendar import Calendar, DataEntry
    #from datetime import date
    data_inicio = DateEntry(frame_detalhes, width=15, background='darkblue', foreground='white', borderwodth=2, year=2023)
    data_inicio.place(x=463,y=40)


    #7 CPF e CAMPO
    local_cpf = Label(frame_detalhes, text="CPF *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_cpf.place(x=460, y=70)  # Para configurar e escolher o título do campo de preenchimento
    e_cpf = Entry(frame_detalhes, width=17, justify='left', relief='solid')  # justify é o local por onde a digitação do usuário irá aparecer no campo
    e_cpf.place(x=463, y=100)  # para configurar o campo de preenchimento

    #8 Curso e Campo_Combobox
    local_curso = Label(frame_detalhes, text="Cursos *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_curso.place(x=460, y=130) #Para configurar e escolher o título do campo de preenchimento
    #Vamos criar a combo box, nesse caso como a lista não esta vinculada, apenas simular cursos
    turmas = ver_turmas()
    turma = []

    for i in turmas:
        turma.append(i[1]) # para pegar apenas os itens da coluna turma

    #8.1Criar a combo box, que é aquele menu de opções
    c_turma = ttk.Combobox(frame_detalhes, width=17, font=('Ivy 8 bold'))
    c_turma['values'] = (turma)
    c_turma.place(x=463, y=160)

    """AGORA CRIAR A LINHA SEPARATÓRIA"""
    #linha para separar cadastro aluno de procurar aluno
    #vai criar uma linha preta
    d_linha= Label(frame_detalhes, relief=GROOVE, width=3, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    d_linha.place(x=624, y=10)
    #para criar um efeito sombreado
    d_linha= Label(frame_detalhes, relief=GROOVE, width=3, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    d_linha.place(x=623, y=10)

    """CRIAÇÃO DAS OPÇÕES DE BUSCA DE ALUNO"""
    # 1Procurar aluno
    local_procurar = Label(frame_detalhes, text="Procurar Aluno [Nome] *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_procurar.place(x=644, y=10)  # Para configurar e escolher o título do campo de preenchimento
    e_procurar = Entry(frame_detalhes, width=12, justify='left', relief='solid')  # justify é o local por onde a digitação do usuário irá aparecer no campo
    # renomear para e_nome de entrada
    e_procurar.place(x=647, y=40)  # para configurar o campo de preenchimento

    #2Botão Procurar aluno
    botao_procurar = Button(frame_detalhes, anchor=CENTER, text='Procurar', width=4, height=1, overrelief=RIDGE, font=('Yvi 6 bold'),bg=co1, fg=co0)
    botao_procurar.place(x=755, y=40)

    #3Criação do botões (SALVAR/ATUALIZAR/CARREGAR) - Abaixo do procurar
    botao_salvar = Button(frame_detalhes,command=novo_aluno, anchor=CENTER, text='SALVAR', width=8, overrelief=RIDGE, font=('Yvi 7 bold'),bg=co3, fg=co1)
    botao_salvar.place(x=647, y=110)  # place é o gerenciador de geometria, organiza widgets colocando em uma posiçao especifica

    botao_atualizar = Button(frame_detalhes,command=update_aluno, anchor=CENTER, text='ATUALIZAR', width=8, overrelief=RIDGE,font=('Yvi 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=647, y=140)

    botao_deletar = Button(frame_detalhes,command=apagar_aluno, anchor=CENTER, text='DELETAR', width=8, overrelief=RIDGE,font=('Yvi 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=647, y=170)

    # 4Criação do botão VER
    botao_deletar = Button(frame_detalhes, anchor=CENTER, text='VER', width=8, overrelief=RIDGE,font=('Yvi 7 bold'), bg=co1, fg=co0)
    botao_deletar.place(x=735, y=170)

    """TABELA DE ALUNOS"""
    #criação de funçao para tabela
    def mostrar_alunos():
        titulo_cursos = Label(frame_tabela, text="Tabela de Turmas", height=1, pady=0, relief="flat", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4)
        titulo_cursos.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Criando uma tabela com barra de rolagem dupla
        # como o cabeçalho não terá um unico titulo, usar lista...
        cabecalho = ['ID', 'Nome', 'Email', 'Telefone', 'Sexo', 'Imagem', 'Data de nascimento', 'CPF', "Turma"]

        df_list = ver_alunos()

        global tabela_aluno
        # funçao para criar tabel
        tabela_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=cabecalho, show="headings")

        # barra de rolagem VERTICAL
        brV = ttk.Scrollbar(frame_tabela, orient="vertical", command=tabela_aluno.yview())
        # barra de rolagem HORIZONTAL
        brH = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tabela_aluno.xview())

        tabela_aluno.configure(yscrollcommand=brV.set, xscrollcommand=brH.set)

        tabela_aluno.grid(column=0, row=1, sticky='nsew')
        brV.grid(column=1, row=1, sticky='ns')
        brH.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd = ["s", "s", "e", "e","s", "s","center", "center", "e"] #orientação do conteudo da coluna
        h = [30, 150, 150, 70,70, 70, 80, 80, 80] #largura da coluna do conteudo
        n = 0

        for col in cabecalho:
            tabela_aluno.heading(col, text=col.title(), anchor=NW)
            # Ajustar a largura da coluna com o tamanho da string do cabeçalho
            tabela_aluno.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in df_list:
            tabela_aluno.insert('', 'end', values=item)

    mostrar_alunos()




#part4: Função de cadastrar Cursos e Turmas ------------
def adicionar():
    #parte2 - CRIAÇÃO DE FRAME PARA A TABELA CURSO E TURMA DENTRO DO FRAME TABELA
    frame_tabela_curso = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

#criar esse frame depois
    frame_tabela_linha = Frame(frame_tabela, width=30, height=200, bg=co1)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma = Frame(frame_tabela, width=300, height=200, bg=co1)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    #Detalhes do CURSO ---------------

    #PARTE FINAL - FUNÇÕES PARA OS BOTÕES
    def novo_curso():
        nome = e_nomecurso.get()
        duracao = e_duracao.get()
        preco = e_preco.get()
        #.get() funçao parar pegar o que tem digitado no campo

        lista_novo_curso = [nome, duracao, preco]

        #para veririficar se tem algum valor vazio
        for i in lista_novo_curso:
            if i == "": #campo vazio
                messagebox.showerror("Erro", "Preencha todos os campos")
                return

        #inserindo os dados #função crud
        criar_cursos(lista_novo_curso)

        # mostrando mensagem de sucesso

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_nomecurso.delete(0, END)
        e_duracao.delete(0, END)
        e_preco.delete(0, END)

        #Mostrando os valores na tabela
        mostrar_cursos() # para atualizar tabela cursos
        adicionar() # para atualizar a página adicionar, para aparecer o novo curso em todos os frames(turmas)

    #PARTE FINAL - FUNÇÃO PARA ATUALIZAR CURSO
    def update_curso():#Copiar a função novo_curso() - já tem atualizar cursos no crud
        try:
            itens_tabela = tabela_curso.focus() #comando que vai me permitir manipular dados da tabela
            tabela_dicionario = tabela_curso.item(itens_tabela) # codigo para transformar as informações salvas na variavél itens_tabela em um dicionário
            lista_tabela = tabela_dicionario['values'] # para pegar apenas os valores

            valor_id = lista_tabela[0] # para pegar o primeiro valor da lista, que é o ID

            #copiar valores das variaveis nome, duracao e preco
            #Inserindo o valor nas entradas da tabela
            e_nomecurso.insert(0, lista_tabela[1])
            e_duracao.insert(0, lista_tabela[2])
            e_preco.insert(0, lista_tabela[3])

            #Criar função atualizar e jogar tudo abaixo para dentro dela
            def atualizar(): #lembrar de adicionar o valor_id na lista abaixo e mudar o nome para atualizar_curso

                nome = e_nomecurso.get()
                duracao = e_duracao.get()
                preco = e_preco.get()#.get() funçao parar pegar o que tem digitado no campo

                lista_novo_curso = [nome, duracao, preco, valor_id]#add o valor_id no final

                #para veririficar se tem algum valor vazio
                for i in lista_novo_curso:
                    if i == "": #campo vazio
                        messagebox.showerror("Erro", "Preencha todos os campos")
                        return

                #inserindo os dados - mudar o nome para a funçao CRUD atualizar_cursos
                atualizar_cursos(lista_novo_curso)

                # mostrando mensagem de sucesso

                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

                e_nomecurso.delete(0, END)
                e_duracao.delete(0, END)
                e_preco.delete(0, END)

                #Mostrando os valores na tabel
                mostrar_cursos()

                #criar primeiro o botão e depois fazer o que tá abaixo
                #destruindo botão salvar após salvar atualização os dados
                botao_salvar_atualizacao.destroy()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos na tabela')

        #Copiar e colocar um botão aqui
        #malicia que eu fiz, try e except
        try:
            botao_salvar_atualizacao = Button(frame_detalhes, command=atualizar, anchor=CENTER, text='Salvar Atualização', width=14,overrelief=RIDGE, font=('Yvi 7 bold'), bg=co3, fg=co1)
            botao_salvar_atualizacao.place(x=227,y=130)  # place é o gerenciador de geometria, organiza widgets colocando em uma posiçao especifica
        except:
            pass


    #FUNÇÃO PARA DELETAR CURSO
    def delete_curso():
        try:
            itens_tabela = tabela_curso.focus() #comando que vai me permitir manipular dados da tabela
            tabela_dicionario = tabela_curso.item(itens_tabela) # codigo para transformar as informações salvas na variavél itens_tabela em um dicionário
            lista_tabela = tabela_dicionario['values'] # para pegar apenas os valores

            valor_id = lista_tabela[0] # para pegar o primeiro valor da lista, que é o ID

            # chamar função deletar_curso do CRUD, lembrar de colocar o valor_id como lista
            deletar_cursos([valor_id])

            #Mostrar mensagem de cursos deletado com sucessso
            messagebox.showinfo('Sucesso', 'Curso deletado com sucesso!')


            #após isso chamar a função mostrar curso para atualizar a tela
            mostrar_cursos()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione o curso que dejesa deletar')

    local_nome = Label(frame_detalhes, text="Nome do curso *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_nome.place(x=4, y=10) #Para configurar e escolher o título do campo de preenchimento
    e_nomecurso = Entry(frame_detalhes, width=35, justify='left', relief='solid', bg=co3)#justify é o local por a digitação do usuário irá aparecer no campo
    e_nomecurso.place(x=7, y=40)#para configurar o campo de preenchimento

    local_duracao = Label(frame_detalhes, text="Duração *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_duracao.place(x=4, y=70) #Para configurar e escolher o título do campo de preenchimento
    e_duracao = Entry(frame_detalhes, width=20, justify='right', relief='solid') #relief é o estilo do campo
    e_duracao.place(x=7, y=100)#para configurar o campo de preenchimento

    local_preco = Label(frame_detalhes, text="Preço *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_preco.place(x=4, y=130) #Para configurar e escolher o título do campo de preenchimento
    e_preco = Entry(frame_detalhes, width=10, justify='right', relief='sunken')
    e_preco.place(x=7, y=160)#para configurar o campo de preenchimento

#Criação do botões (SALVAR/ATUALIZAR/CARREGAR) - Lado dos cursos
    botao_salvar = Button(frame_detalhes,command=novo_curso, anchor=CENTER, text='SALVAR', width=8, overrelief=RIDGE, font=('Yvi 7 bold'), bg=co3, fg=co1)
    botao_salvar.place(x=107, y=160)#place é o gerenciador de geometria, organiza widgets colocando em uma posiçao especifica

    botao_atualizar = Button(frame_detalhes,command=update_curso, anchor=CENTER, text='ATUALIZAR', width=8, overrelief=RIDGE, font=('Yvi 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=187, y=160)

    botao_deletar = Button(frame_detalhes,command=delete_curso, anchor=CENTER, text='DELETAR', width=8, overrelief=RIDGE, font=('Yvi 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=267, y=160)

# Criação da Tabela dos cursos #lembrar da identação
    def mostrar_cursos():
        titulo_cursos = Label(frame_tabela_curso, text="Tabela de Cursos", height=1, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
        titulo_cursos.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #Criando uma tabela com barra de rolagem dupla
        #como o cabeçalho não terá um unico titulo, usar lista...
        cabecalho = ['ID', 'Curso', 'Duração', 'Preço']

        df_list = ver_cursos() #parte2 - depois de importar o crud pra cá
                #[] - uma lista primeira
        global tabela_curso
                       #funçao para criar tabel
        tabela_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended", columns=cabecalho, show="headings")

        #barra de rolagem VERTICAL
        brV = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tabela_curso.yview())
        #barra de rolagem HORIZONTAL
        brH = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tabela_curso.xview())

        tabela_curso.configure(yscrollcommand=brV.set, xscrollcommand=brH.set)

        tabela_curso.grid(column=0, row=1, sticky='nsew')
        brV.grid(column=1, row=1, sticky='ns')
        brH.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd = ["s", "s", "e", "e"]
        h = [30, 150, 80, 60]
        n=0 # Variavel de controle - irá pegar o primeiro item da lista, e com a contagem irá somar +1

        for col in cabecalho:
            tabela_curso.heading(col, text=col.title(), anchor=NW)
            #Ajustar a largura da coluna com o tamanho da string do cabeçalho
            tabela_curso.column(col, width=h[n], anchor=hd[n])

            n+=1

        for item in df_list: #Parte do conteudo da tabela
            tabela_curso.insert('', 'end', values=item) # para inserir os dados na tabela
                        # index = o primeiro é o parent, n precisa colocar nada. index= aonde que ele vai ficar, qual linha que o item vai, values = os valores que irão aparecer
    mostrar_cursos()

    #linha para separar cursos de turmas
    #vai criar uma linha preta
    d_linha= Label(frame_detalhes, relief=GROOVE, width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    d_linha.place(x=374, y=10)
    #para criar um efeito sombreado
    d_linha= Label(frame_detalhes, relief=GROOVE, width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    d_linha.place(x=373, y=10)

    #Linha separatória da tabela
    t_linha= Label(frame_tabela, relief=GROOVE, width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    t_linha.place(x=374, y=10)
    t_linha= Label(frame_tabela, relief=GROOVE, width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    t_linha.place(x=373, y=10)

    #Detalhes da TURMAS --------------------------------

    # PARTE FINAL - FUNÇÕES PARA OS BOTÕES
    def nova_turma():
        nome = e_nometurma.get()
        curso = c_curso.get()
        data = data_inicio.get()
        # .get() funçao parar pegar o que tem digitado no campo

        lista_nova_turma = [nome, curso, data]

        # para veririficar se tem algum valor vazio
        for i in lista_nova_turma:
            if i == "":  # campo vazio
                messagebox.showerror("Erro", "Preencha todos os campos")
                return

        # inserindo os dados
        criar_turma(lista_nova_turma)

        # mostrando mensagem de sucesso

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_nometurma.delete(0, END)
        c_curso.delete(0, END)
        data_inicio.delete(0, END)

        # Mostrando os valores na tabel
        mostrar_turmas()


    def update_turma():
        try:
            itens_tabela = tabela_turma.focus() #comando que vai me permitir manipular dados da tabela
            tabela_dicionario = tabela_turma.item(itens_tabela) # codigo para transformar as informações salvas na variavél itens_tabela em um dicionário
            lista_tabela = tabela_dicionario['values'] # para pegar apenas os valores

            valor_id = lista_tabela[0] # para pegar o primeiro valor da lista, que é o ID

            #copiar valores das variaveis nome, duracao e preco
            #Inserindo o valor nas entradas da tabela
            e_nometurma.insert(0, lista_tabela[1])
            c_curso.insert(0, lista_tabela[2])
            data_inicio.insert(0, lista_tabela[3])

            def atualizar():
                nome = e_nometurma.get()
                curso = c_curso.get()
                data = data_inicio.get()
                # .get() funçao parar pegar o que tem digitado no campo

                lista_nova_turma = [nome, curso, data, valor_id]

                # para veririficar se tem algum valor vazio
                for i in lista_nova_turma:
                    if i == "":  # campo vazio
                        messagebox.showerror("Erro", "Preencha todos os campos")
                        return

                # inserindo os dados do CRUD atualizar_turmas
                atualizar_turmas(lista_nova_turma)

                # mostrando mensagem de sucesso

                messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

                e_nometurma.delete(0, END)
                c_curso.delete(0, END)
                data_inicio.delete(0, END)

                # Mostrando os valores na tabela
                mostrar_turmas()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos na tabela')

        #Copiar e colocar um botão aqui
        #malicia que eu fiz, try e except
        try:
            botao_salvar_atualizacao = Button(frame_detalhes, command=atualizar, anchor=CENTER, text='Salvar Atualização', width=14,overrelief=RIDGE, font=('Yvi 7 bold'), bg=co3, fg=co1)
            botao_salvar_atualizacao.place(x=527,y=130)  # place é o gerenciador de geometria, organiza widgets colocando em uma posiçao especifica
        except:
            pass


    def delete_turma():
        try:
            itens_tabela = tabela_turma.focus() #comando que vai me permitir manipular dados da tabela
            tabela_dicionario = tabela_turma.item(itens_tabela) # codigo para transformar as informações salvas na variavél itens_tabela em um dicionário
            lista_tabela = tabela_dicionario['values'] # para pegar apenas os valores

            valor_id = lista_tabela[0] # para pegar o primeiro valor da lista, que é o ID

            # chamar função deletar_curso do CRUD, lembrar de colocar o valor_id como lista
            deletar_turmas([valor_id])

            #Mostrar mensagem de cursos deletado com sucessso
            messagebox.showinfo('Sucesso', 'Turma deletada com sucesso!')


            #após isso chamar a função mostrar turmas para atualizar a tabela
            mostrar_turmas()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione o curso que dejesa deletar')


    local_nome_turma = Label(frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_nome_turma.place(x=400, y=10) #Para configurar e escolher o título do campo de preenchimento
    e_nometurma = Entry(frame_detalhes, width=35, justify='left', relief='solid')#justify é o local por a digitação do usuário irá aparecer no campo
    e_nometurma.place(x=403, y=40)#para configurar o campo de preenchimento

    local_curso = Label(frame_detalhes, text="Curso *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    local_curso.place(x=400, y=70) #Para configurar e escolher o título do campo de preenchimento
    #Vamos criar a combo box, porém como ela ainda não está vinculada com o banco de dados, vamos criar uma lista de
    #cursos para simular
            #[python, java, power bi]
    cursos = ver_cursos() #para pegar a lista de curso completa - CRUD ver curso
    curso = []
    #ele usou
    for i in cursos:
        curso.append(i[1]) #Adicionar o número [1] que corresponde a posição do curso na lista cursos



    #Criar a combo box, que é aquele menu de opções
    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['values'] = (curso) # para pegar apenas os valores do item 1 da lista que correponde ao nome do curso
    c_curso.place(x=407, y=100)

    #Para criar data de início
    lt_data_inicio = Label(frame_detalhes, text="Data de Inicio *", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    lt_data_inicio.place(x=406, y=130)

    #instalar tk calendar - pip install tkcalendar
    #importar lá em cima
    #from tkcalendar import Calendar, DataEntry
    #from datetime import date
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwodth=2, year=2023)
    data_inicio.place(x=407,y=160)

    # Criação do botões (SALVAR/ATUALIZAR/CARREGAR) lado das turmas, copie o que já tinha feito
    botao_salvar = Button(frame_detalhes, command=nova_turma, anchor=CENTER, text='SALVAR', width=8, overrelief=RIDGE, font=('Yvi 7 bold'),bg=co3, fg=co1)
    botao_salvar.place(x=517,y=160)  # place é o gerenciador de geometria, organiza widgets colocando em uma posiçao especifica

    botao_atualizar = Button(frame_detalhes,command=update_turma, anchor=CENTER, text='ATUALIZAR', width=8, overrelief=RIDGE, font=('Yvi 7 bold'), bg=co6, fg=co1)
    botao_atualizar.place(x=597, y=160)

    botao_deletar = Button(frame_detalhes,command=delete_turma, anchor=CENTER, text='DELETAR', width=8, overrelief=RIDGE,font=('Yvi 7 bold'), bg=co7, fg=co1)
    botao_deletar.place(x=677, y=160)

#copiar a def mostrar cursos para criar a tabela das turmas
    def mostrar_turmas():
        titulo_cursos = Label(frame_tabela_turma, text="Tabela de Turmas", height=1, pady=0, relief="flat", anchor=NW,
                              font=('Ivy 10 bold'), bg=co1, fg=co4)
        titulo_cursos.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        # Criando uma tabela com barra de rolagem dupla
        # como o cabeçalho não terá um unico titulo, usar lista...
        cabecalho = ['ID', 'Noma da Turma', 'Curso', 'Início']

        df_list = ver_turmas() #part2 depois de importar CRUD
                #parte 1 [] lista vazia

        global tabela_turma
        # funçao para criar tabel
        tabela_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended", columns=cabecalho, show="headings")

        # barra de rolagem VERTICAL
        brV = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tabela_turma.yview())
        # barra de rolagem HORIZONTAL
        brH = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tabela_turma.xview())

        tabela_turma.configure(yscrollcommand=brV.set, xscrollcommand=brH.set)

        tabela_turma.grid(column=0, row=1, sticky='nsew')
        brV.grid(column=1, row=1, sticky='ns')
        brH.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd = ["s", "s", "s", "s"]
        h = [30, 130, 150, 80]
        n = 0

        for col in cabecalho:
            tabela_turma.heading(col, text=col.title(), anchor=NW)
            # Ajustar a largura da coluna com o tamanho da string do cabeçalho
            tabela_turma.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in df_list:
            tabela_turma.insert('', 'end', values=item)

    mostrar_turmas()

#part3: Função de Salvar  ------------
def salvar():
    print('Salvar')



# Funcao de control -------------------------------------

def control(i):
    #pass  - fazer primeiro
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():#cada detalhe preenchido na parte do frame detalhes
            widget.destroy() # comando para apagar o que tiver digitado nos campos

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        #CHAMANDO A FUNCAO
        cadastro()
    elif i == 'adicionar':
        for widget in frame_detalhes.winfo_children():  # cada detalhe preenchido na parte do frame detalhes
            widget.destroy()  # comando para apagar o que tiver digitado nos campos

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        # chamando a função
        adicionar()
    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():  # cada detalhe preenchido na parte do frame detalhes
            widget.destroy()  # comando para apagar o que tiver digitado nos campos

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        # chamando a função
        salvar()


##2_#CADASTRO----------
app_img_cadastro = Image.open('add.png') #abrir a imagem
app_img_cadastro = app_img_cadastro.resize((18,18)) #Redimensionar o tamanho da imagem
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro) # Formatar para que possa ser usado dentro do tkinter
app_cadastro = Button(frame_dados,command=lambda:control('cadastro'), image=app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)  #2parte lambda  #funçao control() com a condição
#ADICIONAR---------
app_img_update = Image.open('update.png') #abrir a imagem
app_img_update = app_img_update.resize((18,18)) #Redimensionar o tamanho da imagem
app_img_update = ImageTk.PhotoImage(app_img_update) # Formatar para que possa ser usado dentro do tkinter
app_update = Button(frame_dados,command=lambda:control('adicionar'), image=app_img_update, text="Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_update.place(x=150, y=30)
#SALVAR---------
app_img_save = Image.open('save.png') #abrir a imagem
app_img_save = app_img_save.resize((18,18)) #Redimensionar o tamanho da imagem
app_img_save = ImageTk.PhotoImage(app_img_save) # Formatar para que possa ser usado dentro do tkinter
app_save = Button(frame_dados,command=lambda:control('salvar'), image=app_img_save, text="Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_save.place(x=290, y=30)

cadastro()
janela.mainloop()