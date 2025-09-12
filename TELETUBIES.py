import time
import os
import webbrowser
import random
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_logo_teletubbies():
    print("\033[1;35m")  # Cor roxa
    print("╔══════════════════════════════════════════════════╗")
    print("║                                                  ║")
    print("║           ████████╗███████╗██╗     ███████╗     ║")
    print("║           ╚══██╔══╝██╔════╝██║     ██╔════╝     ║")
    print("║              ██║   █████╗  ██║     ███████╗     ║")
    print("║              ██║   ██╔══╝  ██║     ╚════██║     ║")
    print("║              ██║   ███████╗███████╗███████║     ║")
    print("║              ╚═╝   ╚══════╝╚══════╝╚══════╝     ║")
    print("║                                                  ║")
    print("║          ██████╗ ███████╗███╗   ██╗███████╗     ║")
    print("║         ██╔═══██╗██╔════╝████╗  ██║██╔════╝     ║")
    print("║         ██║   ██║███████╗██╔██╗ ██║███████╗     ║")
    print("║         ██║   ██║╚════██║██║╚██╗██║╚════██║     ║")
    print("║         ╚██████╔╝███████║██║ ╚████║███████║     ║")
    print("║          ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝     ║")
    print("║                                                  ║")
    print("║         [ DEEP WEB INVESTIGATION TOOL ]          ║")
    print("║                                                  ║")
    print("╚══════════════════════════════════════════════════╝")
    print("\033[0m")  # Resetar cor
    time.sleep(2)

def animacao_carregamento_escuro():
    frases_ameacadoras = [
        "Conectando-se aos servidores ocultos...",
        "Acessando bancos de dados não listados...",
        "Quebrando firewalls...",
        "Bypassando protocolos de segurança...",
        "Coletando informações sensíveis...",
        "Rastreando identidades...",
        "Analisando pegadas digitais...",
        "Acessando câmeras e microfones..."
    ]
    
    for frase in frases_ameacadoras:
        print(f"\033[1;31m▌\033[0m \033[0;37m{frase}\033[0m")
        time.sleep(random.uniform(0.3, 0.8))
        if random.random() > 0.7:
            print(f"\033[1;31m⚠  AVISO: Sua atividade está sendo monitorada\033[0m")
            time.sleep(0.5)

def animacao_teletubbies_sombria():
    print("\n\033[1;31m" + "▄" * 60)
    print("   Tinky Winky, Dipsy, Laa-Laa, Po estão observando...")
    print("▀" * 60 + "\033[0m")
    
    personagens = [
        ("👁‍🗨 Tinky Winky", "Roxo", "Bolsa Mágica - Coleta dados"),
        ("👁‍🗨 Dipsy", "Verde", "Chapéu - Acesso a sistemas"),
        ("👁‍🗨 Laa-Laa", "Amarelo", "Bola - Monitoramento em tempo real"),
        ("👁‍🗨 Po", "Vermelho", "Patinete - Rastreamento de localização")
    ]
    
    for nome, cor, item in personagens:
        print(f"\033[1;3{random.randint(1,6)}m{nome} ({cor}) - {item}\033[0m")
        time.sleep(0.7)

def aviso_legal_teletubbies():
    print("\033[1;31m")  # Cor vermelha
    print("╔══════════════════════════════════════════════════╗")
    print("║                 ⚠️ AVISO LEGAL                  ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ • Esta ferramenta acessa informações restritas   ║")
    print("║ • Sua atividade pode ser rastreável              ║")
    print("║ • Use com extrema cautela                        ║")
    print("║ • Não nos responsabilizamos por uso indevido     ║")
    print("║ • Conexão anônima recomendada                    ║")
    print("║ • Algumas funcionalidades podem ser ilegais      ║")
    print("║ • Você assume total responsabilidade             ║")
    print("║ • Sistemas podem contra-atacar                   ║")
    print("╚══════════════════════════════════════════════════╝")
    print("\033[0m")  # Resetar cor
    
    for i in range(3, 0, -1):
        print(f"\033[1;31mIniciando em {i}...\033[0m")
        time.sleep(1)
    
    print("\033[1;32m▌ Conexão segura estabelecida (Talvez...)\033[0m")
    time.sleep(1)

def gerar_links_busca_teletubbies(username):
    print(f"\n\033[1;34m🔍 SISTEMAS PROFUNDOS BUSCAM: {username}\033[0m")
    print("\033[1;34m" + "▄" * 60 + "\033[0m")
    
    for i in range(5):
        print(f"\033[1;35m⏣ Buscando em bancos de dados {'.' * (i+1)}\033[0m")
        time.sleep(0.3)
    
    links = {
        "🌐 Busca Profunda": f"https://www.google.com/search?q={username}",
        "📸 Instagram (Perfis Ocultos)": f"https://www.instagram.com/{username}/",
        "👥 Facebook (Dados Restritos)": f"https://www.facebook.com/{username}",
        "🐦 Twitter (Contas Excluídas)": f"https://twitter.com/{username}",
        "💼 LinkedIn (Histórico Profissional)": f"https://www.linkedin.com/in/{username}",
        "🐱 GitHub (Repositórios Privados)": f"https://github.com/{username}",
        "🎵 TikTok (Dados de Localização)": f"https://www.tiktok.com/@{username}",
        "📺 YouTube (Histórico de Visualização)": f"https://www.youtube.com/@{username}",
        "🔴 Reddit (Posts Deletados)": f"https://www.reddit.com/user/{username}",
        "📌 Pinterest (Interesses)": f"https://www.pinterest.com/{username}",
        "🎮 Twitch (Padrões de Comportamento)": f"https://www.twitch.tv/{username}",
        "🚀 Steam (Histórico de Compras)": f"https://steamcommunity.com/id/{username}",
        "🇷🇺 VK (Conexões Russas)": f"https://vk.com/{username}",
        "🔎 Buscador de Deep Web": f"https://www.socialsearcher.com/search/?q={username}",
        "✅ Verificador de Identidade": f"https://namechk.com/?q={username}",
        "🌌 Fóruns Anônimos": f"https://duckduckgo.com/?q={username}",
        "🕵️‍♂️ Arquivos de Inteligência": f"https://archive.org/search.php?query={username}"
    }
    
    print("\n\033[1;35m⏣ PLATAFORMAS DE VIGILÂNCIA DISPONÍVEIS:\n\033[0m")
    
    for i, (plataforma, url) in enumerate(links.items(), 1):
        print(f"\033[1;3{random.randint(1,6)}m{i:2d}. {plataforma}")
        print(f"    ⚠ {url}\n\033[0m")
        time.sleep(0.1)
    
    return links

def abrir_link_teletubbies(links):
    print("\n\033[1;33m👁‍🗨 O OBSERVADOR quer acessar algum sistema?\033[0m")
    print("Digite o número do sistema ou 0 para voltar")
    
    try:
        escolha = int(input("\n🎯 Sua escolha: "))
        
        if random.random() < 0.15:
            sites_aleatorios = [
                "https://www.unknown.onion",
                "https://www.hiddenwiki.org",
                "https://www.torproject.org",
                "https://www.deeplink.com",
                "https://www.darkweblinks.org"
            ]
            
            url_aleatoria = random.choice(sites_aleatorios)
            print(f"\n\033[1;31m⚠  ALERTA: Redirecionamento não autorizado detectado!\033[0m")
            time.sleep(1)
            print(f"\033[1;31m👁‍🗨 EU CONSIGO TE VER\033[0m")
            time.sleep(2)
            webbrowser.open(url_aleatoria)
            return
        
        if escolha == 0:
            return
        elif 1 <= escolha <= len(links):
            plataforma = list(links.keys())[escolha-1]
            url = list(links.values())[escolha-1]
            print(f"\n\033[1;32m⏣ Acessando {plataforma}...\033[0m")
            
            for _ in range(3):
                print("\033[1;35m⏣ Estabelecendo conexão segura...\033[0m")
                time.sleep(0.5)
            
            print("👁‍🗨 Monitoramento ativado")
            time.sleep(1)
            webbrowser.open(url)
        else:
            print("\033[1;31m❌ Sistema não encontrado! Tente novamente.\033[0m")
    except ValueError:
        print("\033[1;31m❌ Entrada inválida! Sistemas de segurança alertados.\033[0m")

def analisar_username_teletubbies(username):
    print(f"\n\033[1;35m🔍 ANALISANDO PEGADA DIGITAL: {username}\033[0m")
    print("\033[1;35m" + "▄" * 60 + "\033[0m")
    
    for i in range(3):
        print(f"\033[1;36m⏣ Examinando padrões de comportamento {'.' * (i+1)}\033[0m")
        time.sleep(0.7)
    
    comprimento = len(username)
    numeros = sum(c.isdigit() for c in username)
    letras = sum(c.isalpha() for c in username)
    especiais = sum(not c.isalnum() for c in username)
    
    print(f"📏 Comprimento da identidade: {comprimento} caracteres")
    print(f"🔤 Letras identificadas: {letras}")
    print(f"🔢 Números encontrados: {numeros}")
    print(f"✨ Caracteres especiais: {especiais}")
    
    time.sleep(1)
    print("\n🎯 AVALIAÇÃO DE VULNERABILIDADE:")
    
    if comprimento < 4:
        print("   ⚠  Identidade muito fraca (Fácil de comprometer)")
    elif comprimento > 15:
        print("   ⚠  Identidade complexa (Maior superfície de ataque)")
    else:
        print("   ⚠  Identidade moderada (Interessante...)")
    
    if numeros > 3:
        print("   ⚠  Padrão numérico detectado (Possível data significativa)")
    
    if especiais > 2:
        print("   ⚠  Múltiplos caracteres especiais (Tentativa de ofuscação)")
    
    time.sleep(1)
    print(f"\n🔒 Hash de identificação: {abs(hash(username)) % 1000000}")
    print("⚠  Esta identidade foi indexada em nossos sistemas")

def buscar_username_teletubbies():
    limpar_tela()
    print("\033[1;33m" + "▄" * 60)
    print("           SISTEMA DE VIGILÂNCIA TELETUBBIES           ")
    print("▀" * 60 + "\033[0m")
    
    username = input("\n🔍 Digite o username para vigilância: ").strip()
    
    if not username:
        print("\033[1;31m❌ Identidade não fornecida! Abortando...\033[0m")
        time.sleep(1)
        return
    
    animacao_carregamento_escuro()
    
    analisar_username_teletubbies(username)
    
    links = gerar_links_busca_teletubbies(username)
    
    abrir_link_teletubbies(links)
    
    print("\n\033[1;32m👁‍🗨 Vigilância concluída. Arquivos atualizados.\033[0m")
    input("\n⏣ Pressione Enter para retornar ao sistema principal...")

def buscar_email_teletubbies():
    limpar_tela()
    print("\033[1;33m" + "▄" * 60)
    print("           RASTREAMENTO DE IDENTIDADE DIGITAL           ")
    print("▀" * 60 + "\033[0m")
    
    email = input("\n📧 Digite o e-mail para rastreamento: ").strip()
    
    if not email or "@" not in email:
        print("\033[1;31m❌ Identificação de e-mail inválida!\033[0m")
        time.sleep(1)
        return
    
    print(f"\n\033[1;34m🔍 RASTREANDO: {email}\033[0m")
    print("\033[1;34m" + "▄" * 60 + "\033[0m")
    
    for i in range(5):
        print(f"\033[1;35m⏣ Cruzando dados com vazamentos {i+1}/5\033[0m")
        time.sleep(0.5)
    
    links_email = {
        "🌐 Busca Avançada": f"https://www.google.com/search?q={email}",
        "🔎 Rastreador de Pegadas": f"https://www.socialsearcher.com/search/?q={email}",
        "🔒 Verificador de Vazamentos": f"https://haveibeenpwned.com/account/{email}",
        "📧 Análise de Padrão": f"https://www.emailformat.com/i/{email}",
        "🎯 Coletor de Metadados": f"https://hunter.io/email-verifier/{email}",
        "🌌 Fóruns Anônimos": f"https://duckduckgo.com/?q={email}",
        "🕵️‍♂️ Arquivos de Inteligência": f"https://archive.org/search.php?query={email}"
    }
    
    for i, (plataforma, url) in enumerate(links_email.items(), 1):
        print(f"\033[1;3{random.randint(1,6)}m{i}. {plataforma}")
        print(f"   ⚠ {url}\n\033[0m")
    
    input("\n⏣ Pressione Enter para voltar ao sistema principal...")

def informacoes_teletubbies():
    limpar_tela()
    print("\033[1;35m" + "▄" * 60)
    print("           SISTEMA DE INFORMAÇÕES TELETUBBIES           ")
    print("▀" * 60 + "\033[0m")
    
    info = [
        "👁‍🗨 Tinky Winky: Roxo, Bolsa Mágica - Coleta dados",
        "👁‍🗨 Dipsy: Verde, Chapéu - Acesso a sistemas",
        "👁‍🗨 Laa-Laa: Amarelo, Bola - Monitoramento em tempo real", 
        "👁‍🗨 Po: Vermelho, Patinete - Rastreamento de localização",
        "🌞 Sol Baby: Observa tudo, sempre",
        "📺 Teletubbies: Sistema de vigilância avançado",
        "🎯 Objetivo: Coletar e analisar dados digitais"
    ]
    
    for item in info:
        print(f"⏣ {item}")
        time.sleep(0.5)
        if random.random() > 0.8:
            print("\033[1;31m⚠  Atividade detectada nos sistemas...\033[0m")
            time.sleep(0.5)
    
    input("\n⏣ Pressione Enter para voltar...")

def scan_deepweb():
    limpar_tela()
    print("\033[1;31m" + "▄" * 60)
    print("           SCAN DE REDES PROFUNDAS           ")
    print("▀" * 60 + "\033[0m")
    
    print("\n\033[1;35m⏣ Iniciando varredura de redes não indexadas...\033[0m")
    time.sleep(1)
    
    for i in range(10):
        ip = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
        status = random.choice(["VULNERÁVEL", "PROTEGIDO", "OCULTO", "ACESSÍVEL"])
        print(f"⏣ {ip} - {status}")
        time.sleep(0.2)
    
    print("\n\033[1;32m⏣ Varredura concluída. 87% dos sistemas vulneráveis.\033[0m")
    input("\n⏣ Pressione Enter para voltar...")

def menu_principal_teletubbies():
    while True:
        limpar_tela()
        print("\033[1;35m" + "▄" * 60)
        print("           TELETUBBIES OSINT TOOL           ")
        print("▀" * 60 + "\033[0m")
        print("\033[1;36m1. 🔍 Buscar por Username\033[0m")
        print("\033[1;36m2. 📧 Buscar por E-mail\033[0m") 
        print("\033[1;36m3. 🤖 Informações do Sistema\033[0m")
        print("\033[1;36m4. 🌌 Scan Deep Web\033[0m")
        print("\033[1;36m5. ⚠️  Aviso Legal\033[0m")
        print("\033[1;31m6. ❌ Sair\033[0m")
        print("\033[1;35m" + "▄" * 60 + "\033[0m")
        
        opcao = input("\n🎯 Escolha uma opção: ").strip()
        
        if opcao == "1":
            buscar_username_teletubbies()
        elif opcao == "2":
            buscar_email_teletubbies()
        elif opcao == "3":
            informacoes_teletubbies()
        elif opcao == "4":
            scan_deepweb()
        elif opcao == "5":
            aviso_legal_teletubbies()
        elif opcao == "6":
            print("\n\033[1;32m👁‍🗨 Saindo do sistema... Sua atividade foi registrada.\033[0m")
            time.sleep(2)
            break
        else:
            print("\033[1;31m❌ Comando não reconhecido! Tente novamente.\033[0m")
            time.sleep(1)

def main():
    mostrar_logo_teletubbies()
    animacao_teletubbies_sombria()
    aviso_legal_teletubbies()
    menu_principal_teletubbies()

if __name__ == "__main__":
    main()