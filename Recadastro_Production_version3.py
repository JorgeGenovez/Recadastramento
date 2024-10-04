import flet as ft
import pandas as pd
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googledrive import df


#CadastrosPIB = pd.read_csv("Projeto Recadastro\\Versão de Produção Recadastro\\Versão de produção 2\\Membros.csv")
TesteCadastroPIB = df

def main(pagina):
    Rc = ft.Text("Recadastramento")
    Usuarios = ["Jorge", "Geovani"]
    Senhas = ["123", "456"]

    #Opção para menu de preenchimento automático
    # Função para atualizar sugestões
    
    sugestoes = ft.Column()

    def atualizar_sugestoes(evento):
        texto_digitado = lista_nomes.value.strip().lower()  # Captura o texto digitado na caixa de texto correta
        sugestoes.controls.clear()  # Limpa as sugestões anteriores
        
        if texto_digitado:  # Se houver texto digitado
            nomes_filtrados = [nome for nome in nomes_completos if nome.lower().startswith(texto_digitado)]
            for nome in nomes_filtrados:
                sugestao = ft.TextButton(nome, on_click=lambda e, n=nome: selecionar_nome(n))  # Cria um botão para cada nome filtrado
                sugestoes.controls.append(sugestao)  # Adiciona o botão à coluna de sugestões
        
        pagina.update()  # Atualiza a página para refletir as mudanças

    def selecionar_nome(nome):
        lista_nomes.value = nome  # Atualiza o campo de entrada com o nome selecionado
        sugestoes.controls.clear()  # Limpa as sugestões após a seleção
        pagina.update()  # Atualiza a página para refletir as mudanças


    nomes_completos = TesteCadastroPIB["Nome Completo"].tolist()
    lista_nomes = ft.TextField(label="Nome Completo", on_change=atualizar_sugestoes)

    # Tópicos do Cadastro
    #por foto
    #-------------------------------------------------------------------
    matricula = ft.TextField(label="Matrícula")
    nomecompleto = ft.TextField(label="Nome")
    cpf = ft.TextField(label="CPF")
    datanascimento = ft.TextField(label="Data de Nascimento")


    sexo = ft.Dropdown(
    label="Sexo",
    options=[
        ft.dropdown.Option("Masculino"),
        ft.dropdown.Option("Feminino")
    ],
    value="",  # Valor padrão
        )
    #--------------------------------------
    pai_membro = ft.Dropdown(
    label="Seu pai é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
        )
    #----------------------------------------   
    nome_mae = ft.TextField(label="Nome da Mãe")
    mae_membro = ft.Dropdown(
    label="Sua mãe é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
        )
    #--------------------------------------
    nome_conjuge = ft.TextField(label="Nome do Cônjuge")
    datanascimento_conjuge = ft.TextField(label="Data de Nascimento do Cônjuge")

    conjuge_membro = ft.Dropdown(
    label="Seu cônjuge é membro da PIB Pavuna?",
    options = [
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
        )
    tipo_sanguineo = ft.TextField(label="Tipo Sanguíneo")
    estado_civil = ft.TextField(label="Estado Civil")
    datacasamento = ft.TextField(label="Data do Casamento")
    profissao = ft.TextField(label="Profissão")
    naturalidade = ft.TextField(label="Naturalidade")
    nacionalidade = ft.TextField(label="Nacionalidade")
    rua = ft.TextField(label="Rua")
    complemento = ft.TextField(label="Complemento")
    bairro = ft.TextField(label="Bairro")
    municipio = ft.TextField(label="Município")
    estado = ft.TextField(label="Estado")
    cep = ft.TextField(label="CEP")
    tel_residencial = ft.TextField(label="Telefone Residencial")
    tel_celular = ft.TextField(label="Telefone Celular")
    email = ft.TextField(label="E-mail")
    nome_pai = ft.TextField(label="Nome do Pai")
    cargo_atual = ft.TextField(label = "Cargo Atual")
    databatismo = ft.TextField(label = "Data do Batismo")
    igrejabatismo = ft.TextField(label = "Igreja onde foi bartizado")
    entradaPIB = ft.TextField(label="Quando se Tornou membro PIB?")
    formaentrada = ft.TextField(label = "Como se tornou membro da PIB?")
    #----------------------------------------------------------------------
    #pedir uma foto
    #-------------------------------------------------------------------

    nome_filho1 = (ft.TextField(label="Nome Filho(a) 1"))
    datanascimento_filho1 = (ft.TextField(label="Data de Nascimento do Filho(a) 1"))
    
    filho1_membro = ft.Dropdown(
    label="Seu filho(a) 1 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho2 = (ft.TextField(label="Nome Filho(a) 2"))
    datanascimento_filho2 = (ft.TextField(label="Data de Nascimento do Filho(a) 2"))
    
    filho2_membro = ft.Dropdown(
    label="Seu filho(a) 2 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho3 = (ft.TextField(label="Nome Filho(a) 3"))
    datanascimento_filho3 = (ft.TextField(label="Data de Nascimento do Filho(a) 3"))
    
    filho3_membro = ft.Dropdown(
    label="Seu filho(a) 3 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho4 = (ft.TextField(label="Nome Filho(a) 4"))
    datanascimento_filho4 = (ft.TextField(label="Data de Nascimento do Filho(a) 4"))
    
    filho4_membro = ft.Dropdown(
    label="Seu filho(a) 4 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    nome_filho5 = (ft.TextField(label="Nome Filho(a) 5"))
    datanascimento_filho5 = (ft.TextField(label="Data de Nascimento do Filho(a) 5"))
    
    filho5_membro = ft.Dropdown(
    label="Seu filho(a) 5 é membro da PIB Pavuna?",
    options=[
        ft.dropdown.Option("Sim"),
        ft.dropdown.Option("Não")
    ],
    value="",  # Valor padrão
    )

    def confirmando(evento):
        nomecompleto_valor = nomecompleto.value
        matricula_valor = matricula.value
        cpf_valor = cpf.value
        datanascimento_valor = datanascimento.value
        sexo_valor = sexo.value
        tipo_sanguineo_valor = tipo_sanguineo.value
        estado_civil_valor = estado_civil.value
        datacasamento_valor = datacasamento.value
        profissao_valor = profissao.value
        naturalidade_valor = naturalidade.value
        nacionalidade_valor = nacionalidade.value
        rua_valor = rua.value
        complemento_valor = complemento.value
        bairro_valor = bairro.value
        municipio_valor = municipio.value
        estado_valor = estado.value
        cep_valor = cep.value
        tel_residencial_valor = tel_residencial.value
        tel_celular_valor = tel_celular.value
        email_valor = email.value
        nome_pai_valor = nome_pai.value
        nome_mae_valor = nome_mae.value
        nome_conjuge_valor = nome_conjuge.value
        datanascimento_conjuge_valor = datanascimento_conjuge.value
        cargo_atual_valor = cargo_atual.value
        databatismo_valor = databatismo.value
        igrejabatismo_valor = igrejabatismo.value
        entradaPIB_valor = entradaPIB.value
        formaentrada_valor = formaentrada.value
        pai_membro_valor = pai_membro.value
        mae_membro_valor = mae_membro.value
        conjuge_membro_valor = conjuge_membro.value
        
        nome_filho1_valor = nome_filho1.value
        datanascimento_filho1_valor = datanascimento_filho1.value
        filho1_membro_valor = filho1_membro.value
        
        nome_filho2_valor = nome_filho2.value
        datanascimento_filho2_valor = datanascimento_filho2.value 
        filho2_membro_valor = filho2_membro.value

        nome_filho3_valor = nome_filho3.value
        datanascimento_filho3_valor = datanascimento_filho3.value 
        filho3_membro_valor = filho3_membro.value

        nome_filho4_valor = nome_filho4.value
        datanascimento_filho4_valor = datanascimento_filho4.value 
        filho4_membro_valor = filho4_membro.value

        nome_filho5_valor = nome_filho5.value
        datanascimento_filho5_valor = datanascimento_filho5.value 
        filho5_membro_valor = filho5_membro.value
        #-------------------------------------
        #Definir Campos de preenchimento Obrigatório 
        #-------------------------------------

        SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        SPREADSHEET_ID = "197dGyWjtAVUVR2K8eODfIxfrEFgeErTcxMhp3OIX8N0"
        RANGE_NAME = "Dados!A1:AY3000"

        creds = None

        if os.path.exists("Projeto Recadastro\\Versão de Produção Recadastro\\Versão de produção 2\\token.json"):
            creds = Credentials.from_authorized_user_file("Projeto Recadastro\\Versão de Produção Recadastro\\Versão de produção 2\\token.json", SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "Projeto Recadastro\\Versão de Produção Recadastro\\Versão de produção 2\\credentials.json", SCOPES
                )
                # Use this line instead of run_local_server
                creds = flow.run_console()
        
            with open("Projeto Recadastro\\Versão de Produção Recadastro\\Versão de produção 2\\token.json", "w") as token:
                token.write(creds.to_json())

        # Exemplo de chamada para adicionar dados à planilha
        try:
            # Criar um serviço para interagir com a API do Google Sheets
            service = build("sheets", "v4", credentials=creds)
            sheet = service.spreadsheets()
            
            dados = {
                "Nome Completo": [nomecompleto_valor],
                "Matrícula": [str(matricula_valor)], 
                "CPF": [str(cpf_valor)], 
                "Data de Nascimento": [str(datanascimento_valor)],  
                "Sexo": [str(sexo_valor)],  
                "Tipo Sanguíneo": [str(tipo_sanguineo_valor)],  
                "Estado Civil": [str(estado_civil_valor)],  
                "Data de Casamento": [str(datacasamento_valor)],  
                "Profissão": [str(profissao_valor)],  
                "Naturalidade": [str(naturalidade_valor)], 
                "Nacionalidade": [str(nacionalidade_valor)], 
                "Rua": [str(rua_valor)], 
                "Complemento": [str(complemento_valor)],  
                "Bairro": [str(bairro_valor)], 
                "Município": [str(municipio_valor)],  
                "Estado": [str(estado_valor)],  
                "CEP": [str(cep_valor)],  
                "Tel. Residencial": [str(tel_residencial_valor)],  
                "Tel. Celular": [str(tel_celular_valor)],  
                "E-mail": [str(email_valor)],  
                "Nome do Pai": [str(nome_pai_valor)],  
                "Pai Membro": [str(pai_membro_valor)],
                "Nome da Mãe": [str(nome_mae_valor)], 
                "Mãe Membro": [str(mae_membro_valor)],
                "Nome do Conjuge":[str(nome_conjuge_valor)],
                "Data de Nascimento Conjuge": [str(datanascimento_conjuge_valor)],
                "Conjuge Membro": [str(conjuge_membro_valor)],
                "Cargo atual": [str(cargo_atual_valor)],
                "Data Batismo": [str(databatismo_valor)],
                "Igreja Batismo":[str(igrejabatismo_valor)],
                "Data de Entrada PIB": [str(entradaPIB_valor)],
                "Forma de entrada": [str(formaentrada_valor)],
                "Nome do filho(a) 1": [str(nome_filho1_valor)],
                "Data de Nascimento do filho(a) 1": [str(datanascimento_filho1_valor)],
                "Seu filho(a) 1 é membro da PIB Pavuna?": [str(filho1_membro_valor)],
                "Nome do filho(a) 2": [str(nome_filho2_valor)],
                "Data de Nascimento do filho(a) 2": [str(datanascimento_filho2_valor)],
                "Seu filho(a) 2 é membro da PIB Pavuna?": [str(filho2_membro_valor)],
                "Nome do filho(a) 3": [str(nome_filho3_valor)],
                "Data de Nascimento do filho(a) 3": [str(datanascimento_filho3_valor)],
                "Seu filho(a) 3 é membro da PIB Pavuna?": [str(filho3_membro_valor)],
                "Nome do filho(a) 4": [str(nome_filho4_valor)],
                "Data de Nascimento do filho(a) 4": [str(datanascimento_filho4_valor)],
                "Seu filho(a) 4 é membro da PIB Pavuna?": [str(filho4_membro_valor)],
                "Nome do filho(a) 5": [str(nome_filho5_valor)],
                "Data de Nascimento do filho(a) 5": [str(datanascimento_filho5_valor)],
                "Seu filho(a) 5 é membro da PIB Pavuna?": [str(filho5_membro_valor)]
            }

            # Convertendo para a lista de valores
            valores = [
                [v[0] for v in dados.values()]  # Mantém os valores como strings
            ]


            # Print the values to debug
            print("Valores a serem adicionados:", valores)

            # Append the values to the sheet
            request = sheet.values().append(
                spreadsheetId=SPREADSHEET_ID,
                range=RANGE_NAME,
                valueInputOption="RAW",
                insertDataOption="INSERT_ROWS",
                body={"values": valores},
            )
            response = request.execute()

            print(f"Dados adicionados com sucesso: {response}")

        except HttpError as error:
            print(f"An error occurred: {error}")

 
        #--------------------------------------------------
        nomecompleto.value = ""
        matricula.value = ""
        cpf.value = ""
        datanascimento.value = ""
        tipo_sanguineo.value = ""
        estado_civil.value = ""
        datacasamento.value = ""
        profissao.value = ""
        naturalidade.value = ""
        nacionalidade.value = ""
        rua.value = ""
        complemento.value = ""
        bairro.value = ""
        municipio.value = ""
        estado.value = ""
        cep.value = ""
        tel_residencial.value = ""
        tel_celular.value = ""
        email.value = ""
        nome_pai.value = ""
        nome_mae.value = ""
        nome_conjuge.value = ""
        datanascimento_conjuge.value = ""
        cargo_atual.value = ""
        databatismo.value = ""
        igrejabatismo.value = ""
        entradaPIB.value = ""
        formaentrada.value = ""
        sexo.value = ""
        pai_membro.value = ""
        mae_membro.value =  ""
        conjuge_membro.value = ""
        nome_filho1.value = ""
        datanascimento_filho1.value = ""
        filho1_membro.value = ""
        nome_filho2.value = ""
        datanascimento_filho2.value = ""
        filho2_membro.value = ""
        nome_filho3.value = ""
        datanascimento_filho3.value = ""
        filho3_membro.value = ""
        nome_filho4.value = ""
        datanascimento_filho4.value = ""
        filho4_membro.value = ""
        nome_filho5.value = ""
        datanascimento_filho5.value = ""
        filho5_membro.value = ""

        pagina.update()
        janela_recadastro.open = False
        concluir_janela.open = True
        pagina.update()
    Confirmar = ft.ElevatedButton("Confirmar", on_click=confirmando)

    def autopreencher(evento):
        nome_inserido = lista_nomes.value.strip()  # Obter o valor do campo
        if (TesteCadastroPIB["Nome Completo"] == nome_inserido).any():
            indice = TesteCadastroPIB[TesteCadastroPIB["Nome Completo"] == nome_inserido].index[0]  # Obter o primeiro índice correspondente
            
            nomecompleto.value = TesteCadastroPIB["Nome Completo"].iloc[indice]
            matricula.value = TesteCadastroPIB["Matrícula"].iloc[indice]
            cpf.value = TesteCadastroPIB["CPF"].iloc[indice]
            datanascimento.value = TesteCadastroPIB["Data de Nascimento"].iloc[indice]
            tipo_sanguineo.value = TesteCadastroPIB["Tipo Sanguíneo"].iloc[indice]
            estado_civil.value = TesteCadastroPIB["Estado Civil"].iloc[indice]
            datacasamento.value = TesteCadastroPIB["Data de Casamento"].iloc[indice]
            profissao.value = TesteCadastroPIB["Profissão"].iloc[indice]
            naturalidade.value = TesteCadastroPIB["Naturalidade"].iloc[indice]
            nacionalidade.value = TesteCadastroPIB["Nacionalidade"].iloc[indice]
            rua.value = TesteCadastroPIB["Rua"].iloc[indice]
            complemento.value = TesteCadastroPIB["Complemento"].iloc[indice]
            bairro.value = TesteCadastroPIB["Bairro"].iloc[indice]
            municipio.value = TesteCadastroPIB["Cidade"].iloc[indice]
            estado.value = TesteCadastroPIB["Estado"].iloc[indice]
            cep.value = TesteCadastroPIB["CEP"].iloc[indice]
            tel_residencial.value = TesteCadastroPIB["Tel. Residencial"].iloc[indice]
            tel_celular.value = TesteCadastroPIB["Celular"].iloc[indice]
            email.value = TesteCadastroPIB["e-mail"].iloc[indice]
            nome_pai.value = TesteCadastroPIB["Nome do Pai"].iloc[indice]
            nome_mae.value = TesteCadastroPIB["Nome da Mãe"].iloc[indice]
            nome_conjuge.value = TesteCadastroPIB["Nome"].iloc[indice]
            datanascimento_conjuge.value = TesteCadastroPIB["Nascimento"].iloc[indice]
            cargo_atual.value = TesteCadastroPIB["Cargo Atual"].iloc[indice]
            databatismo.value = TesteCadastroPIB["Databatismo"].iloc[indice]
            igrejabatismo.value = TesteCadastroPIB["Igreja"].iloc[indice]
            entradaPIB.value = TesteCadastroPIB["Data Membro"].iloc[indice]
            formaentrada.value = TesteCadastroPIB["Modo"].iloc[indice]
    
            pagina.update()       
    
    # Criação da janela de recadastramento com scroll
    janela_recadastro = ft.AlertDialog(
    title=Rc,
    content=ft.Column(
        controls=[
            ft.Row(controls=[
                ft.Column(controls=[
                    matricula, nomecompleto, cpf,
                    datanascimento, sexo, tipo_sanguineo, 
                    estado_civil, datacasamento, profissao, 
                    naturalidade, nacionalidade,rua, complemento,
                    bairro, municipio, estado, cep, tel_residencial,
                    tel_celular, email, nome_pai, pai_membro,
                    nome_mae, mae_membro, nome_conjuge,
                    datanascimento_conjuge, conjuge_membro,
                    cargo_atual, databatismo, igrejabatismo,
                    entradaPIB, formaentrada, 
                    nome_filho1, datanascimento_filho1, filho1_membro, 
                    nome_filho2, datanascimento_filho2, filho2_membro,
                    nome_filho3, datanascimento_filho3, filho3_membro,
                    nome_filho4, datanascimento_filho4, filho4_membro,
                    nome_filho5, datanascimento_filho5, filho5_membro
                ]),
            ]),
            Confirmar
        ],
        scroll=True,
        width=300  # Define uma largura específica, mas ainda assim flexível
    )
    )
    pagina.overlay.append(janela_recadastro)
    # Função para abrir a janela de recadastramento
    def Recadastro(evento):
        pagina.overlay.append(janela_recadastro)  # Atribui a janela à página
        janela_recadastro.open = True  # Abre a janela
        pagina.update()  # Atualiza a página

    Iniciar_cadastro = ft.ElevatedButton("Cadastro", on_click=Recadastro)
    Completar = ft.ElevatedButton("Autopreenchimento", on_click=autopreencher)

    # LOGIN
    def Verificar(evento):
        if Nome_usuario.value in Usuarios:
            if Senha.value in Senhas:
                if Senhas.index(Senha.value) == Usuarios.index(Nome_usuario.value):
                    Nome_usuario.value = ""
                    Senha.value = ""
                    pagina.remove(Rc)
                    pagina.remove(botao_iniciar)
                    janela.open = False
                    pagina.add(lista_nomes)
                    pagina.add(sugestoes)
                    pagina.add(Completar)
                    pagina.add(Iniciar_cadastro)
                    
                    pagina.update()
                else:
                    Senha.value = "Senha Inválida"
                    pagina.update()                 
            else:
                Senha.value = "Senha Inválida"
                pagina.update()
        else:
            Nome_usuario.value = "Usuário Inválido"
            Senha.value = ""
            pagina.update()
#------------------------------------------------------------
#Janela confirmação de cadastro feito

    def fechar_ok(evento):
            concluir_janela.open = False
            pagina.update()

    titulo_concluir = ft.Text("Cadastro concluído")
    ok = ft.ElevatedButton("OK", on_click=fechar_ok)

    concluir_janela = ft.AlertDialog(
        title = titulo_concluir,
        actions=[ok]
    )
    pagina.overlay.append(concluir_janela)

#------------------------------------------------------------
#Janela Login
    titulo_janela = ft.Text("Bem-vindo ao sistema de Recadastramento")
    Nome_usuario = ft.TextField(label="Usuário")
    Senha = ft.TextField(label="Senha")
    botao_entrar = ft.ElevatedButton("Acessar Sistema", on_click=Verificar)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=ft.Column(controls=[Nome_usuario, Senha]),
        actions=[botao_entrar]
    )
    
    # Função para abrir a janela de login
    def Abrir_popup(evento):
        pagina.overlay.append(janela)
        janela.open = True
        pagina.update()   

    
    botao_iniciar = ft.ElevatedButton("Login", on_click=Abrir_popup)
    pagina.add(Rc)
    pagina.add(botao_iniciar)

    # Função para verificar e modificar os valores vazios, interrompendo o processo

ft.app(main)