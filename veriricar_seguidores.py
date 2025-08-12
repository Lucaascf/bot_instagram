from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.common.keys import Keys
import random

# Configurações
EMAIL = os.getenv("INSTA_EMAIL")
SENHA = os.getenv("INSTA_PASSWORD")
# USUARIO_TESTE = "gringobaian0"

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

def fazer_login():
    """Login rápido"""
    try:
        time.sleep(2)  # Reduzido de 3 para 2
        if "login" not in driver.current_url.lower():
            print("✅ Já logado!")
            return True
        
        print("🔑 Fazendo login...")
        driver.find_element(By.NAME, "username").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(SENHA)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)  # Reduzido de 5 para 3
        print("✅ Login OK!")
        return True
    except:
        print("✅ Sessão mantida!")
        return True

def comentar_no_post(post_url):
    """Comentar super rápido"""
    try:
        print(f"💬 Comentando no post...")
        
        # Abrir post
        driver.execute_script(f"window.open('{post_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)  # Reduzido de 4 para 2
        
        comentario = "ola hehe"
        seletor = "textarea[placeholder*='comentário']"
        
        # Função para buscar campo fresco
        def buscar_campo():
            elementos = driver.find_elements(By.CSS_SELECTOR, seletor)
            for elemento in elementos:
                try:
                    if elemento.is_displayed() and elemento.is_enabled():
                        return elemento
                except:
                    continue
            return None
        
        # Verificar se campo existe
        campo = buscar_campo()
        if not campo:
            print("   ❌ Campo não encontrado")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            return False
        
        # Comentar super rápido
        buscar_campo().click()
        time.sleep(0.5)  # Reduzido de 1 para 0.5
        buscar_campo().send_keys(comentario)
        time.sleep(0.5)  # Reduzido de 1 para 0.5
        buscar_campo().send_keys(Keys.RETURN)
        
        print("   📤 Comentário enviado!")
        time.sleep(2)  # Reduzido de 3 para 2
        
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return True
        
    except Exception as e:
        print(f"   ❌ Erro: {str(e)[:30]}...")
        try:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except:
            pass
        return False

def verificar_perfil(username):
    """Verificar perfil rápido"""
    
    try:
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(1.5)  # Reduzido de 4 para 2
        
        # Verificar se existe
        if any(erro in driver.page_source.lower() for erro in [
            "page not found", "user not found"
        ]):
            print("❌ Perfil não existe")
            return False
        
        # Verificar se é privado
        if any(texto in driver.page_source for texto in [
            "This account is private", "Esta conta é privada"
        ]):
            print("🔒 Perfil privado")
            return False
        
        print("✅ Perfil público")
        
        # Pegar primeiro post
        post_info = driver.execute_script("""
            var posts = document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]');
            return posts.length > 0 ? posts[0].href : null;
        """)
        
        if post_info:
            print(f"📷 Post encontrado")
            return comentar_no_post(post_info)
        else:
            print("📷 Nenhum post encontrado")
            return False
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

# EXECUÇÃO
try:
    print("🚀 INSTAGRAM AUTO COMMENT")
    
    # Lê usuários do arquivo (ignorando linhas vazias)
    with open('usernames__imcryansp.__20250812_010053.txt', 'r') as f:
        usuarios = [linha.strip().replace('@', '') for linha in f if linha.strip()]
    
    print(f"👤 Total de usuários: {len(usuarios)}")
    print("="*50)
    
    driver.get("https://www.instagram.com/")
    
    if not fazer_login():
        exit(1)
    
    for usuario in usuarios:
        print(f"\n🔍 Verificando: @{usuario}")
        verificar_perfil(usuario)
        time.sleep(random.randint(1 , 2))  # Pausa aleatória entre 2 e 5 segundos
    
    print("\n✅ Todos os usuários processados!")

except Exception as e:
    print(f"❌ Erro: {e}")

finally:
    driver.quit()