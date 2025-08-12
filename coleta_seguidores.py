from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random
import json
from datetime import datetime

# Configurações
EMAIL = os.getenv("INSTA_EMAIL")
SENHA = os.getenv("INSTA_PASSWORD")
LISTA_USUARIOS = ["_imcryansp._"]
MAX_SEGUIDORES = 10000  # Ilimitado
MAX_SCROLLS = 500

# Chrome otimizado
PROFILE_PATH = os.path.join(os.getcwd(), "insta_profile")
options = Options()
options.add_argument(f"--user-data-dir={PROFILE_PATH}")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-notifications")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
options.add_argument("--window-size=1366,768")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
wait = WebDriverWait(driver, 15)

def pausa_otima():
    """Pausa otimizada para velocidade máxima segura"""
    time.sleep(random.uniform(1.2, 1.8))

def fazer_login():
    """Login otimizado"""
    try:
        time.sleep(random.uniform(2, 4))
        if "login" not in driver.current_url.lower():
            print("✅ Já logado!")
            return True
        
        print("🔑 Login...")
        username_field = driver.find_element(By.NAME, "username")
        username_field.click()
        username_field.send_keys(EMAIL)
        time.sleep(1)
        
        password_field = driver.find_element(By.NAME, "password")
        password_field.click()
        password_field.send_keys(SENHA)
        time.sleep(1)
        
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(random.uniform(4, 7))
        print("✅ Login OK!")
        return True
    except:
        print("✅ Sessão mantida!")
        return True

def remover_popups():
    """Remove popups rapidamente"""
    try:
        for button_xpath in ["//button[contains(text(), 'Agora não')]", "//button[contains(text(), 'Not Now')]"]:
            try:
                button = driver.find_element(By.XPATH, button_xpath)
                button.click()
                print("🚫 Popup removido")
                time.sleep(1)
                break
            except:
                continue
    except:
        pass

def coletar_seguidores_rapido():
    """Coleta otimizada com velocidade máxima segura"""
    print("🚀 Coleta rápida otimizada iniciada!")
    
    seguidores = []
    seguidores_unicos = set()
    scrolls_sem_novos = 0
    
    time.sleep(3)  # Carregamento inicial
    
    for scroll_num in range(MAX_SCROLLS):
        if len(seguidores) >= MAX_SEGUIDORES:
            break
            
        print(f"🔄 Scroll {scroll_num + 1} | Coletados: {len(seguidores)}")
        
        # COLETA SUPER OTIMIZADA - JavaScript direto
        novos_encontrados = 0
        try:
            dados = driver.execute_script("""
                var seguidores = [];
                var dialog = document.querySelector('div[role="dialog"]');
                if (!dialog) return [];
                
                var links = dialog.querySelectorAll('a[href*="/"]');
                for (var i = 0; i < links.length; i++) {
                    var link = links[i];
                    var href = link.href;
                    
                    if (href && href.includes('instagram.com/') && 
                        !href.includes('/p/') && !href.includes('/reel/') && 
                        !href.includes('/tv/') && !href.includes('/stories/')) {
                        
                        var partes = href.split('/');
                        var username = partes[partes.length - 1] || partes[partes.length - 2];
                        
                        if (username && username.length > 0) {
                            seguidores.push({
                                username: username,
                                nome: link.textContent.trim() || username,
                                url: href
                            });
                        }
                    }
                }
                return seguidores;
            """)
            
            # Processa dados coletados
            for dado in dados:
                username = dado['username']
                if (username and username not in seguidores_unicos and 
                    username not in ['p', 'reel', 'tv', 'stories', 'explore', 'accounts', 'direct', 'reels']):
                    
                    seguidores.append({
                        'username': username,
                        'nome_display': dado['nome'],
                        'url': dado['url'],
                        'posicao': len(seguidores) + 1
                    })
                    seguidores_unicos.add(username)
                    novos_encontrados += 1
                    
                    # Log a cada 25 para não poluir
                    if len(seguidores) % 25 == 0:
                        print(f"👥 {len(seguidores)} seguidores coletados...")
                    elif novos_encontrados <= 5:  # Mostra os primeiros de cada scroll
                        print(f"👤 {len(seguidores):03d}. @{username}")
                        
        except Exception as e:
            print(f"⚠️ Erro: {e}")
        
        print(f"📊 +{novos_encontrados} novos")
        
        # Controle de parada otimizado
        if novos_encontrados == 0:
            scrolls_sem_novos += 1
            if scrolls_sem_novos >= 5:  # Para mais cedo
                print("🛑 Fim da coleta")
                break
        else:
            scrolls_sem_novos = 0
        
        # SCROLL RÁPIDO E EFICIENTE
        if scroll_num < MAX_SCROLLS - 1:
            try:
                scroll_result = driver.execute_script("""
                    var dialog = document.querySelector('div[role="dialog"]');
                    if (!dialog) return false;
                    
                    var containers = dialog.querySelectorAll('div');
                    for (var i = 0; i < containers.length; i++) {
                        var container = containers[i];
                        if (container.scrollHeight > container.clientHeight) {
                            container.scrollTop += 1000;  // Scroll otimizado
                            return true;
                        }
                    }
                    return false;
                """)
                
                if not scroll_result:
                    driver.execute_script("window.scrollBy(0, 1000);")
                
                pausa_otima()  # Pausa otimizada
                
            except:
                pass
    
    return seguidores

def salvar_rapido(todos_seguidores, lista_usuarios):
    """Salvamento otimizado para múltiplos perfis"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # JSON compacto
    nome_json = f"seguidores_multiplos_{timestamp}.json"
    with open(nome_json, 'w', encoding='utf-8') as f:
        json.dump({
            'perfis_alvo': lista_usuarios,
            'data_coleta': datetime.now().isoformat(),
            'total_seguidores_unicos': len(todos_seguidores),
            'seguidores': list(todos_seguidores.values())
        }, f, ensure_ascii=False, indent=2)
    
    # TXT apenas usernames
    nome_txt = f"usernames_multiplos_{timestamp}.txt"
    with open(nome_txt, 'w', encoding='utf-8') as f:
        f.write(f"SEGUIDORES DE: {', '.join(['@' + u for u in lista_usuarios])}\n")
        f.write(f"Total únicos: {len(todos_seguidores)}\n")
        f.write("="*40 + "\n\n")
        for seguidor in todos_seguidores.values():
            f.write(f"@{seguidor['username']}\n")
    
    print(f"💾 Salvos: {nome_json} | {nome_txt}")
    print(f"🎯 Total únicos: {len(todos_seguidores)} seguidores")

def executar_coleta_otimizada(username):
    """Execução principal super otimizada"""
    try:
        # Vai direto ao perfil
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(3)
        
        if "Page not found" in driver.page_source:
            print(f"❌ Perfil @{username} não encontrado!")
            return False
        
        print(f"✅ Perfil carregado!")
        remover_popups()
        
        # Encontra e clica em seguidores
        for selector in [f"//a[@href='/{username}/followers/']", f"//a[contains(@href, '/{username}/followers')]"]:
            try:
                button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                driver.execute_script("arguments[0].click();", button)
                break
            except:
                continue
        
        time.sleep(4)
        
        if '/followers/' not in driver.current_url:
            print("❌ Lista não abriu!")
            return False
        
        print("✅ Lista aberta! Iniciando coleta rápida...")
        
        # COLETA RÁPIDA
        seguidores = coletar_seguidores_rapido()
        
        if seguidores:
            print(f"\n🎉 SUCESSO!")
            salvar_rapido(seguidores, username)
            return True
        else:
            print("❌ Nenhum seguidor coletado")
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

# EXECUÇÃO PRINCIPAL OTIMIZADA
try:
    print("🚀 INSTAGRAM SCRAPER OTIMIZADO - MÚLTIPLOS PERFIS")
    print(f"🎯 Alvos: {LISTA_USUARIOS}")
    print("="*40)
    
    driver.get("https://www.instagram.com/")
    fazer_login()
    remover_popups()
    
    # Dicionário para armazenar todos os seguidores únicos
    todos_seguidores = {}  # {username: dados_completos}
    
    for i, username in enumerate(LISTA_USUARIOS, 1):
        print(f"\n🔄 [{i}/{len(LISTA_USUARIOS)}] Processando @{username}")
        print("="*40)
        
        sucesso = executar_coleta_otimizada(username)
        
        if sucesso:
            # Lê o arquivo JSON mais recente para pegar os dados
            arquivos_json = [f for f in os.listdir('.') if f.startswith(f'seguidores_{username}_')]
            if arquivos_json:
                arquivo_mais_recente = max(arquivos_json, key=os.path.getctime)
                with open(arquivo_mais_recente, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                    
                # Adiciona seguidores únicos ao dicionário principal
                novos_adicionados = 0
                for seguidor in dados['seguidores']:
                    if seguidor['username'] not in todos_seguidores:
                        todos_seguidores[seguidor['username']] = seguidor
                        novos_adicionados += 1
                
                print(f"✅ @{username}: {len(dados['seguidores'])} seguidores | +{novos_adicionados} novos únicos")
                
                # Remove arquivo individual
                os.remove(arquivo_mais_recente)
                arquivo_txt = arquivo_mais_recente.replace('seguidores_', 'usernames_').replace('.json', '.txt')
                if os.path.exists(arquivo_txt):
                    os.remove(arquivo_txt)
        else:
            print(f"❌ Falha ao coletar @{username}")
        
        # Pausa entre perfis
        if i < len(LISTA_USUARIOS):
            print("⏳ Aguardando 10s antes do próximo...")
            time.sleep(10)
    
    # Salva resultado final
    if todos_seguidores:
        print(f"\n🎉 COLETA COMPLETA!")
        print(f"📊 Seguidores únicos coletados: {len(todos_seguidores)}")
        salvar_rapido(todos_seguidores, LISTA_USUARIOS)
    else:
        print("\n❌ Nenhum seguidor foi coletado")
    
    input("\n⏸️ Enter para fechar...")

except Exception as e:
    print(f"❌ Erro: {e}")
    input()

finally:
    try:
        driver.quit()
        print("🔒 Fechado!")
    except:
        pass