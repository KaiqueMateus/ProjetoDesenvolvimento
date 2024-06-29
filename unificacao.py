import customtkinter as ctk


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


def cadastro_cliente():
    apagar_frames_para_o_proximo()
    frame_cadastroCliente()


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
#Cadastro de clientes
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

    botao_editar = ctk.CTkButton(frame, text="editar cliente", font=("Arial", 30), text_color='white', fg_color='#DF4621')
    botao_editar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')
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
                                 fg_color='#DF4621')
    botao_editar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

####################################################################################################################
#lado esquerdo, navegação
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
    frameEsquerda, text="AGENDAR",
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

janela.mainloop()