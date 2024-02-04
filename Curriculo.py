import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

import time

def output_delay():
    time.sleep(2)  

import datetime

data_atual = datetime.date.today()
dia_semana = data_atual.weekday()
dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

print("Bem-vindo à apresentação do meu currículo!")
output_delay()
entrada = input("Meu nome é Arthur, me diga o seu: ")
output_delay()
clear_terminal()
print("Olá,",entrada+"!")
output_delay()
if dia_semana != 'domingo':
    print(f"Espero que esteja tendo uma ótima {dias_semana[dia_semana]}.")
else:
    print(f"Espero que esteja tendo um ótimo {dias_semana[dia_semana]}.")
output_delay()
output_delay()

# Dados pessoais
nome = "Arthur Couto Lima"
idade = 26
email = "arthurcoutolima@gmail.com"
telefone = "+55 13 98189-4841"

# Objetivos Profissionais

objetivos = "Trabalhar na modalidade home office com programação e desenvolvimento de softwares;\n                          Adquirir conhecimento ao longo da experiência para implementar técnicas para melhor performace dos sistemas;\n                          Atuar em projetos colaborativos;\n                          Me especializar, porém expandir meu conhecimento em outras linguagens de programação. "

# Certificados e Cursos

certificado1 = {
    "curso": "Imersão Dev, 7 ª edição",
    "instituicao": "Alura"
}

certificado2 = {
    "curso": "1° lugar na Simulação Empresarial",
    "instituicao": "Universidade São Judas campus Unimonte"
}

certificado3 = {
    "curso": "Power BI Completo – Do Básico ao Avançado",
    "instituicao": "Udemy"
}

certificado4 = {
    "curso": "Business Intelligence, SQL Server, MySQL, Oracle, T-SQL e PLSQL",
    "instituicao": "Udemy"
}

curso1 = {
    "cursando": "Python 3 completo: PySide6, Django, Selenium, Regexp, Testes, TDD, POO, Design Patterns GoF, algoritmos e programação",
    "instituicao": "Udemy"
}
# Experiência profissional
experiencia1 = {
    "cargo": "Mensageiro Setor: Hotelaria/Prédio Comercial",
    "empresa": "Condomínio Praiamar Corporate",
    "periodo": "04/2017 a 03/2019",
    "descricao": "Recebimento e entrega interna de correspondências, encomendas,malotes eremessas;\n           Recebimento e entrega de remessas, malotes e comunicados entre as unidades da sede (Grupo Mendes);\n           Elaboração de um sistema automatizado preliminar (em Excel) de registro de entrada e saída das correspondências, encomendas, malotes e remessas; \n           incluindo: monitoramento gráfico compartilhado.\n           Utilização de sistema interno de protocolo da mensageria;\n           Suporte ao agendamento para uso das salas de reunião, bem como monitoramento e suporte técnico aos usuários;\n           Suporte à recepção;\n           Suporte à administração quanto da recepção e acompanhamento de usuários dos helipontos.\n           Suporte à recepção do setor administrativo;\n           Breve experiência como recepcionista da administração."
}

experiencia2 = {
    "cargo": "Recepcionista",
    "empresa": "Just Fit",
    "periodo": "12/2015 a 07/2016",
    "descricao": "Atendimento ao cliente;\n           Arquivo(organização de contratos);\n           Efetuação de matrículas e cancelamentos;\n           Venda de planos;\n           Elaboração e alimentação de planilhas."
}

experiencia3 = {
    "cargo": "Aprendiz prestando serviços à MSC)",
    "empresa": "CAMPS",
    "periodo": "08/2013 a 11/2014",
    "descricao": "Auxílio ao Departamento de pessoal;\n           Recepção do departamento;\n           Arquivo (controle e arquivamento);\n           Solicitação ao almoxarifado;\n           Entrega de holerites;\n           Troca de bobinas de máquinas de ponto;\n           Realização de planilhas;\n           Montagem de caixas de papelão;\n           Auxílio ao RH;\n           Serviço externo."
}

# Formação acadêmica
formacao1 = {
    "curso": "Bacharelado em Administração",
    "instituicao": "São Judas campus Unimonte - Santos/SP",
    "periodo": "2015 - 2018"
}

# Habilidades
habilidades = "Boa comunicação e escrita;\n           Convivência com equipes;\n           Gerenciamento de pessoas;\n           Bom planejamento;\n           Capacidades de organização;\n           Proatividade;\n           Flexibilidade e capacidade de se adaptar a mudanças"



clear_terminal()
output_delay()
print("Estou finalizando o processamento do currículo, só mais 1 momento...")
output_delay()
clear_terminal()
print(".")
output_delay()
clear_terminal()
print("..")
output_delay()
clear_terminal()
print("...")
output_delay()
clear_terminal()
print("Pronto! Por favor, não se esqueça de digitar 'sair' ao final da leitura.")
output_delay()
print("Aqui está:")
output_delay()
output_delay()
output_delay()

# Imprimir currículo em portugues
print("CURRÍCULO")
print("---------")
print("Nome:", nome)
print("Idade:", idade)
print("Email:", email)
print("Telefone:", telefone)
print("\nObjetivos Profissionais: ", objetivos)
print("\nCertificados: ")
print("Evento: ", certificado1["curso"])
print("Instituição:", certificado1["instituicao"])
print("\nEvento: ", certificado2["curso"])
print("Instituição:", certificado2["instituicao"])
print("\nCurso: ", certificado3["curso"])
print("Instituição:", certificado3["instituicao"])
print("\nCurso: ", certificado4["curso"])
print("Instituição:", certificado4["instituicao"])
print("\nCursando: ", curso1["cursando"])
print("Instituição:", curso1["instituicao"])
print("\nExperiência Profissional:")
print("Cargo:", experiencia1["cargo"])
print("Empresa:", experiencia1["empresa"])
print("Período:", experiencia1["periodo"])
print("Descrição:", experiencia1["descricao"])
print("\nCargo:", experiencia2["cargo"])
print("Empresa:", experiencia2["empresa"])
print("Período:", experiencia2["periodo"])
print("Descrição:", experiencia2["descricao"])
print("\nCargo:", experiencia3["cargo"])
print("Empresa:", experiencia3["empresa"])
print("Período:", experiencia3["periodo"])
print("Descrição:", experiencia3["descricao"])
print("\nFormação Acadêmica:")
print("Curso:", formacao1["curso"])
print("Instituição:", formacao1["instituicao"])
print("Período:", formacao1["periodo"])
print("\nHabilidades:", habilidades)

encerramento = input("Obrigado pela sua atenção, [sair]? ")
encerramento = encerramento.lower()
condicao_1 = "nao"
condicao_2 = "sim"


while True:
   
    if encerramento != "sair":
        output_delay()
        print("Por favor, digite apenas [sair].")
        output_delay()
        clear_terminal()
        encerramento = input("Obrigado pela sua atenção, [sair]? ")
        encerramento = encerramento.lower()

    else:
        break


output_delay()
clear_terminal()
pergunta_1 = input("Entrar em contato com Arthur? ")
pergunta_1 = pergunta_1.lower()
i = 0

while (True and i == 0):

    while (pergunta_1 == "nao" or pergunta_1 == "sim"):
        
        if pergunta_1 == "sim":
            output_delay()
            print("Celular/Whatsapp: +55 13 981894841\n \nE-mail: arthurcoutolima@gmail.com\n \nAguardo o contato\n \nObrigado!")
            i += 1
            break
        
        elif pergunta_1 == "nao":
            output_delay()
            clear_terminal()
            print(".")
            output_delay()
            clear_terminal()
            print("..")
            output_delay()
            clear_terminal()
            print("...")
            output_delay()
            clear_terminal()
            print("Acho que você quis dizer: 'sim'.")
            output_delay()
            step1 = input("Confirmar? ")
            step1 = step1.lower()


            if step1 == "nao":
                output_delay()
                clear_terminal()
                print(".")
                output_delay()
                clear_terminal()
                print("..")
                output_delay()
                clear_terminal()
                print("...")
                output_delay()
                clear_terminal()
                print("\nObrigado por confirmar! Aqui está o contato:\n \nCelular/Whatsapp: +55 13 981894841\n \nE-mail: arthurcoutolima@gmail.com")
                i += 1
            else:
                output_delay()
                print("\nFico feliz que tenha confirmado que sim! Aqui está o contato:\n \nCelular/Whatsapp: +55 13 981894841\n \nE-mail: arthurcoutolima@gmail.com")
                i += 1
            break
        

    else:
        output_delay()
        print("Favor inserir apenas [sim] ou [nao]")
        output_delay()
        clear_terminal()
        pergunta_1 = input("Entrar em contato com Arthur? ")
        pergunta_1 = pergunta_1.lower()