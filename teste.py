import tkinter as tk
from tkinter import ttk
import datetime
import calendar
import customtkinter as ctk

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criar a janela principal
janela = ctk.CTk()
janela.geometry("1000x600")
janela.configure(fg_color="#000000")  # Altera a cor de fundo da janela principal para preto

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

    # Configurando os botões principais
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

    subtitulo2 = ctk.CTkLabel(frame, text="Procedimentos", font=("Arial", 18), text_color="white")
    subtitulo2.pack(padx=10, pady=(5, 5))

    unha = ctk.CTkButton(
        frame, text="UNHA", command=clique, width=350, height=50,
        fg_color="#fa7f72", hover_color="lightpink",
        text_color="white", corner_radius=10, border_color="grey", border_width=2,
        font=("Arial", 30, "bold")
    )
    unha.pack(padx=10, pady=10)

    cabelo = ctk.CTkButton(
        frame, text="CABELO", command=clique, width=350, height=50,
        fg_color="#fa7f72", hover_color="lightpink",
        text_color="white", corner_radius=10, border_color="grey", border_width=2,
        font=("Arial", 30, "bold")
    )
    cabelo.pack(padx=10, pady=10)

    sobrancelha = ctk.CTkButton(
        frame, text="SOBRANCELHA", command=clique, width=350, height=50,
        fg_color="#fa7f72", hover_color="lightpink",
        text_color="white", corner_radius=10, border_color="grey", border_width=2,
        font=("Arial", 30, "bold")
    )
    sobrancelha.pack(padx=10, pady=10)

    subtitulo3 = ctk.CTkLabel(frame, text="Atendimento", font=("Arial", 18), text_color="white")
    subtitulo3.pack(padx=10, pady=(5, 5))

    agendar = ctk.CTkButton(
        frame, text="AGENDAR", command=clique, width=350, height=50,
        fg_color="#fa7f72", hover_color="lightpink",
        text_color="white", corner_radius=10, border_color="grey", border_width=2,
        font=("Arial", 30, "bold")
    )
    agendar.pack(padx=10, pady=10)

def configure_frame_direita(parent):
    frame_cor = "#000000"  # Cor do frame à direita
    frame = ctk.CTkFrame(parent, corner_radius=10, fg_color=frame_cor)
    frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Adiciona o calendário interativo no estilo do Outlook
    calendar_frame = tk.Frame(frame, bg="black")
    calendar_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Configurando o calendário interativo
    today = datetime.date.today()
    current_month = today.month
    current_year = today.year

    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    def update_calendar(month, year):
        for widget in calendar_frame.winfo_children():
            widget.destroy()

        calendar_label = tk.Label(calendar_frame, text=f"{months[month - 1]} {year}", font=("Arial", 24), bg="black", fg="white")
        calendar_label.pack(pady=20)

        # Função para lidar com o clique em um dia do calendário
        def day_clicked(day):
            # Cria uma janela para entrada de texto
            entry_window = tk.Toplevel(janela)
            entry_window.geometry("300x150")
            entry_window.title(f"Informações do dia {day}")

            # Texto explicativo
            info_label = tk.Label(entry_window, text=f"Informe as informações para o dia {day}:", font=("Arial", 12))
            info_label.pack(pady=10)

            # Campo de entrada de texto
            info_entry = tk.Entry(entry_window, width=30)
            info_entry.pack(pady=10)

            # Botão para salvar as informações
            def save_info():
                info = info_entry.get()
                # Aqui você pode salvar as informações em algum lugar (banco de dados, arquivo, etc.)
                print(f"Informações para o dia {day} salvas: {info}")
                entry_window.destroy()

            save_button = ttk.Button(entry_window, text="Salvar", command=save_info)
            save_button.pack(pady=10)

        # Configuração do calendário com dias
        days_frame = tk.Frame(calendar_frame, bg="black")
        days_frame.pack()

        # Obtém o número de dias no mês atual usando o módulo calendar
        num_days = calendar.monthrange(year, month)[1]

        day_colors = {
            "Monday": "#2274a5",
            "Tuesday": "#32936f",
            "Wednesday": "#fdae61",
            "Thursday": "#e94f37",
            "Friday": "#1e434c",
            "Saturday": "#b4656f",
            "Sunday": "#465362"
        }

        janela.style = ttk.Style()

        # Cria botões para cada dia do mês
        for day in range(1, num_days + 1):
            day_of_week = calendar.weekday(year, month, day)
            day_name = calendar.day_name[day_of_week]
            janela.style.configure(f"{day_name}.TButton", foreground="white", background=day_colors[day_name], font=("Arial", 12, "bold"))

            day_button = ttk.Button(days_frame, text=str(day), width=10,  # Aumenta a largura dos botões
                                    style=f'{day_name}.TButton',  # Aplica o estilo baseado no dia da semana
                                    command=lambda d=day: day_clicked(d))
            day_button.grid(row=(day - 1) // 7, column=(day - 1) % 7, padx=10, pady=10)  # Aumenta o espaçamento entre os botões

    def prev_month():
        nonlocal current_month, current_year
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
        update_calendar(current_month, current_year)

    def next_month():
        nonlocal current_month, current_year
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
        update_calendar(current_month, current_year)

    # Botões para mudar de mês
    prev_button = ttk.Button(calendar_frame, text="Anterior", command=prev_month)
    prev_button.pack(side="left", padx=10)

    next_button = ttk.Button(calendar_frame, text="Próximo", command=next_month)
    next_button.pack(side="right", padx=10)

    update_calendar(current_month, current_year)

configure_frame_esquerda(janela)
configure_frame_direita(janela)
janela.mainloop()