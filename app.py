import customtkinter as ctk
import datetime
import calendar
from flask import Flask
from database import db
from models import Cliente, Funcionario, Agendamento
from routes import bp as main_bp
import threading
from waitress import serve
import logging
import requests
from tkinter import messagebox
import pdb
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_flask_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///salao.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)
    return app

def run_flask_app():
    app = create_flask_app()
    logging.info("Starting Flask app...")
    serve(app, host='0.0.0.0', port=5000)

def create_interface():
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

    def ver_agendamentos():
        apagar_frames_para_o_proximo()
        frame_ver_agendamentos()

    def editar_agendamento():
        apagar_frames_para_o_proximo()
        frame_editar_agendamento()

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

        def cadastrar_cliente():
            data = {
                "nome": entry_nome.get(),
                "email": entry_email.get(),
                "telefone": int(entry_telefone.get()),
                "sexo": sexo_var.get(),
                "cpf": entry_cpf.get(),
                "data_nascimento": datetime.strptime(entry_data_nascimento.get(), "%d/%m/%Y").date().isoformat(),
                "cep": entry_CEP.get(),
                "bairro": entry_Bairro.get(),
                "logradouro": entry_logradouro.get(),
                "numero": entry_Numero.get()
            }
            response = requests.post("http://localhost:5000/clientes", json=data)
            if response.status_code == 201:
                print(response)
                messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            else:
                print(response)
                messagebox.showerror("Erro", "Falha ao cadastrar cliente.")

        botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 30), text_color="white",
                                        fg_color='#DF4621', command=cadastrar_cliente)
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

        subtitulo2 = ctk.CTkLabel(frame, text="Buscar Cliente por CPF", text_color="white", font=("Arial", 18))
        subtitulo2.pack(padx=10, pady=(5, 5))

        entry_buscar_cpf = ctk.CTkEntry(frame, fg_color="white", text_color="black", height=30, width=200, placeholder_text="CPF")
        entry_buscar_cpf.pack(padx=10, pady=5)

        def buscar_cliente():
            cpf = entry_buscar_cpf.get()
            response = requests.get(f"http://localhost:5000/clientes/cpf/{cpf}")
            if response.status_code == 200:
                cliente = response.json()
                preencher_formulario(cliente)
            else:
                messagebox.showerror("Erro", "Cliente não encontrado.")

        botao_buscar = ctk.CTkButton(frame, text="Buscar", font=("Arial", 18), text_color="white",
                                    fg_color='#DF4621', command=buscar_cliente)
        botao_buscar.pack(padx=10, pady=5)

        # Labels e Entradas para os dados pessoais organizados em duas colunas
        frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

        # Linha 1
        label_nome = ctk.CTkLabel(frame_dados_pessoais, text="Nome:", font=("Arial", 30), text_color="white")
        label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_nome = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        label_email = ctk.CTkLabel(frame_dados_pessoais, text="E-mail:", font=("Arial", 30), text_color="white")
        label_email.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        entry_email = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_email.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        # Linha 2
        label_telefone = ctk.CTkLabel(frame_dados_pessoais, text="Telefone:", font=("Arial", 30), text_color="white")
        label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_telefone = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # Linha 3
        label_cpf = ctk.CTkLabel(frame_dados_pessoais, text="CPF:", font=("Arial", 30), text_color="white")
        label_cpf.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        entry_cpf = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
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

        def preencher_formulario(cliente):
            entry_nome.delete(0, ctk.END)
            entry_nome.insert(0, cliente["nome"])
            entry_email.delete(0, ctk.END)
            entry_email.insert(0, cliente["email"])
            entry_telefone.delete(0, ctk.END)
            entry_telefone.insert(0, cliente["telefone"])
            entry_cpf.delete(0, ctk.END)
            entry_cpf.insert(0, cliente["cpf"])
            entry_CEP.delete(0, ctk.END)
            entry_CEP.insert(0, cliente["cep"])
            entry_Bairro.delete(0, ctk.END)
            entry_Bairro.insert(0, cliente["bairro"])
            entry_logradouro.delete(0, ctk.END)
            entry_logradouro.insert(0, cliente["logradouro"])
            entry_Numero.delete(0, ctk.END)
            entry_Numero.insert(0, cliente["numero"])

        def atualizar_cliente():
            try:
                data = {
                    "nome": entry_nome.get(),
                    "email": entry_email.get(),
                    "telefone": entry_telefone.get(),
                    "cpf": entry_cpf.get(),
                    "cep": entry_CEP.get(),
                    "bairro": entry_Bairro.get(),
                    "logradouro": entry_logradouro.get(),
                    "numero": entry_Numero.get()
                }
                cpf = entry_cpf.get()
                response = requests.put(f"http://localhost:5000/clientes/cpf/{cpf}", json=data)
                if response.status_code == 200:
                    messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
                else:
                    print(f"Erro ao atualizar cliente: {response.status_code}")
                    print(f"Detalhes do erro: {response.text}")
                    messagebox.showerror("Erro", f"Falha ao atualizar cliente. Código: {response.status_code}")
            except ValueError as ve:
                print(f"Erro ao converter data: {ve}")
                messagebox.showerror("Erro", "Dados inválidos.")

        botao_atualizar = ctk.CTkButton(frame, text="Atualizar", font=("Arial", 30), text_color="white",
                                        fg_color='#DF4621', command=atualizar_cliente)
        botao_atualizar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

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

        def cadastrar_funcionario():
            try:
                data = {
                    "nome": entry_nome.get(),
                    "email": entry_email.get(),
                    "telefone": entry_telefone.get(),
                    "sexo": sexo_var.get(),
                    "cpf": entry_cpf.get(),
                    "data_nascimento": datetime.strptime(entry_data_nascimento.get(), "%d/%m/%Y").date().isoformat(),
                    "cep": entry_CEP.get(),
                    "bairro": entry_Bairro.get(),
                    "logradouro": entry_logradouro.get(),
                    "numero": entry_Numero.get(),
                    "data_admissao": datetime.strptime(entry_data_admissao.get(), "%d/%m/%Y").date().isoformat(),
                    "funcao": entry_funcao.get()
                }
                response = requests.post("http://localhost:5000/funcionarios", json=data)
                if response.status_code == 201:
                    messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
                else:
                    print(f"Erro ao cadastrar funcionário: {response.status_code}")
                    print(f"Detalhes do erro: {response.text}")
                    messagebox.showerror("Erro", f"Falha ao cadastrar funcionário. Código: {response.status_code}")
            except ValueError as ve:
                print(f"Erro ao converter data: {ve}")
                messagebox.showerror("Erro", "Dados inválidos.")

        botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 30), text_color="white",
                                        fg_color='#DF4621', command=cadastrar_funcionario)
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

        # Entrada para buscar o funcionário pelo CPF
        label_busca_cpf = ctk.CTkLabel(frame, text="CPF:", font=("Arial", 30), text_color="white")
        label_busca_cpf.pack(padx=10, pady=5)
        entry_busca_cpf = ctk.CTkEntry(frame, fg_color="white", text_color="black", height=30, width=200)
        entry_busca_cpf.pack(padx=10, pady=5)

        def buscar_funcionario():
            cpf = entry_busca_cpf.get()
            response = requests.get(f"http://localhost:5000/funcionarios/cpf/{cpf}")
            if response.status_code == 200:
                funcionario = response.json()
                entry_nome.delete(0, ctk.END)
                entry_nome.insert(0, funcionario['nome'])
                entry_email.delete(0, ctk.END)
                entry_email.insert(0, funcionario['email'])
                entry_telefone.delete(0, ctk.END)
                entry_telefone.insert(0, funcionario['telefone'])
                entry_data_nascimento.delete(0, ctk.END)
                entry_data_nascimento.insert(0, datetime.strptime(funcionario['data_nascimento'], '%Y-%m-%d').strftime('%d/%m/%Y'))
                entry_CEP.delete(0, ctk.END)
                entry_CEP.insert(0, funcionario['cep'])
                entry_Bairro.delete(0, ctk.END)
                entry_Bairro.insert(0, funcionario['bairro'])
                entry_logradouro.delete(0, ctk.END)
                entry_logradouro.insert(0, funcionario['logradouro'])
                entry_Numero.delete(0, ctk.END)
                entry_Numero.insert(0, funcionario['numero'])
                entry_funcao.delete(0, ctk.END)
                entry_funcao.insert(0, funcionario['funcao'])
            else:
                messagebox.showerror("Erro", "Funcionário não encontrado.")

        botao_buscar = ctk.CTkButton(frame, text="Buscar", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621', command=buscar_funcionario)
        botao_buscar.pack(padx=10, pady=15)

        # Labels e Entradas para os dados pessoais organizados em duas colunas
        frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

        # Linha 1
        label_nome = ctk.CTkLabel(frame_dados_pessoais, text="Nome:", font=("Arial", 30), text_color="white")
        label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_nome = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        label_email = ctk.CTkLabel(frame_dados_pessoais, text="E-mail:", font=("Arial", 30), text_color="white")
        label_email.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        entry_email = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_email.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        # Linha 2
        label_telefone = ctk.CTkLabel(frame_dados_pessoais, text="Telefone:", font=("Arial", 30), text_color="white")
        label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_telefone = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        # Linha 3

        label_data_nascimento = ctk.CTkLabel(frame_dados_pessoais, text="Data de Nascimento:",
                                            font=("Arial", 30), text_color="white")
        label_data_nascimento.grid(row=2, column=2, padx=10, pady=5, sticky="w")
        entry_data_nascimento = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
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

        def editar_funcionario():
            try:
                data = {
                    "nome": entry_nome.get(),
                    "email": entry_email.get(),
                    "telefone": entry_telefone.get(),
                    "data_nascimento": datetime.strptime(entry_data_nascimento.get(), "%d/%m/%Y").date().isoformat(),
                    "cep": entry_CEP.get(),
                    "bairro": entry_Bairro.get(),
                    "logradouro": entry_logradouro.get(),
                    "numero": entry_Numero.get(),
                    "funcao": entry_funcao.get()
                }
                cpf = entry_busca_cpf.get()
                response = requests.get(f"http://localhost:5000/funcionarios/cpf/{cpf}")
                if response.status_code == 200:
                    funcionario = response.json()
                    response_update = requests.put(f"http://localhost:5000/funcionarios/{funcionario['id']}", json=data)
                    if response_update.status_code == 200:
                        messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")
                    else:
                        print(f"Erro ao atualizar funcionário: {response_update.status_code}")
                        print(f"Detalhes do erro: {response_update.text}")
                        messagebox.showerror("Erro", f"Falha ao atualizar funcionário. Código: {response_update.status_code}")
                else:
                    messagebox.showerror("Erro", "Funcionário não encontrado.")
            except ValueError as ve:
                print(f"Erro ao converter data: {ve}")
                messagebox.showerror("Erro", "Dados inválidos.")

        botao_cadastrar = ctk.CTkButton(frame, text="Confirmar", font=("Arial", 30), text_color="white",
                                        fg_color='#DF4621', command=editar_funcionario)
        botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')


    ####################################################################################################################
    #Agendamento
    def frame_agenda():
        frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
        frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Conteúdo do frame à direita
        texto_direita = ctk.CTkLabel(frame, text="AGENDAMENTO", font=("Arial", 30), text_color="white")
        texto_direita.pack(padx=10, pady=10)

        subtitulo2 = ctk.CTkLabel(frame, text="Dados do cliente", text_color="red", font=("Arial", 18))
        subtitulo2.pack(padx=10, pady=(5, 5))

        linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
        linha2.pack(padx=10, pady=(5, 20))

        # Labels e Entradas para os dados pessoais organizados em duas colunas
        frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

        # Linha 1
        label_CPF = ctk.CTkLabel(frame_dados_pessoais, text="CPF Cliente", font=("Arial", 30), text_color="white")
        label_CPF.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_CPF_cliente = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_CPF_cliente.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        label_CPF_funcionario = ctk.CTkLabel(frame_dados_pessoais, text="CPF Funcionário", font=("Arial", 30), text_color="white")
        label_CPF_funcionario.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_CPF_funcionario = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_CPF_funcionario.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
        linha4.pack(padx=10, pady=(5, 20))

        frame_endereco = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        frame_endereco.pack(padx=10, pady=10, expand=False, fill='both')

        # Linha 1 (Endereço)
        label_CEP = ctk.CTkLabel(frame_endereco, text="Procedimento:", font=("Arial", 30), text_color="white")
        label_CEP.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_procedimento = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
        entry_procedimento.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        label_Bairro = ctk.CTkLabel(frame_endereco, text="Profissional:", font=("Arial", 30), text_color="white")
        label_Bairro.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        entry_profissional = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
        entry_profissional.grid(row=0, column=3, padx=10, pady=5, sticky="e")

        # Linha 2 (Endereço)
        label_logradouro = ctk.CTkLabel(frame_endereco, text="Data:", font=("Arial", 30), text_color="white")
        label_logradouro.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_data = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
        entry_data.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        label_Numero = ctk.CTkLabel(frame_endereco, text="horário:", font=("Arial", 30), text_color="white")
        label_Numero.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        entry_horario = ctk.CTkEntry(frame_endereco, fg_color="white", text_color="black", height=30, width=200)
        entry_horario.grid(row=1, column=3, padx=10, pady=5, sticky="e")

        linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
        linha2.pack(padx=10, pady=(5, 20))

        def cadastrar_agendamento():
            cpf_cliente = entry_CPF_cliente.get()
            cpf_funcionario = entry_CPF_funcionario.get()

            cliente_response = requests.get(f"http://localhost:5000/clientes/cpf/{cpf_cliente}")
            funcionario_response = requests.get(f"http://localhost:5000/funcionarios/cpf/{cpf_funcionario}")

            if cliente_response.status_code != 200:
                messagebox.showerror("Erro", f"Cliente não encontrado. Código: {cliente_response.status_code}")
                return

            if funcionario_response.status_code != 200:
                messagebox.showerror("Erro", f"Funcionário não encontrado. Código: {funcionario_response.status_code}")
                return

            cliente_id = cliente_response.json().get("id")
            funcionario_id = funcionario_response.json().get("id")

            # Convertendo a data e o horário para o formato esperado pelo backend
            try:
                data_agendamento = datetime.strptime(f"{entry_data.get()} {entry_horario.get()}", "%d/%m/%Y %H:%M")
                data_agendamento_str = data_agendamento.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                messagebox.showerror("Erro", "Formato de data ou horário inválido. Use dd/mm/yyyy hh:mm")
                return

            data = {
                "cliente_id": cliente_id,
                "funcionario_id": funcionario_id,
                "data_agendamento": data_agendamento_str,
                "servico": entry_procedimento.get()
            }

            response = requests.post("http://localhost:5000/agendamentos", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Sucesso", "Agendamento cadastrado com sucesso!")
            else:
                print(f"Erro ao cadastrar agendamento: {response.status_code}")
                print(f"Detalhes do erro: {response.text}")
                messagebox.showerror("Erro", f"Falha ao cadastrar agendamento. Código: {response.status_code}")

        botao_cadastrar = ctk.CTkButton(frame, text="Cadastrar", font=("Arial", 30), text_color="white",
                                        fg_color='#DF4621', command=cadastrar_agendamento)
        botao_cadastrar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

        botao_editar = ctk.CTkButton(frame, text="Editar Agendamento", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621', command=editar_agendamento)
        botao_editar.pack(after=frame_endereco, padx=10, pady=15, side='bottom')

        botao_ver_agendamentos = ctk.CTkButton(frame, text="Ver Agendamentos", font=("Arial", 30), text_color="white",
                                            fg_color='#DF4621', command=ver_agendamentos)
        botao_ver_agendamentos.pack(after=frame_endereco, padx=10, pady=15, side='bottom')


    def frame_ver_agendamentos():
        frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
        frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Conteúdo do frame à direita
        texto_direita = ctk.CTkLabel(frame, text="VER AGENDAMENTOS", font=("Arial", 30), text_color="white")
        texto_direita.pack(padx=10, pady=10)

        linha = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
        linha.pack(padx=10, pady=(5, 20))

        lista_agendamentos = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        lista_agendamentos.pack(padx=10, pady=10, expand=True, fill='both')

        def carregar_agendamentos():
            response = requests.get("http://localhost:5000/agendamentos")
            if response.status_code == 200:
                agendamentos = response.json()
                for agendamento in agendamentos:
                    item_frame = ctk.CTkFrame(lista_agendamentos, corner_radius=10, fg_color="white")
                    item_frame.pack(padx=10, pady=5, fill='x')
                    label_info = ctk.CTkLabel(item_frame, text=f"Nome do Cliente: {agendamento['cliente_nome']}, "
                                                            f"Funcionário Responsável: {agendamento['funcionario_nome']}, "
                                                            f"Data: {agendamento['data_agendamento']}, "
                                                            f"Serviço: {agendamento['servico']}",
                                            font=("Arial", 20), text_color="black")
                    label_info.pack(padx=10, pady=5)
            else:
                print(response.text)
                messagebox.showerror("Erro", f"Falha ao carregar agendamentos. Código: {response.status_code}")

        carregar_agendamentos()

    def frame_editar_agendamento():
        frame = ctk.CTkFrame(frameAuxiliar, corner_radius=10, fg_color=frame_cor)
        frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Conteúdo do frame à direita
        texto_direita = ctk.CTkLabel(frame, text="EDITAR AGENDAMENTO", font=("Arial", 30), text_color="white")
        texto_direita.pack(padx=10, pady=10)

        subtitulo2 = ctk.CTkLabel(frame, text="Identificador", text_color="red", font=("Arial", 18))
        subtitulo2.pack(padx=10, pady=(5, 5))

        linha2 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
        linha2.pack(padx=10, pady=(5, 20))

        # Labels e Entradas para os dados pessoais organizados em duas colunas
        frame_dados_pessoais = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        frame_dados_pessoais.pack(padx=10, pady=10, expand=False, fill='both')

        # Linha 1
        label_CPF = ctk.CTkLabel(frame_dados_pessoais, text="CPF Cliente", font=("Arial", 30), text_color="white")
        label_CPF.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_CPF = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_CPF.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        label_data_original = ctk.CTkLabel(frame_dados_pessoais, text="Data Original", font=("Arial", 30), text_color="white")
        label_data_original.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_data_original = ctk.CTkEntry(frame_dados_pessoais, fg_color="white", text_color="black", height=30, width=200)
        entry_data_original.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        linha4 = ctk.CTkFrame(frame, height=2, width=380, fg_color="red")
        linha4.pack(padx=10, pady=(5, 20))

        frame_dados_agendamento = ctk.CTkFrame(frame, corner_radius=10, fg_color="#fa7f72")
        frame_dados_agendamento.pack(padx=10, pady=10, expand=False, fill='both')

        # Linha 1 (Endereço)
        label_nova_data = ctk.CTkLabel(frame_dados_agendamento, text="Nova Data", font=("Arial", 30), text_color="white")
        label_nova_data.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        entry_nova_data = ctk.CTkEntry(frame_dados_agendamento, fg_color="white", text_color="black", height=30, width=200)
        entry_nova_data.grid(row=0, column=1, padx=10, pady=5, sticky="e")

        label_novo_horario = ctk.CTkLabel(frame_dados_agendamento, text="Novo Horário", font=("Arial", 30), text_color="white")
        label_novo_horario.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        entry_novo_horario = ctk.CTkEntry(frame_dados_agendamento, fg_color="white", text_color="black", height=30, width=200)
        entry_novo_horario.grid(row=1, column=1, padx=10, pady=5, sticky="e")

        def buscar_agendamento():
            cpf_cliente = entry_CPF.get()
            data_original = entry_data_original.get()

            try:
                data_obj = datetime.strptime(data_original, "%d/%m/%Y")
                data_str = data_obj.strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Erro", "Formato de data inválido. Use dd/mm/yyyy")
                return

            response = requests.get(f"http://localhost:5000/agendamentos/search?cpf_cliente={cpf_cliente}&data_agendamento={data_str}")
            if response.status_code == 200:
                agendamento = response.json()
                entry_nova_data.delete(0, 'end')
                entry_nova_data.insert(0, data_obj.strftime("%d/%m/%Y"))
                entry_novo_horario.delete(0, 'end')
                entry_novo_horario.insert(0, datetime.strptime(agendamento['data_agendamento'], "%Y-%m-%d %H:%M:%S").strftime("%H:%M"))
            else:
                messagebox.showerror("Erro", f"Agendamento não encontrado. Código: {response.status_code}")

        def confirmar_edicao():
            cpf_cliente = entry_CPF.get()
            data_original = entry_data_original.get()
            nova_data = entry_nova_data.get()
            novo_horario = entry_novo_horario.get()

            try:
                data_obj = datetime.strptime(nova_data, "%d/%m/%Y")
                horario_obj = datetime.strptime(novo_horario, "%H:%M")
                data_agendamento_str = datetime.combine(data_obj, horario_obj.time()).strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                messagebox.showerror("Erro", "Formato de data ou horário inválido. Use dd/mm/yyyy para a data e HH:MM para o horário.")
                return

            response = requests.get(f"http://localhost:5000/agendamentos/search?cpf_cliente={cpf_cliente}&data_agendamento={datetime.strptime(data_original, '%d/%m/%Y').strftime('%Y-%m-%d')}")
            if response.status_code != 200:
                messagebox.showerror("Erro", "Agendamento original não encontrado.")
                return

            agendamento_id = response.json().get('id')
            data = {
                "data_agendamento": data_agendamento_str
            }

            response = requests.put(f"http://localhost:5000/agendamentos/{agendamento_id}", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Agendamento atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", f"Falha ao atualizar agendamento. Código: {response.status_code}")

        botao_buscar = ctk.CTkButton(frame, text="Buscar Agendamento", font=("Arial", 30), text_color="white",
                                    fg_color='#DF4621', command=buscar_agendamento)
        botao_buscar.pack(after=frame_dados_agendamento, padx=10, pady=15, side='bottom')

        botao_confirmar = ctk.CTkButton(frame, text="Confirmar", font=("Arial", 30), text_color="white",
                                        fg_color='#DF4621', command=confirmar_edicao)
        botao_confirmar.pack(after=frame_dados_agendamento, padx=10, pady=15, side='bottom')

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

    janela.mainloop()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app)
    tkinter_thread = threading.Thread(target=create_interface)

    flask_thread.start()
    tkinter_thread.start()

    flask_thread.join()
    tkinter_thread.join()
