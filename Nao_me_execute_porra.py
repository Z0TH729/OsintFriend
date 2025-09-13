import webbrowser
import platform
import time

def detectar_dispositivo():
    sistema = platform.system().lower()
    arquitetura = platform.machine().lower()
    
    if 'linux' in sistema and 'android' in arquitetura:
        return "Android"
    elif 'linux' in sistema:
        return "Linux"
    elif 'windows' in sistema:
        return "Windows"
    elif 'darwin' in sistema:
        return "macOS/iOS"
    else:
        return "Desconhecido"

def redirecionar_instagram():
    url = "https://www.instagram.com/z0th729/"
    dispositivo = detectar_dispositivo()
    
    print(f"📱 Dispositivo detectado: {dispositivo}")
    print(f"🔗 URL: {url}")
    print("⏳ Abrindo navegador...")
    
    try:
        # Abre no navegador padrão
        webbrowser.open(url)
        print("✅ Navegador aberto com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("\n📋 Se não abrir automaticamente, copie o link:")
        print(url)
    
    # Pausa para ver a mensagem
    time.sleep(2)

if __name__ == "__main__":
    print("=" * 50)
    print("        REDIRECIONADOR PARA INSTAGRAM")
    print("=" * 50)
    
    redirecionar_instagram()
    
    print("\n🎉 Redirecionamento concluído!")
    input("Pressione Enter para sair...")
