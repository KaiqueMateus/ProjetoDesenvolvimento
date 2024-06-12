import customtkinter as ctk

# Configurações iniciais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Cria a janela principal e altera a cor de fundo
janela = ctk.CTk()
janela.geometry("800x600")
janela.configure(fg_color="#fa7f72")  # Altera a cor de fundo da janela principal

def configure_frame_esquerda(parent):
    frame = ctk.CTkFrame(parent, width=250, corner_radius=10, fg_color="#ff6347")
    frame.pack(side="left", fill="y", padx=20, pady=20)
    
    # Adicionando Título e Subtítulo
    titulo = ctk.CTkLabel(frame, text="SOS", font=("Arial", 80), text_color="white")
    titulo.pack(padx=10, pady=(10, 5))

    subtitulo = ctk.CTkLabel(frame, text="Cadastrar", font=("Arial", 18), text_color="white")
    subtitulo.pack(padx=10, pady=(5, 5))

    linha = ctk.CTkFrame(frame, height=2, width=380, fg_color="white")
    linha.pack(padx=10, pady=(5, 20))

    # Campos de login
    def clique():
        print("Fazer Login")
    
    # Configurando o botão com as opções solicitadas
    funcionario = ctk.CTkButton(
        frame, text="FUNCIONARIO", command=clique, width=350, height=50, 
        fg_color="#fa7f72", hover_color="lightpink",
        text_color="white", corner_radius=10, border_color="grey", border_width=2,
        font=("Arial", 30, "bold")
    )
    funcionario.pack(padx=10, pady=10)
    
    cliente = ctk.CTkButton(
        frame, text="CLIENTE", command=clique, width=350, height=50, 
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

    subtitulo2 = ctk.CTkLabel(frame, text="Procedimentos", font=("Arial", 18), text_color="white")
    subtitulo2.pack(padx=10, pady=(5, 5))

    linha = ctk.CTkFrame(frame, height=2, width=300, fg_color="white")
    linha.pack(padx=10, pady=(5, 20))

    unha = ctk.CTkButton(
        frame, text="UNHA", command=clique, width=350, height=50, 
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
        frame, text="CABELO", command=clique, width=350, height=50, 
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
        frame, text="SOBRANCELHA", command=clique, width=350, height=50, 
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

    subtitulo3 = ctk.CTkLabel(frame, text="Atendimento", font=("Arial", 18), text_color="white")
    subtitulo3.pack(padx=10, pady=(5, 5))

    linha = ctk.CTkFrame(frame, height=2, width=300, fg_color="white")
    linha.pack(padx=10, pady=(5, 20))

    agendar = ctk.CTkButton(
        frame, text="AGENDAR", command=clique, width=350, height=50, 
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

def configure_frame_direita(parent):
    frame_cor = "#fa7f72"  # Cor do frame à direita
    frame = ctk.CTkFrame(parent, corner_radius=10, fg_color=frame_cor)
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
    radio_masculino = ctk.CTkRadioButton(frame_dados_pessoais, text="Masculino", variable=sexo_var, value="Masculino", font=("Arial", 25), text_color="white")
    radio_masculino.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    radio_feminino = ctk.CTkRadioButton(frame_dados_pessoais, text="Feminino", variable=sexo_var, value="Feminino", font=("Arial", 25), text_color="white")
    radio_feminino.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    # Linha 3
    label_cpf = ctk.CTkLabel(frame_dados_pessoais, text="CPF:", font=("Arial", 30), text_color="white")
    label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_cpf = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
    entry_cpf.grid(row=2, column=1, padx=10, pady=5, sticky="e")

    label_data_nascimento = ctk.CTkLabel(frame_dados_pessoais, text="Data de Nascimento:", font=("Arial", 30), text_color="white")
    label_data_nascimento.grid(row=2, column=2, padx=10, pady=5, sticky="w")
    entry_data_nascimento = ctk.CTkEntry(frame_dados_pessoais,  fg_color="white", text_color="black", height=30, width=200)
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

    label_Número = ctk.CTkLabel(frame_endereco, text="Número:", font=("Arial", 30), text_color="white")
    label_Número.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    entry_Número = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
    entry_Número.grid(row=1, column=3, padx=10, pady=5, sticky="e")

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

configure_frame_esquerda(janela)
configure_frame_direita(janela)

# Inicia o loop principal
janela.mainloop()
