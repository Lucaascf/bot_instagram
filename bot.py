from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Configurações
EMAIL = os.getenv("INSTA_EMAIL")
SENHA = os.getenv("INSTA_PASSWORD")
PERFIL_BUSCAR = "lucaascf"

# Pasta para salvar perfil/cookies
PROFILE_PATH = os.path.join(os.getcwd(), "insta_profile")

# Chrome com perfil salvo (cookies/sessão)
options = Options()
options.add_argument(f"--user-data-dir={PROFILE_PATH}")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def fazer_login():
    """Login apenas se necessário"""
    try:
        # Verifica se já está logado procurando por elementos da página principal
        time.sleep(3)
        if "login" not in driver.current_url.lower():
            print("✅ Já estava logado!")
            return True
        
        # Se chegou aqui, precisa fazer login
        print("🔑 Fazendo login...")
        driver.find_element(By.NAME, "username").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(SENHA)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        time.sleep(5)
        print("✅ Login realizado!")
        return True
        
    except:
        # Se não encontrou campos de login, provavelmente já está logado
        print("✅ Sessão mantida!")
        return True

def remover_popups():
    """Remove popups básicos"""
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Agora não') or contains(text(), 'Not Now')]").click()
        print("🚫 Popup removido")
    except:
        pass

def buscar_perfil(usuario):
    """Busca perfil via search"""
    print(f"🔍 Iniciando busca por @{usuario}")
    
    try:
        print("🔍 Tentando atalho de teclado '/' para abrir busca...")
        
        # Método 1: Tecla de atalho "/" para abrir busca
        from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(driver)
        actions.send_keys("/").perform()
        time.sleep(2)
        
        print("🔍 Procurando caixa de busca após atalho...")
        search_box = None
        
        # Tenta encontrar a caixa de busca
        search_box_selectors = [
            "//input[@placeholder='Search' or @placeholder='Buscar']",
            "//input[@aria-label='Search input' or @aria-label='Entrada de pesquisa']",
            "//input[@type='text']",
            "//input[contains(@class, 'search')]",
        ]
        
        for selector in search_box_selectors:
            try:
                search_box = driver.find_element(By.XPATH, selector)
                print("✅ Caixa de busca encontrada com atalho!")
                break
            except:
                continue
        
        # Se o atalho não funcionou, vai direto para URL de busca
        if not search_box:
            print("❌ Atalho não funcionou, indo direto para página de busca...")
            driver.get("https://www.instagram.com/explore/search/")
            time.sleep(3)
            
            # Tenta novamente encontrar a caixa
            for selector in search_box_selectors:
                try:
                    search_box = driver.find_element(By.XPATH, selector)
                    print("✅ Caixa de busca encontrada na página de busca!")
                    break
                except:
                    continue
        
        if not search_box:
            print("❌ Não conseguiu encontrar caixa de busca!")
            return False
            
        # Limpa e digita o usuário
        search_box.clear()
        search_box.send_keys(usuario)
        print(f"✅ Digitou: {usuario}")
        time.sleep(2)
        
        # Pressiona Enter
        search_box.send_keys(Keys.RETURN)
        print("✅ Pressionou Enter")
        time.sleep(4)
        
        print("🔍 Procurando resultado do perfil...")
        
        # Múltiplos seletores para encontrar o perfil
        profile_selectors = [
            f"//a[contains(@href, '/{usuario}/')]",
            f"//div[contains(text(), '{usuario}')]//ancestor::a",
            f"//span[contains(text(), '@{usuario}')]//ancestor::a",
            f"//span[contains(text(), '{usuario}')]//ancestor::a",
        ]
        
        profile_found = False
        for selector in profile_selectors:
            try:
                profile_link = driver.find_element(By.XPATH, selector)
                profile_link.click()
                print(f"✅ Clicou no perfil @{usuario}")
                time.sleep(3)
                profile_found = True
                break
            except:
                continue
        
        if not profile_found:
            print(f"❌ Perfil @{usuario} não encontrado nos resultados!")
            return False
        
        print(f"🎉 SUCESSO! Perfil @{usuario} acessado via busca!")
        return True
        
    except Exception as e:
        print(f"❌ ERRO na busca: {str(e)}")
        print(f"❌ Tipo do erro: {type(e).__name__}")
        return False

# EXECUÇÃO PRINCIPAL
try:
    print("🌐 Abrindo Instagram...")
    driver.get("https://www.instagram.com/")
    
    # Login
    fazer_login()
    
    # Remove popups
    remover_popups()
    
    # Busca perfil
    print("🔍 TENTANDO BUSCA NATIVA PRIMEIRO...")
    busca_sucesso = buscar_perfil(PERFIL_BUSCAR)
    
    if busca_sucesso:
        print("🎉 Sucesso via busca nativa!")
    else:
        print("❌ Busca nativa falhou!")
        print("🔄 Tentando URL direta...")
        driver.get(f"https://www.instagram.com/{PERFIL_BUSCAR}/")
        time.sleep(3)
        print("✅ Perfil acessado via URL!")
    
    print(f"📍 URL: {driver.current_url}")
    print("⏸️ Enter para fechar...")
    input()

except Exception as e:
    print(f"❌ Erro: {e}")
    print("⏸️ Enter para fechar...")
    input()

finally:
    driver.quit()