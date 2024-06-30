import customtkinter as ctk
import datetime
import calendar

# Cria a janela principal
janela = ctk.CTk()
cor_background = '#fa7f72'
width = janela.winfo_screenwidth()
height = janela.winfo_height()
geometry = str(width) + "x" + str(height)
janela.geometry(geometry)
janela.configure(fg_color=cor_background)


frame_cor = "#fa7f72"
###################################################################################################################
def cadastro_Funcionario():
    apagar_frames_para_o_proximo()
    frame_cadastroFuncionario()

def editar_funcionario():
    apagar_frames_para_o_proximo()
    frame_editar_funcionario()

def cadastro_cliente():
    apagar_frames_para_o_proximo()
    frame_cadastroCliente()

def editar_cliente():
    apagar_frames_para_o_proximo()
    frame_editar_cliente()

def agenda():
    apagar_frames_para_o_proximo()
    frame_agenda()

def editar_agendar():
    apagar_frames_para_o_proximo()
    frame_editar_agenda()

def apagar_frames_para_o_proximo():
    for frame in frameAuxiliar.winfo_children():
        if getattr(frame, "name", None) != "frameEsquerda":
            frame.destroy()


frameAuxiliar = ctk.CTkFrame(janela, width, height, fg_color='red')

frameLogin = ctk.CTkFrame(janela, width, height, fg_color=cor_background)
frameLogin.pack(fill='both', expand=True)
titulo = ctk.CTkLabel(frameLogin, text="SOS", font=('Chonburi', 250), text_color="white")
titulo.pack(padx=10, pady=(10, 5))

entryusuario = ctk.CTkEntry(frameLogin, width=668, height=44, corner_radius=14,
                            placeholder_text='Nome de Usuario ou Email')
entryusuario.pack(padx=10, pady=(10, 5))

entrysenha = ctk.CTkEntry(frameLogin, width=668, height=44, corner_radius=14,
                          placeholder_text='Sua senha')
entrysenha.pack(padx=10, pady=(27, 5))

esqueceusenha = ctk.CTkButton(frameLogin, width=235, height=30, text="Esqueceu a senha?",
                              text_color='white', hover=False, font=('regular', 15))
esqueceusenha.configure(fg_color=cor_background)
esqueceusenha.pack(after=entrysenha, padx=10, pady=(10, 5))


def teste():
    if entrysenha.get() == 'admin' and entryusuario.get() == 'admin':
        temp1 = entryusuario.get()
        print(f"Bem vindo {temp1}")
        frameLogin.pack_forget()
        frameAuxiliar.pack(fill='both', expand=True)
    elif entrysenha.get() != 'admin' and entryusuario.get() == 'admin':
        print('Senha incorreta!')


login = ctk.CTkButton(frameLogin, font=('Crimson pro', 30), text="Entrar", command=teste,
                      width=303, height=66, fg_color="#DF4621")
login.pack(padx=250, pady=(114, 5))



######################################################################################################################
# Cadastro de clientes
def frame_cadastroCliente():
    frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Conteúdo do frame à direita
    texto_direita = ctk.CTkLabel(frame, text="CADASTRO DE CLIENTES", font=("Arial", 30), text_color="white")
    texto_direita.pack(padx=10, pady=10)

    subtitulo2 = ctk.CTkLabel(frame, text="Dados Pessoais", text_color="red", font=("Arial", 18))
    subtitulo2.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1
    label_nome = ctk.CTkLabel(frame_dados_pessoais, text="Nome:", font=("Arial", 30), text_color="white")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_email = ctk.CTkLabel(frame_dados_pessoais, text="E-mail:", font=("Arial", 30), text_color="white")
    label_email.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_email = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
    entry_email.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2
    label_telefone = ctk.CTkLabel(frame_dados_pessoais, text="Telefone:", font=("Arial", 30), text_color="white")
    label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_telefone = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_sexo = ctk.CTkLabel(frame_dados_pessoais, text="Sexo:", font=("Arial", 30), text_color="white")
    label_sexo.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    sexo_var = ctk.StringVar(value="Masculino")
    radio_masculino = ctk.CTkRadioButton(frame_dados_pessoais, text="Masculino", variable=sexo_var,
                                         value="Masculino", font=("Arial", 25), text_color="white")
    radio_masculino.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    radio_feminino = ctk.CTkRadioButton(frame_dados_pessoais, text="Feminino", variable=sexo_var,
                                        value="Feminino", font=("Arial", 25), text_color="white")
    radio_feminino.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    # Linha 3
    label_cpf = ctk.CTkLabel(frame_dados_pessoais, text="CPF:", font=("Arial", 30), text_color="white")
    label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_cpf = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_cpf.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    label_data_nascimento = ctk.CTkLabel(frame_dados_pessoais, text="Data de Nascimento:",
                                         font=("Arial", 30), text_color="white")
    label_data_nascimento.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_data_nascimento = ctk.CTkEntry(frame_dados_pessoais,
                                         fg_color="white", text_color="black", height=30, width=200)
    entry_data_nascimento.grid(row=2, column=3, padx=10, pady=5, sticky="e")

    subtitulo3 = ctk.CTkLabel(frame, text="Endereço", text_color="red", font=("Arial", 18))
    subtitulo3.pack(padx=10, pady=(5, 5))

    linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha4.pack(padx=10, pady=(5, 20))

    frame_endereco = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_endereco.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1 (Endereço)
    label_CEP = ctk.CTkLabel(frame_endereco, text="CEP:", font=("Arial", 30), text_color="white")
    label_CEP.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_CEP = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_CEP.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_Bairro = ctk.CTkLabel(frame_endereco, text="Bairro:", font=("Arial", 30), text_color="white")
    label_Bairro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Bairro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Bairro.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2 (Endereço)
    label_logradouro = ctk.CTkLabel(frame_endereco, text="Logradouro:", font=("Arial", 30), text_color="white")
    label_logradouro.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_logradouro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_logradouro.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_Numero = ctk.CTkLabel(frame_endereco, text="Número:", font=("Arial", 30), text_color="white")
    label_Numero.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Numero = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Numero.grid(row=1, column=3, padx=10, pady=5, sticky="e")

    botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621')
    botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom', anchor='s')

    botao_editar = ctk.CTkButton(frame, text="editar cliente", font=("Arial", 30),
                                 text_color='white', fg_color='#DF4621', command=editar_cliente)
    botao_editar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')


def frame_editar_cliente():
    frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Conteúdo do frame à direita
    texto_direita = ctk.CTkLabel(frame, text="EDITAR CLIENTE", font=("Arial", 30), text_color="white")
    texto_direita.pack(padx=10, pady=10)

    subtitulo2 = ctk.CTkLabel(frame, text="Dados Pessoais", text_color="red", font=("Arial", 18))
    subtitulo2.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1
    label_nome = ctk.CTkLabel(frame_dados_pessoais, text="Nome:", font=("Arial", 30), text_color="white")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_email = ctk.CTkLabel(frame_dados_pessoais, text="E-mail:", font=("Arial", 30), text_color="white")
    label_email.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_email = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
    entry_email.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2
    label_telefone = ctk.CTkLabel(frame_dados_pessoais, text="Telefone:", font=("Arial", 30), text_color="white")
    label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_telefone = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="e")


    # Linha 3
    label_cpf = ctk.CTkLabel(frame_dados_pessoais, text="CPF:", font=("Arial", 30), text_color="white")
    label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_cpf = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_cpf.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    subtitulo3 = ctk.CTkLabel(frame, text="Endereço", text_color="red", font=("Arial", 18))
    subtitulo3.pack(padx=10, pady=(5, 5))

    linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha4.pack(padx=10, pady=(5, 20))

    frame_endereco = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_endereco.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1 (Endereço)
    label_CEP = ctk.CTkLabel(frame_endereco, text="CEP:", font=("Arial", 30), text_color="white")
    label_CEP.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_CEP = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_CEP.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_Bairro = ctk.CTkLabel(frame_endereco, text="Bairro:", font=("Arial", 30), text_color="white")
    label_Bairro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Bairro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Bairro.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2 (Endereço)
    label_logradouro = ctk.CTkLabel(frame_endereco, text="Logradouro:", font=("Arial", 30), text_color="white")
    label_logradouro.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_logradouro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_logradouro.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_Numero = ctk.CTkLabel(frame_endereco, text="Número:", font=("Arial", 30), text_color="white")
    label_Numero.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Numero = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Numero.grid(row=1, column=3, padx=10, pady=5, sticky="e")

    botao_cadastrar = ctk.CTkButton(frame, text="Confirmar", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621')
    botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom', anchor='s')

#######################################################################################################################
#Cadastro de funcionario

def frame_cadastroFuncionario():

    frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Conteúdo do frame à direita
    texto_direita = ctk.CTkLabel(frame, text="CADASTRO DE FUNCIONÁRIOS", font=("Arial", 30), text_color="white")
    texto_direita.pack(padx=10, pady=10)

    subtitulo2 = ctk.CTkLabel(frame, text="Dados Pessoais", text_color="red", font=("Arial", 18))
    subtitulo2.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1
    label_nome = ctk.CTkLabel(frame_dados_pessoais, text="Nome:", font=("Arial", 30), text_color="white")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_email = ctk.CTkLabel(frame_dados_pessoais, text="E-mail:", font=("Arial", 30), text_color="white")
    label_email.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_email = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
    entry_email.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2
    label_telefone = ctk.CTkLabel(frame_dados_pessoais, text="Telefone:", font=("Arial", 30), text_color="white")
    label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_telefone = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_sexo = ctk.CTkLabel(frame_dados_pessoais, text="Sexo:", font=("Arial", 30), text_color="white")
    label_sexo.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    sexo_var = ctk.StringVar(value="Masculino")
    radio_masculino = ctk.CTkRadioButton(frame_dados_pessoais, text="Masculino", variable=sexo_var,
                                         value="Masculino", font=("Arial", 25), text_color="white")
    radio_masculino.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    radio_feminino = ctk.CTkRadioButton(frame_dados_pessoais, text="Feminino", variable=sexo_var,
                                        value="Feminino", font=("Arial", 25), text_color="white")
    radio_feminino.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    # Linha 3
    label_cpf = ctk.CTkLabel(frame_dados_pessoais, text="CPF:", font=("Arial", 30), text_color="white")
    label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_cpf = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_cpf.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    label_data_nascimento = ctk.CTkLabel(frame_dados_pessoais, text="Data de Nascimento:",
                                         font=("Arial", 30), text_color="white")
    label_data_nascimento.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_data_nascimento = ctk.CTkEntry(frame_dados_pessoais,
                                         fg_color="white", text_color="black", height=30, width=200)
    entry_data_nascimento.grid(row=2, column=3, padx=10, pady=5, sticky="e")

    subtitulo3 = ctk.CTkLabel(frame, text="Endereço", text_color="red", font=("Arial", 18))
    subtitulo3.pack(padx=10, pady=(5, 5))

    linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha4.pack(padx=10, pady=(5, 20))

    frame_endereco = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_endereco.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1 (Endereço)
    label_CEP = ctk.CTkLabel(frame_endereco, text="CEP:", font=("Arial", 30), text_color="white")
    label_CEP.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_CEP = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_CEP.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_Bairro = ctk.CTkLabel(frame_endereco, text="Bairro:", font=("Arial", 30), text_color="white")
    label_Bairro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Bairro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Bairro.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2 (Endereço)
    label_logradouro = ctk.CTkLabel(frame_endereco, text="Logradouro:", font=("Arial", 30), text_color="white")
    label_logradouro.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_logradouro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_logradouro.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_Numero = ctk.CTkLabel(frame_endereco, text="Número:", font=("Arial", 30), text_color="white")
    label_Numero.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Numero = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Numero.grid(row=1, column=3, padx=10, pady=5, sticky="e")

    admissao = ctk.CTkLabel(frame, text="Admissao", text_color="red", font=("Arial", 18))
    admissao.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_admissao = ctk.CTkFrame(frame, corner_radius=10, width=800, height=100, fg_color="#fa7f72")
    frame_admissao.pack(padx=10, pady=10, expand=False, fill='both', anchor="center")

    # Linha 1
    label_data_admissao = ctk.CTkLabel(frame_admissao, text="Data de Admissão:", width=45, font=("Arial", 30), text_color="white")
    label_data_admissao.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_data_admissao = ctk.CTkEntry(frame_admissao, fg_color="white", text_color="black", height=30, width=200)
    entry_data_admissao.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_funcao = ctk.CTkLabel(frame_admissao, text="Função:", font=("Arial", 30), text_color="white")
    label_funcao.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_funcao = ctk.CTkEntry(frame_admissao, fg_color="white", text_color="black", height=30, width=200)
    entry_funcao.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621')
    botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

    botao_editar = ctk.CTkButton(frame, text="Editar funcionario", font=("Arial", 30), text_color="white",
                                 fg_color='#DF4621', command=editar_funcionario)
    botao_editar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

#EDitar funcionario
def frame_editar_funcionario():
    frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Conteúdo do frame à direita
    texto_direita = ctk.CTkLabel(frame, text="EDITAR FUNCIONÁRIO", font=("Arial", 30), text_color="white")
    texto_direita.pack(padx=10, pady=10)

    subtitulo2 = ctk.CTkLabel(frame, text="Dados Pessoais", text_color="red", font=("Arial", 18))
    subtitulo2.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1
    label_nome = ctk.CTkLabel(frame_dados_pessoais, text="Nome:", font=("Arial", 30), text_color="white")
    label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_email = ctk.CTkLabel(frame_dados_pessoais, text="E-mail:", font=("Arial", 30), text_color="white")
    label_email.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_email = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
    entry_email.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2
    label_telefone = ctk.CTkLabel(frame_dados_pessoais, text="Telefone:", font=("Arial", 30), text_color="white")
    label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_telefone = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="e")


    # Linha 3
    subtitulo3 = ctk.CTkLabel(frame, text="Endereço", text_color="red", font=("Arial", 18))
    subtitulo3.pack(padx=10, pady=(5, 5))

    linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha4.pack(padx=10, pady=(5, 20))

    frame_endereco = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_endereco.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1 (Endereço)
    label_CEP = ctk.CTkLabel(frame_endereco, text="CEP:", font=("Arial", 30), text_color="white")
    label_CEP.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_CEP = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_CEP.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_Bairro = ctk.CTkLabel(frame_endereco, text="Bairro:", font=("Arial", 30), text_color="white")
    label_Bairro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Bairro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Bairro.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2 (Endereço)
    label_logradouro = ctk.CTkLabel(frame_endereco, text="Logradouro:", font=("Arial", 30), text_color="white")
    label_logradouro.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_logradouro = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_logradouro.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_Numero = ctk.CTkLabel(frame_endereco, text="Número:", font=("Arial", 30), text_color="white")
    label_Numero.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Numero = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Numero.grid(row=1, column=3, padx=10, pady=5, sticky="e")

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_admissao = ctk.CTkFrame(frame, corner_radius=10, width=800, height=100, fg_color="#fa7f72")
    frame_admissao.pack(padx=10, pady=10, expand=False, fill='both', anchor="center")

    # Linha 1

    label_funcao = ctk.CTkLabel(frame_admissao, text="Função:", font=("Arial", 30), text_color="white")
    label_funcao.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_funcao = ctk.CTkEntry(frame_admissao, fg_color="white", text_color="black", height=30, width=200)
    entry_funcao.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    botao_cadastrar = ctk.CTkButton(frame, text="Confirmar", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621')
    botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

####################################################################################################################
#Agendamento
def frame_agenda():
    frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Conteúdo do frame à direita
    texto_direita = ctk.CTkLabel(frame, text="AGENDAMENTO", font=("Arial", 30), text_color="white")
    texto_direita.pack(padx=10, pady=10)

    subtitulo2 = ctk.CTkLabel(frame, text="Identificador", text_color="red", font=("Arial", 18))
    subtitulo2.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1
    label_CPF = ctk.CTkLabel(frame_dados_pessoais, text="CPF", font=("Arial", 30), text_color="white")
    label_CPF.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    # Linha 2


    # Linha 3
    linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha4.pack(padx=10, pady=(5, 20))

    frame_dados_agendamento = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
    frame_dados_agendamento.pack(padx=10, pady=10, expand=False, fill='both')

    # Linha 1 (Endereço)
    label_Data_Original = ctk.CTkLabel(frame_dados_agendamento, text="Data original:", font=("Arial", 30), text_color="white")
    label_Data_Original.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_Data_original = ctk.CTkEntry(frame_dados_agendamento, fg_color="white", text_color="black", height=30, width=200)
    entry_Data_original.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_Bairro = ctk.CTkLabel(frame_dados_agendamento, text="Nova Data:", font=("Arial", 30), text_color="white")
    label_Bairro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Bairro = ctk.CTkEntry(frame_dados_agendamento, fg_color="white", text_color="black", height=30, width=200)
    entry_Bairro.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    # Linha 2 (Endereço)
    label_horario = ctk.CTkLabel(frame_dados_agendamento, text="Horario:", font=("Arial", 30), text_color="white")
    label_horario.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_horario = ctk.CTkEntry(frame_dados_agendamento, fg_color="white", text_color="black", height=30, width=200)
    entry_horario.grid(row=1, column=1, padx=10, pady=5, sticky="e")

    label_ = ctk.CTkLabel(frame_dados_agendamento, text="Número:", font=("Arial", 30), text_color="white")
    label_Numero.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Numero = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Numero.grid(row=1, column=3, padx=10, pady=5, sticky="e")

    admissao = ctk.CTkLabel(frame, text="Admissao", text_color="red", font=("Arial", 18))
    admissao.pack(padx=10, pady=(5, 5))

    linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
    linha2.pack(padx=10, pady=(5, 20))

    # Labels e Entradas para os dados pessoais organizados em duas colunas
    frame_admissao = ctk.CTkFrame(frame, corner_radius=10, width=800, height=100, fg_color="#fa7f72")
    frame_admissao.pack(padx=10, pady=10, expand=False, fill='both', anchor="center")

    # Linha 1
    label_data_admissao = ctk.CTkLabel(frame_admissao, text="Data de Admissão:", width=45, font=("Arial", 30), text_color="white")
    label_data_admissao.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_data_admissao = ctk.CTkEntry(frame_admissao, fg_color="white", text_color="black", height=30, width=200)
    entry_data_admissao.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    label_funcao = ctk.CTkLabel(frame_admissao, text="Função:", font=("Arial", 30), text_color="white")
    label_funcao.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_funcao = ctk.CTkEntry(frame_admissao, fg_color="white", text_color="black", height=30, width=200)
    entry_funcao.grid(row=0, column=3, padx=10, pady=5, sticky="e")

    botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 30), text_color="white",
                                fg_color='#DF4621')
    botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

    botao_editar = ctk.CTkButton(frame, text="Editar funcionario", font=("Arial", 30), text_color="white",
                             fg_color='#DF4621', command=editar_funcionario)
    botao_editar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

####################################################################################################################
# lado esquerdo, navegação


frameEsquerda = ctk.CTkFrame(frameAuxiliar, width=250, corner_radius=10, fg_color="#ff6347")
frameEsquerda.name = "frameEsquerda"
frameEsquerda.pack(side="left", fill="y", padx=20, pady=20)

titulo = ctk.CTkLabel(frameEsquerda, text="SOS", font=("Arial", 80), text_color="white")
titulo.pack(padx=10, pady=(10, 5))

subtitulo = ctk.CTkLabel(frameEsquerda, text="Cadastrar", font=("Arial", 18), text_color="white")
subtitulo.pack(padx=10, pady=(5, 5))

linha = ctk.CTkFrame(frameEsquerda, height=2, width=380, fg_color="white")
linha.pack(padx=10, pady=(5, 20))


# Configurando o botão com as opções solicitadas
funcionario = ctk.CTkButton(
    frameEsquerda, text="FUNCIONARIO", command=cadastro_Funcionario,
    width=350, height=50,
    fg_color="#fa7f72", hover_color="lightpink",
    text_color="white", corner_radius=10, border_color="grey", border_width=2,
    font=("Arial", 30, "bold")
)
funcionario.pack(padx=10, pady=10)

cliente = ctk.CTkButton(
    frameEsquerda, text="CLIENTE", width=350, height=50, command=cadastro_cliente,
    fg_color="#fa7f72", hover_color="lightpink",
    text_color="white", corner_radius=10, border_color="grey", border_width=2,
    font=("Arial", 30, "bold")
)
cliente.pack(padx=10, pady=10)

# Função para alterar o efeito hover

def on_enter_funcionario(event):
    funcionario.configure(fg_color="lightpink", text_color="darkred")

def on_leave_funcionario(event):
    funcionario.configure(fg_color="#fa7f72", text_color="white")

def on_enter_cliente(event):
    cliente.configure(fg_color="lightpink", text_color="darkred")

def on_leave_cliente(event):
    cliente.configure(fg_color="#fa7f72", text_color="white")

funcionario.bind("<Enter>", on_enter_funcionario)

funcionario.bind("<Leave>", on_leave_funcionario)

cliente.bind("<Enter>", on_enter_cliente)
cliente.bind("<Leave>", on_leave_cliente)

subtitulo2 = ctk.CTkLabel(frameEsquerda, text="Procedimentos", font=("Arial", 18), text_color="white")
subtitulo2.pack(padx=10, pady=(5, 5))

linha = ctk.CTkFrame(frameEsquerda, height=2, width=300, fg_color="white")
linha.pack(padx=10, pady=(5, 20))

unha = ctk.CTkButton(
    frameEsquerda, text="UNHA",
    width=350, height=50,
    fg_color="#fa7f72", hover_color="lightpink",
    text_color="white", corner_radius=10, border_color="grey", border_width=2,
    font=("Arial", 30, "bold")
)
unha.pack(padx=10, pady=10)

def on_enter_unha(event):
    unha.configure(fg_color="lightpink", text_color="darkred")

def on_leave_unha(event):
    unha.configure(fg_color="#fa7f72", text_color="white")

unha.bind("<Enter>", on_enter_unha)
unha.bind("<Leave>", on_leave_unha)

cabelo = ctk.CTkButton(
    frameEsquerda, text="CABELO",
    width=350, height=50,
    fg_color="#fa7f72", hover_color="lightpink",
    text_color="white", corner_radius=10, border_color="grey", border_width=2,
    font=("Arial", 30, "bold")
)
cabelo.pack(padx=10, pady=10)

def on_enter_cabelo(event):
    cabelo.configure(fg_color="lightpink", text_color="darkred")

def on_leave_cabelo(event):
    cabelo.configure(fg_color="#fa7f72", text_color="white")

cabelo.bind("<Enter>", on_enter_cabelo)
cabelo.bind("<Leave>", on_leave_cabelo)

sobrancelha = ctk.CTkButton(
    frameEsquerda, text="SOBRANCELHA",
    width=350, height=50,
    fg_color="#fa7f72", hover_color="lightpink",
    text_color="white", corner_radius=10, border_color="grey", border_width=2,
    font=("Arial", 30, "bold")
)
sobrancelha.pack(padx=10, pady=10)

def on_enter_sobrancelha(event):
    sobrancelha.configure(fg_color="lightpink", text_color="darkred")

def on_leave_sobrancelha(event):
    sobrancelha.configure(fg_color="#fa7f72", text_color="white")

sobrancelha.bind("<Enter>", on_enter_sobrancelha)
sobrancelha.bind("<Leave>", on_leave_sobrancelha)

subtitulo3 = ctk.CTkLabel(frameEsquerda, text="Atendimento", font=("Arial", 18), text_color="white")
subtitulo3.pack(padx=10, pady=(5, 5))

linha = ctk.CTkFrame(frameEsquerda, height=2, width=300, fg_color="white")
linha.pack(padx=10, pady=(5, 20))

agendar = ctk.CTkButton(
    frameEsquerda, text="AGENDAR", command=agenda,
    width=350, height=50,
    fg_color="#fa7f72", hover_color="lightpink",
    text_color="white", corner_radius=10, border_color="grey", border_width=2,
    font=("Arial", 30, "bold")
)
agendar.pack(padx=10, pady=10)

def on_enter_agendar(event):
    agendar.configure(fg_color="lightpink", text_color="darkred")

def on_leave_agendar(event):
    agendar.configure(fg_color="#fa7f72", text_color="white")

agendar.bind("<Enter>", on_enter_agendar)
agendar.bind("<Leave>", on_leave_agendar)

###############################################################################################################

############# Adiciona o calendário
#calendar_frame = ctk.CTkFrame(frameAuxiliar, fg_color="black")
#calendar_frame.pack(fill="both", expand=True, padx=20, pady=20)


# Configurando o calendário interativo
#today = datetime.date.today()
#current_month = today.month
#current_year = today.year

#months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

#def update_calendar(month, year):
#        for widget in calendar_frame.winfo_children():
#            widget.destroy()

#        calendar_label = ctk.CTkLabel(calendar_frame, text=f"{months[month - 1]} {year}", font=("Arial", 24), bg_color="black", fg_color="white")
#        calendar_label.pack(pady=20)

        # Função para lidar com o clique em um dia do calendário
#        def day_clicked(day):
#           # Cria uma janela para entrada de texto
#            entry_window = ctk.Toplevel(janela)
#            entry_window.geometry("300x150")
#            entry_window.title(f"Informações do dia {day}")

            # Texto explicativo
#            info_label = ctk.Label(entry_window, text=f"Informe as informações para o dia {day}:", font=("Arial", 12))
#            info_label.pack(pady=10)

            # Campo de entrada de texto
#            info_entry = ctk.Entry(entry_window, width=30)
#            info_entry.pack(pady=10)

            # Botão para salvar as informações
#            def save_info():
#                info = info_entry.get()
                # Aqui você pode salvar as informações em algum lugar (banco de dados, arquivo, etc.)
#                print(f"Informações para o dia {day} salvas: {info}")
#                entry_window.destroy()

#            save_button = ctk.Button(entry_window, text="Salvar", command=save_info)
#            save_button.pack(pady=10)

        # Configuração do calendário com dias
#        days_frame = ctk.CTkFrame(calendar_frame, bg_color="black")
#        days_frame.pack()

        # Obtém o número de dias no mês atual usando o módulo calendar
#        num_days = calendar.monthrange(year, month)[1]

#        day_colors = {
#            "Monday": "#2274a5",
#            "Tuesday": "#32936f",
#            "Wednesday": "#fdae61",
#            "Thursday": "#e94f37",
#            "Friday": "#1e434c",
#            "Saturday": "#b4656f",
#            "Sunday": "#465362"
#        }

        #janela.style = ctk.CTkStyle()

        
        # Cria botões para cada dia do mês
#        for day in range(1, num_days + 1):
#            day_of_week = calendar.weekday(year, month, day)
#            day_name = calendar.day_name[day_of_week]
#            janela.style.configure(f"{day_name}.TButton", foreground="white", background=day_colors[day_name], font=("Arial", 12, "bold"))
            
#            day_button = ctk.Button(days_frame, text=str(day), width=10,  # Aumenta a largura dos botões
#                                    style=f'{day_name}.TButton',  # Aplica o estilo baseado no dia da semana
#                                    command=lambda d=day: day_clicked(d))
#            day_button.grid(row=(day - 1) // 7, column=(day - 1) % 7, padx=10, pady=10)  # Aumenta o espaçamento entre os botões

#def prev_month():
    #nonlocal current_month, current_year
#    if current_month == 1:
#            current_month = 12
#            current_year -= 1
#   else:
#            current_month -= 1
#    update_calendar(current_month, current_year)

#def next_month():
 #       #nonlocal current_month, current_year
 #       if current_month == 12:
 #           current_month = 1
 #           current_year += 1
 #       else:
 #           current_month += 1
 #       update_calendar(current_month, current_year)

    # Botões para mudar de mês
#prev_button = ctk.CTkButton(calendar_frame, text="Anterior", command=prev_month)
#prev_button.pack(side="left", padx=10)

#next_button = ctk.CTkButton(calendar_frame, text="Próximo", command=next_month)
#next_button.pack(side="right", padx=10)

#update_calendar(current_month, current_year)

###############################################################################################################

# EDITAR AGENDA
def frame_editar_agenda():
    
    frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

# Conteúdo do frame à direita
    texto_direita = ctk.CTkLabel(frame, text="EDITAR AGENDA", font=("Arial", 30), text_color="white")
    texto_direita.pack(padx=10, pady=10)

# Linha 1
    label_CPF = ctk.CTkLabel(frame_editar_agenda, text="CPF:", font=("Arial", 30), text_color="white")
    label_CPF.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_CPF = ctk.CTkEntry(frame_editar_agenda,  fg_color="white", text_color="black", height=30, width=200)
    entry_CPF.grid(row=0, column=1, padx=10, pady=5, sticky="e")

# Linha 2
    label_Novo_Valor = ctk.CTkLabel(frame_editar_agenda, text="Novo_Valor:", font=("Arial", 30), text_color="white")
    label_Novo_Valor.grid(row=0, column=2, padx=10, pady=5, sticky="w")
    entry_Novo_Valor = ctk.CTkEntry(frame_editar_agenda, fg_color="white", text_color="black", height=30, width=200)
    entry_Novo_Valor.grid(row=0, column=3, padx=10, pady=5, sticky="e")

# Linha 3
    label_Modificação = ctk.CTkLabel(frame_editar_agenda, text="Modificação:", font=("Arial", 30), text_color="white")
    label_Modificação.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_Modificação = ctk.CTkEntry(frame_editar_agenda,  fg_color="white", text_color="black", height=30, width=200)
    entry_Modificação.grid(row=1, column=1, padx=10, pady=5, sticky="e")


###############################################################################################################



janela.mainloop()
