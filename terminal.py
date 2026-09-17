# Alteração realizada na branch terminal-cyber

from colorama import init, Fore
import time

#############################################
#hacker (invasao de usuario)
##################################################



##################################################
# Rotina de login
#################################################
def login():
    login_correto = "admin"
    senha_correta = "1234"

    tentativas = 0
    SenhaCorreta = False
    while SenhaCorreta == False:

        login = input("Login: ")
        senha = input("Senha: ")

        if login == login_correto and senha == senha_correta:
            print("\nAcesso permitido")
            time.sleep(1)

            # TENTANDO ENTRAR NO SISTEMA
            print("Carregando acesso ao sistema...")
            time.sleep(1)

            for i in range(0, 101, 20):
                print("ACCESS CHECK ", i, "%")
                time.sleep(0.4)

            print("\nTentativa de acesso bem-sucedida.\n")
            SenhaCorreta = True            
            time.sleep(1)
            acessar_arquivo()

        else:
            tentativas +=  1
            if tentativas >= 3:
                print(Fore.RED + "\nALERTA DE SEGURANÇA")
                print(Fore.RED + "Muitas tentativas detectadas")
                print(Fore.RED + "IP bloqueado:", ip)
                exit()


##########################
# Funçao para acesso aos arquivos
##########################
def acessar_arquivo():
# TENTANDO ABRIR ARQUIVOS DO SISTEMA
    abrir_arquivo = input("ACCESS SYSTEM FILES? (Y/N): ").lower() #str

    if abrir_arquivo != "y":    
        print(Fore.RED + "\nAcesso ao sistema encerrado.")
        exit()
    else:
        lista_de_arquivos = ["dados.txt", "relatorio.pdf", "banco.docx"]

        print("\nSCANNING SYSTEM DIRECTORY...")
        time.sleep(1)

        for arquivo in lista_de_arquivos:    # Este for mostra a relação dos arquivos da array "lista_de_arquivos"
            print("FILE DETECTED: ", arquivo)
            time.sleep(0.4)

        nome = input("\nFILE NAME ").strip().lower()

        print("\nATTEMPTING FILE ACCESS...")
        time.sleep(1)

        for i in range(0, 101, 20): #imersao 
             print("ACCESS CHECK ", i, "%")
             time.sleep(0.4)

        print("\nACCESS LEVEL: LIMITED \n PROTECTED DATA BLOCKED\n")
        time.sleep(1)

        while True:
            if nome == "relatorio.pdf":
                print(Fore.GREEN + "Dados do cliente: Giovana")
                print("Link do relatório: https://www.exemplo.***\n\n")
                time.sleep(1)
                break
            elif nome == "banco.docx":
                print(Fore.GREEN + "Dados do cliente: Giovana")
                print("Segredo bancário: Cliente VIP")
                print("Conta: 45829  |  Senha do banco: 167\n\n")
                time.sleep(1)
                break
            elif nome == "dados.txt":
                print(Fore.BLUE + "Dados do cliente: Giovana")
                print("Informações pessoais: CPF 123.456.789-00\n\n")
                time.sleep(1)
                break
             

        print(Fore.RED + "[FIREWALL ALERT] SYSTEM BREACH DETECTED] ===============================\n\n")
        #ERRO NO SISTEMA    

        print("ERROR 401 - UNAUTHORIZED ACCESS")
        time.sleep(0.1)

        print("ERROR 403 - ACCESS FORBIDDEN")
        time.sleep(0.1)

        print("ERROR 404 - TARGET FILE NOT FOUND")
        print("ERROR 500 - INTERNAL SERVER ERROR")
        time.sleep(0.1)

        print("ERROR 502 - BAD GATEWAY")
        time.sleep(0.1)

        print("ERROR 503 - SERVICE UNAVAILABLE")
        print("ERROR 504 - GATEWAY TIMEOUT")
        print("[SECURITY MODULE] SUSPICIOUS ACTIVITY DETECTED")
        time.sleep(0.1)

        print("[FIREWALL] SOURCE IP FLAGGED")
        time.sleep(0.1)

        print("[ACCESS CONTROL] PERMISSION DENIED")
        time.sleep(0.1)

        print("[SECURITY ALERT] UNAUTHORIZED FILE ACCESS ATTEMPT")
        print("[PROCESS MANAGER] TERMINATING SESSION")
        time.sleep(1)

        print("\n[FIREWALL] SECURITY BREACH DETECTED")
        print("[FIREWALL] FILE ACCESS BLOCKED")

        exit()


##############################                
# INICIO DO SISTEMA
##############################
init()

print("=== Sistema CMD ===")
ip = "192.168.1.45"

print("\nAtividade de rede detectada")
print("IP:", ip, "\n")

time.sleep(1)
    
login()  # aqui a chamada da função de login 
