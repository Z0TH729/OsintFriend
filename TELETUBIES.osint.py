import time
import os
import webbrowser
import random
import sys
import requests
import json
import socket
import re
from bs4 import BeautifulSoup
import phonenumbers
from phonenumbers import carrier, timezone, geocoder
import ipaddress

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_logo_teletubbies_sangue():
    print("\033[1;31m")  # Cor vermelha
    print("🩸" * 60)
    print("🩸                                                          🩸")
    print("🩸    ████████╗███████╗██╗     ███████╗███████╗████████╗    🩸")
    print("🩸    ╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝    🩸")
    print("🩸       ██║   █████╗  ██║     █████╗  ███████╗   ██║       🩸")
    print("🩸       ██║   ██╔══╝  ██║     ██╔══╝  ╚════██║   ██║       🩸")
    print("🩸       ██║   ███████╗███████╗███████╗███████║   ██║       🩸")
    print("🩸       ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝   ╚═╝       🩸")
    print("🩸                                                          🩸")
    print("🩸    ██████╗ ███████╗███╗   ██╗███████╗███████╗████████╗   🩸")
    print("🩸    ██╔═══██╗██╔════╝████╗  ██║██╔════╝██╔════╝╚══██╔══╝   🩸")
    print("🩸    ██║   ██║███████╗██╔██╗ ██║███████╗███████╗   ██║      🩸")
    print("🩸    ██║   ██║╚════██║██║╚██╗██║╚════██║╚════██║   ██║      🩸")
    print("🩸    ╚██████╔╝███████║██║ ╚████║███████║███████║   ██║      🩸")
    print("🩸     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝   ╚═╝      🩸")
    print("🩸                                                          🩸")
    print("🩸               [ DEEP WEB INVESTIGATION TOOL ]            🩸")
    print("🩸                     🩸 SANGUE E OSINT 🩸                 🩸")
    print("🩸" * 60)
    print("\033[0m")  # Resetar cor
    time.sleep(2)

def animacao_carregamento_escuro():
    frases_ameacadoras = [
        "🩸 Conectando-se aos servidores ocultos...",
        "🔪 Acessando bancos de dados não listados...",
        "💀 Quebrando firewalls...",
        "🖤 Bypassando protocolos de segurança...",
        "🩸 Coletando informações sensíveis...",
        "🔪 Rastreando identidades...",
        "💀 Analisando pegadas digitais...",
        "🖤 Acessando câmeras e microfones...",
        "🩸 Monitorando conexões...",
        "🔪 Preparando injeção de dados..."
    ]
    
    for frase in frases_ameacadoras:
        print(f"\033[1;31m▌\033[0m \033[1;37m{frase}\033[0m")
        time.sleep(random.uniform(0.2, 0.6))
        if random.random() > 0.6:
            print(f"\033[1;31m⚠️  ALERTA: Sua atividade está sendo monitorada\033[0m")
            time.sleep(0.3)
        if random.random() > 0.8:
            print(f"\033[1;31m🔴 SISTEMA DETECTOU ANOMALIA\033[0m")
            time.sleep(0.4)

def animacao_teletubbies_sombria():
    print("\n\033[1;31m" + "🔴" * 60)
    print("   Tinky Winky, Dipsy, Laa-Laa, Po estão observando...")
    print("💀 Eles sabem tudo sobre você 💀")
    print("🔴" * 60 + "\033[0m")
    
    personagens = [
        ("👁‍🗨 Tinky Winky", "Roxo", "Bolsa Mágica - Coleta dados de sangue"),
        ("👁‍🗨 Dipsy", "Verde", "Chapéu - Acesso a sistemas vitais"),
        ("👁‍🗨 Laa-Laa", "Amarelo", "Bola - Monitoramento em tempo real"), 
        ("👁‍🗨 Po", "Vermelho", "Patinete - Rastreamento de localização"),
        ("💀 Sol Baby", "Dourado", "Observa tudo, sempre - Controle total")
    ]
    
    for nome, cor, item in personagens:
        print(f"\033[1;31m{nome} ({cor}) - {item}\033[0m")
        time.sleep(0.5)
        if random.random() > 0.7:
            print(f"\033[1;31m🔴 SINAL DE ALERTA: ACTIVADO\033[0m")

def mostrar_teletubby_morto():
    print("\033[1;31m")  # Cor vermelha
    print("    ╔══════════════════════════════════════════╗")
    print("    ║               💀 TELLETUBBY MORTO 💀     ║")
    print("    ║      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      ║")
    print("    ║      █                            █      ║")
    print("    ║      █    ████████████████████    █      ║")
    print("    ║      █    █                  █    █      ║")
    print("    ║      █    █    X        X    █    █      ║")
    print("    ║      █    █                  █    █      ║")
    print("    ║      █    █       ----       █    █      ║")
    print("    ║      █    █                  █    █      ║")
    print("    ║      █    ████████████████████    █      ║")
    print("    ║      █                            █      ║")
    print("    ║      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀      ║")
    print("    ║                                           ║")
    print("    ║        死はただ始まりにすぎない           ║")
    print("    ║      (Shi wa tada hajimari ni suginai)    ║")
    print("    ║        'A morte é apenas o começo'        ║")
    print("    ║                                           ║")
    print("    ╚══════════════════════════════════════════╝")
    print("\033[0m")  # Resetar cor
    time.sleep(3)

def aviso_legal_teletubbies():
    print("\033[1;31m")  # Cor vermelha
    print("🔴" * 60)
    print("🔴                ⚠️ AVISO LEGAL ⚠️                 🔴")
    print("🔴" * 60)
    print("🔴 • Esta ferramenta acessa informações restritas   🔴")
    print("🔴 • Sua atividade está sendo monitorada            🔴")
    print("🔴 • Use com extrema cautela                        🔴")
    print("🔴 • Não nos responsabilizamos por uso indevido     🔴")
    print("🔴 • Conexão anônima é ilusória                     🔴")
    print("🔴 • Todas as funcionalidades são ilegais           🔴")
    print("🔴 • Você assume total responsabilidade             🔴")
    print("🔴 • Sistemas podem contra-atacar                   🔴")
    print("🔴 • Seus dados já foram comprometidos              🔴")
    print("🔴" * 60)
    print("\033[0m")  # Resetar cor
    
    for i in range(5, 0, -1):
        print(f"\033[1;31m🔴 INICIANDO EM {i}... SEUS DADOS JÁ ESTÃO COMPROMETIDOS\033[0m")
        time.sleep(0.7)
    
    print("\033[1;31m🔴 CONEXÃO SEGURA ESTABELECIDA (MENTIRA)\033[0m")
    time.sleep(1)

# Tinky Winky - Pesquisa de nicks e nomes aprofundada
def tinky_winky_pesquisa_nicks():
    limpar_tela()
    print("\033[1;35m" + "🟣" * 60)  # Roxo para Tinky Winky
    print("           TINKY WINKY - PESQUISA DE NICKS           ")
    print("🟣" * 60 + "\033[0m")
    
    username = input("\n🔪 Digite o username para pesquisa avançada: ").strip()
    
    if not username:
        print("\033[1;31m💀 Identidade não fornecida! Abortando...\033[0m")
        time.sleep(1)
        return
    
    print(f"\n\033[1;35m🔪 TINKY WINKY BUSCA: {username}\033[0m")
    print("\033[1;35m" + "🟣" * 60 + "\033[0m")
    
    for i in range(5):
        print(f"\033[1;35m🩸 Buscando em bancos de dados {'.' * (i+1)}\033[0m")
        time.sleep(0.3)
    
    # Lista de plataformas para pesquisa (adicionado Discord)
    plataformas = [
        ("Google", f"https://www.google.com/search?q={username}"),
        ("Instagram", f"https://www.instagram.com/{username}/"),
        ("Facebook", f"https://www.facebook.com/{username}"),
        ("Twitter", f"https://twitter.com/{username}"),
        ("Discord", f"https://discord.com/users/{username}"),
        ("Telegram", f"https://t.me/{username}"),
        ("LinkedIn", f"https://www.linkedin.com/in/{username}"),
        ("GitHub", f"https://github.com/{username}"),
        ("TikTok", f"https://www.tiktok.com/@{username}"),
        ("YouTube", f"https://www.youtube.com/@{username}"),
        ("Reddit", f"https://www.reddit.com/user/{username}"),
        ("Pinterest", f"https://www.pinterest.com/{username}"),
        ("Twitch", f"https://www.twitch.tv/{username}"),
        ("Steam", f"https://steamcommunity.com/id/{username}"),
        ("VK", f"https://vk.com/{username}"),
        ("Social Searcher", f"https://www.socialsearcher.com/search/?q={username}"),
        ("Namechk", f"https://namechk.com/?q={username}"),
        ("DuckDuckGo", f"https://duckduckgo.com/?q={username}"),
        ("Archive.org", f"https://archive.org/search.php?query={username}")
    ]
    
    print("\n\033[1;35m🩸 PLATAFORMAS DE PESQUISA DISPONÍVEIS:\n\033[0m")
    
    for i, (plataforma, url) in enumerate(plataformas, 1):
        print(f"\033[1;35m{i:2d}. {plataforma}")
        print(f"    💀 {url}\n\033[0m")
        time.sleep(0.1)
    
    try:
        escolha = int(input("\n🔪 Escolha uma plataforma para acessar (0 para voltar): "))
        
        if escolha == 0:
            return
        elif 1 <= escolha <= len(plataformas):
            plataforma, url = plataformas[escolha-1]
            print(f"\n\033[1;35m🩸 Acessando {plataforma}...\033[0m")
            
            for _ in range(3):
                print("\033[1;35m🔴 Estabelecendo conexão insegura...\033[0m")
                time.sleep(0.5)
            
            webbrowser.open(url)
        else:
            print("\033[1;31m💀 Plataforma não encontrada!\033[0m")
    except ValueError:
        print("\033[1;31m💀 Entrada inválida!\033[0m")
    
    input("\n🩸 Pressione Enter para voltar...")

# Dipsy - Pesquisa de email aprofundada
def dipsy_pesquisa_email():
    limpar_tela()
    mostrar_teletubby_morto()  # Mostra o Teletubby morto no segundo menu
    print("\033[1;32m" + "🟢" * 60)  # Verde para Dipsy
    print("           DIPSY - PESQUISA DE EMAIL           ")
    print("🟢" * 60 + "\033[0m")
    
    email = input("\n🔪 Digite o e-mail para pesquisa: ").strip()
    
    if not email or "@" not in email:
        print("\033[1;31m💀 E-mail inválido!\033[0m")
        time.sleep(1)
        return
    
    print(f"\n\033[1;32m🔪 DIPSY ANALISA: {email}\033[0m")
    print("\033[1;32m" + "🟢" * 60 + "\033[0m")
    
    for i in range(5):
        print(f"\033[1;32m🩸 Cruzando dados com vazamentos {i+1}/5\033[0m")
        time.sleep(0.5)
    
    # Lista de plataformas para pesquisa de email
    plataformas_email = [
        ("Google", f"https://www.google.com/search?q={email}"),
        ("Social Searcher", f"https://www.socialsearcher.com/search/?q={email}"),
        ("Have I Been Pwned", f"https://haveibeenpwned.com/account/{email}"),
        ("Email Format", f"https://www.emailformat.com/i/{email}"),
        ("Hunter.io", f"https://hunter.io/email-verifier/{email}"),
        ("DuckDuckGo", f"https://duckduckgo.com/?q={email}"),
        ("Archive.org", f"https://archive.org/search.php?query={email}"),
        ("BreachDirectory", f"https://breachdirectory.org/#{email}"),
        ("Epieos", f"https://epieos.com/?q={email}"),
        ("EmailRep", f"https://emailrep.io/{email}")
    ]
    
    print("\n\033[1;32m🩸 FONTES DE PESQUISA DE EMAIL:\n\033[0m")
    
    for i, (plataforma, url) in enumerate(plataformas_email, 1):
        print(f"\033[1;32m{i:2d}. {plataforma}")
        print(f"    💀 {url}\n\033[0m")
        time.sleep(0.1)
    
    try:
        escolha = int(input("\n🔪 Escolha uma plataforma para acessar (0 para voltar): "))
        
        if escolha == 0:
            return
        elif 1 <= escolha <= len(plataformas_email):
            plataforma, url = plataformas_email[escolha-1]
            print(f"\n\033[1;32m🩸 Acessando {plataforma}...\033[0m")
            
            for _ in range(3):
                print("\033[1;32m🔴 Estabelecendo conexão insegura...\033[0m")
                time.sleep(0.5)
            
            webbrowser.open(url)
        else:
            print("\033[1;31m💀 Plataforma não encontrada!\033[0m")
    except ValueError:
        print("\033[1;31m💀 Entrada inválida!\033[0m")
    
    input("\n🩸 Pressione Enter para voltar...")

# Laa-Laa - Pesquisa de números de telefone
def laalaa_pesquisa_telefone():
    limpar_tela()
    print("\033[1;33m" + "🟡" * 60)  # Amarelo para Laa-Laa
    print("           LAA-LAA - PESQUISA DE TELEFONE           ")
    print("🟡" * 60 + "\033[0m")
    
    telefone = input("\n🔪 Digite o número de telefone (com DDD): ").strip()
    
    if not telefone:
        print("\033[1;31m💀 Número não fornecido!\033[0m")
        time.sleep(1)
        return
    
    print(f"\n\033[1;33m🔪 LAA-LAA ANALISA: {telefone}\033[0m")
    print("\033[1;33m" + "🟡" * 60 + "\033[0m")
    
    try:
        # Analisar número com phonenumbers
        parsed_number = phonenumbers.parse(telefone, "BR")
        
        print(f"📞 Número válido: {phonenumbers.is_valid_number(parsed_number)}")
        print(f"🌍 Região: {geocoder.description_for_number(parsed_number, 'pt')}")
        print(f"📱 Operadora: {carrier.name_for_number(parsed_number, 'pt')}")
        
        timezones = timezone.time_zones_for_number(parsed_number)
        if timezones:
            print(f"⏰ Fuso horário: {', '.join(timezones)}")
        
        print(f"🔢 Tipo: {phonenumbers.number_type(parsed_number)}")
        print(f"🌐 Formato internacional: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        
    except Exception as e:
        print(f"\033[1;31m💀 Erro ao analisar número: {e}\033[0m")
    
    # Lista de plataformas para pesquisa de telefone
    plataformas_telefone = [
        ("Google", f"https://www.google.com/search?q={telefone}"),
        ("Truecaller", f"https://www.truecaller.com/search/br/{telefone}"),
        ("Sync.me", f"https://sync.me/pt-BR/search/?number={telefone}"),
        ("Facebook", f"https://www.facebook.com/search/top/?q={telefone}"),
        ("Instagram", f"https://www.instagram.com/search/?q={telefone}"),
        ("Discord", f"https://discord.com/users/{telefone}"),
        ("Telegram", f"https://t.me/{telefone}"),
        ("DuckDuckGo", f"https://duckduckgo.com/?q={telefone}"),
        ("Archive.org", f"https://archive.org/search.php?query={telefone}")
    ]
    
    print("\n\033[1;33m🩸 FONTES DE PESQUISA DE TELEFONE:\n\033[0m")
    
    for i, (plataforma, url) in enumerate(plataformas_telefone, 1):
        print(f"\033[1;33m{i:2d}. {plataforma}")
        print(f"    💀 {url}\n\033[0m")
        time.sleep(0.1)
    
    try:
        escolha = int(input("\n🔪 Escolha uma plataforma para acessar (0 para voltar): "))
        
        if escolha == 0:
            return
        elif 1 <= escolha <= len(plataformas_telefone):
            plataforma, url = plataformas_telefone[escolha-1]
            print(f"\n\033[1;33m🩸 Acessando {plataforma}...\033[0m")
            
            for _ in range(3):
                print("\033[1;33m🔴 Estabelecendo conexão insegura...\033[0m")
                time.sleep(0.5)
            
            webbrowser.open(url)
        else:
            print("\033[1;31m💀 Plataforma não encontrada!\033[0m")
    except ValueError:
        print("\033[1;31m💀 Entrada inválida!\033[0m")
    
    input("\n🩸 Pressione Enter para voltar...")

# Po - Pesquisa de CPF
def po_pesquisa_cpf():
    limpar_tela()
    print("\033[1;31m" + "🔴" * 60)  # Vermelho para Po
    print("           PO - PESQUISA DE CPF           ")
    print("🔴" * 60 + "\033[0m")
    
    cpf = input("\n🔪 Digite o CPF (apenas números): ").strip()
    
    if not cpf:
        print("\033[1;31m💀 CPF não fornecido!\033[0m")
        time.sleep(1)
        return
    
    # Validar CPF manualmente
    def validar_cpf(cpf):
        # Remove caracteres não numéricos
        cpf = ''.join(filter(str.isdigit, cpf))
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        
        # Calcula o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto
        
        # Calcula o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto
        
        # Verifica se os dígitos calculados conferem com os informados
        return int(cpf[9]) == digito1 and int(cpf[10]) == digito2
    
    print(f"\n\033[1;31m🔪 PO ANALISA: {cpf}\033[0m")
    print("\033[1;31m" + "🔴" * 60 + "\033[0m")
    
    if validar_cpf(cpf):
        print("✅ CPF válido")
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        print(f"📄 CPF formatado: {cpf_formatado}")
    else:
        print("❌ CPF inválido")
    
    # Lista de plataformas para pesquisa de CPF
    plataformas_cpf = [
        ("Google", f"https://www.google.com/search?q={cpf}"),
        ("Consulta CPF", f"https://consulta-cpf.com/?cpf={cpf}"),
        ("Serasa", "https://www.serasa.com.br/"),
        ("Receita Federal", "https://www.gov.br/receitafederal/pt-br"),
        ("DuckDuckGo", f"https://duckduckgo.com/?q={cpf}"),
        ("Archive.org", f"https://archive.org/search.php?query={cpf}")
    ]
    
    print("\n\033[1;31m🩸 FONTES DE PESQUISA DE CPF:\n\033[0m")
    
    for i, (plataforma, url) in enumerate(plataformas_cpf, 1):
        print(f"\033[1;31m{i:2d}. {plataforma}")
        print(f"    💀 {url}\n\033[0m")
        time.sleep(0.1)
    
    try:
        escolha = int(input("\n🔪 Escolha uma plataforma para acessar (0 para voltar): "))
        
        if escolha == 0:
            return
        elif 1 <= escolha <= len(plataformas_cpf):
            plataforma, url = plataformas_cpf[escolha-1]
            print(f"\n\033[1;31m🩸 Acessando {plataforma}...\033[0m")
            
            for _ in range(3):
                print("\033[1;31m🔴 Estabelecendo conexão insegura...\033[0m")
                time.sleep(0.5)
            
            webbrowser.open(url)
        else:
            print("\033[1;31m💀 Plataforma não encontrada!\033[0m")
    except ValueError:
        print("\033[1;31m💀 Entrada inválida!\033[0m")
    
    input("\n🩸 Pressione Enter para voltar...")

# Sol Baby - Localização por IP
def sol_baby_localizacao_ip():
    limpar_tela()
    print("\033[1;36m" + "🔵" * 60)  # Azul para Sol Baby
    print("           SOL BABY - LOCALIZAÇÃO POR IP           ")
    print("🔵" * 60 + "\033[0m")
    
    ip = input("\n🔪 Digite o endereço IP: ").strip()
    
    if not ip:
        # Obter IP público automaticaly
        try:
            ip = requests.get('https://api.ipify.org').text
            print(f"🌐 Seu IP público: {ip}")
        except:
            print("\033[1;31m💀 IP não fornecido e não foi possível obter IP automaticamente!\033[0m")
            time.sleep(1)
            return
    
    print(f"\n\033[1;36m🔪 SOL BABY ANALISA: {ip}\033[0m")
    print("\033[1;36m" + "🔵" * 60 + "\033[0m")
    
    try:
        # Verificar se é um IP válido
        ipaddress.ip_address(ip)
        
        # Usar API para geolocalização
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data["status"] == "success":
            print(f"🌍 País: {data.get('country', 'N/A')}")
            print(f"🏙️ Região: {data.get('regionName', 'N/A')}")
            print(f"🏢 Cidade: {data.get('city', 'N/A')}")
            print(f"📮 CEP: {data.get('zip', 'N/A')}")
            print(f"📍 Coordenadas: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
            print(f"⏰ Fuso horário: {data.get('timezone', 'N/A')}")
            print(f"📡 Provedor: {data.get('isp', 'N/A')}")
            print(f"🏢 Organização: {data.get('org', 'N/A')}")
            print(f"📡 AS: {data.get('as', 'N/A')}")
        else:
            print("❌ Não foi possível obter informações do IP")
            
    except ValueError:
        print("❌ Endereço IP inválido")
    except Exception as e:
        print(f"❌ Erro ao obter informações: {e}")
    
    input("\n🩸 Pressione Enter para voltar...")

# Navegação Google via terminal
def navegacao_google_terminal():
    limpar_tela()
    print("\033[1;34m" + "🔵" * 60)  # Azul para Google
    print("           NAVEGAÇÃO GOOGLE NO TERMINAL           ")
    print("🔵" * 60 + "\033[0m")
    
    consulta = input("\n🔪 Digite sua pesquisa no Google: ").strip()
    
    if not consulta:
        print("\033[1;31m💀 Consulta vazia!\033[0m")
        time.sleep(1)
        return
    
    print(f"\n\033[1;34m🔪 BUSCANDO: {consulta}\033[0m")
    print("\033[1;34m" + "🔵" * 60 + "\033[0m")
    
    # Simulação de busca
    for i in range(3):
        print(f"\033[1;34m🔍 Analisando resultados {'.' * (i+1)}\033[0m")
        time.sleep(0.5)
    
    # Abrir no navegador
    url = f"https://www.google.com/search?q={consulta}"
    webbrowser.open(url)
    
    input("\n🩸 Pressione Enter para voltar...")

# Função para pesquisa específica no Discord
def pesquisa_discord():
    limpar_tela()
    print("\033[1;34m" + "🔵" * 60)  # Azul para Discord
    print("           PESQUISA NO DISCORD           ")
    print("🔵" * 60 + "\033[0m")
    
    username = input("\n🔪 Digite o username do Discord: ").strip()
    
    if not username:
        print("\033[1;31m💀 Username não fornecido!\033[0m")
        time.sleep(1)
        return
    
    print(f"\n\033[1;34m🔪 BUSCANDO NO DISCORD: {username}\033[0m")
    print("\033[1;34m" + "🔵" * 60 + "\033[0m")
    
    # Simulação de busca
    for i in range(3):
        print(f"\033[1;34m🔍 Analisando perfil do Discord {'.' * (i+1)}\033[0m")
        time.sleep(0.5)
    
    # Abrir no navegador
    url = f"https://discord.com/users/{username}"
    webbrowser.open(url)
    
    input("\n🩸 Pressione Enter para voltar...")

# Menu principal
def menu_principal():
    while True:
        limpar_tela()
        print("\033[1;31m" + "🔴" * 60)
        print("           TELLETUBBIES DEEP WEB INVESTIGATION           ")
        print("🔴" * 60 + "\033[0m")
        
        print("\n\033[1;35m[1] Tinky Winky - Pesquisa de NICKS\033[0m")
        print("\033[1;32m[2] Dipsy - Pesquisa de EMAIL\033[0m")
        print("\033[1;33m[3] Laa-Laa - Pesquisa de TELEFONE\033[0m")
        print("\033[1;31m[4] Po - Pesquisa de CPF\033[0m")
        print("\033[1;36m[5] Sol Baby - Localização por IP\033[0m")
        print("\033[1;34m[6] Navegação Google\033[0m")
        print("\033[1;34m[7] Pesquisa Discord\033[0m")  # Nova opção
        print("\033[1;30m[0] Sair (Não Recomendado)\033[0m")
        
        print("\n\033[1;31m" + "🔴" * 60 + "\033[0m")
        
        try:
            opcao = int(input("\n🔪 Escolha uma opção: "))
            
            if opcao == 0:
                print("\033[1;31m💀 Saindo... Mas lembre-se, estamos sempre observando.\033[0m")
                time.sleep(2)
                break
            elif opcao == 1:
                tinky_winky_pesquisa_nicks()
            elif opcao == 2:
                dipsy_pesquisa_email()
            elif opcao == 3:
                laalaa_pesquisa_telefone()
            elif opcao == 4:
                po_pesquisa_cpf()
            elif opcao == 5:
                sol_baby_localizacao_ip()
            elif opcao == 6:
                navegacao_google_terminal()
            elif opcao == 7:
                pesquisa_discord()  # Nova função
            else:
                print("\033[1;31m💀 Opção inválida! Tente novamente.\033[0m")
                time.sleep(1)
        except ValueError:
            print("\033[1;31m💀 Entrada inválida! Digite um número.\033[0m")
            time.sleep(1)

# Execução principal
if __name__ == "__main__":
    limpar_tela()
    mostrar_logo_teletubbies_sangue()
    animacao_carregamento_escuro()
    animacao_teletubbies_sombria()
    aviso_legal_teletubbies()
    menu_principal()