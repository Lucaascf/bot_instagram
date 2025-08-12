from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time

# Configurações
EMAIL = os.getenv("INSTA_EMAIL")
SENHA = os.getenv("INSTA_PASSWORD")

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

def fazer_login(driver):
    """Login otimizado"""
    try:
        time.sleep(2)
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
        time.sleep(5)
        print("✅ Login OK!")
        return True
    except:
        print("✅ Sessão mantida!")
        return True

def teste_enviar_dm_direto(username, driver):
    """Teste: Clica diretamente no botão 'Enviar mensagem' do perfil"""
    try:
        print(f"📩 TESTE: Enviando DM para @{username}...")
        
        # Ir para o perfil do usuário
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(3)
        
        print("🔍 Procurando botão 'Enviar mensagem'...")
        
        # Procurar pelo botão "Enviar mensagem" diretamente no perfil
        selectors_botao_msg = [
            "//button[contains(text(), 'Enviar mensagem')]",
            "//button[contains(text(), 'Message')]",
            "//div[contains(text(), 'Enviar mensagem')]",
            "//div[contains(text(), 'Message')]",
            "//button[contains(@aria-label, 'Enviar mensagem')]",
            "//button[contains(@aria-label, 'Message')]"
        ]
        
        botao_encontrado = False
        for selector in selectors_botao_msg:
            try:
                botao = driver.find_element(By.XPATH, selector)
                if botao.is_displayed():
                    print(f"✅ Botão encontrado: {selector}")
                    driver.execute_script("arguments[0].click();", botao)
                    botao_encontrado = True
                    break
            except:
                continue
        
        if not botao_encontrado:
            print("❌ Botão 'Enviar mensagem' não encontrado")
            return False
        
        time.sleep(4)
        print(f"🌐 URL atual após clicar: {driver.current_url}")
        
        # Procurar campo de mensagem
        print("🔍 Procurando campo de mensagem...")
        campo_mensagem = None
        selectors_campo = [
            "textarea[placeholder*='mensagem']",
            "textarea[placeholder*='message']", 
            "div[contenteditable='true'][role='textbox']",
            "textarea[aria-label*='mensagem']",
            "textarea[aria-label*='message']",
            "div[contenteditable='true']"
        ]
        
        for i, selector in enumerate(selectors_campo):
            try:
                campo_mensagem = driver.find_element(By.CSS_SELECTOR, selector)
                if campo_mensagem.is_displayed() and campo_mensagem.is_enabled():
                    print(f"✅ Campo encontrado com seletor {i+1}: {selector}")
                    break
            except:
                continue
        
        if not campo_mensagem:
            print("❌ Campo de mensagem não encontrado")
            print("🔍 Elementos encontrados na página:")
            # Debug: mostrar elementos textarea e contenteditable
            try:
                textareas = driver.find_elements(By.TAG_NAME, "textarea")
                print(f"   📝 {len(textareas)} textareas encontrados")
                
                editables = driver.find_elements(By.CSS_SELECTOR, "[contenteditable='true']")
                print(f"   ✏️ {len(editables)} elementos contenteditable encontrados")
            except:
                pass
            return False
        
        # Enviar a mensagem
        mensagem = "ola hehe teste"
        print(f"📝 Digitando mensagem: '{mensagem}'")
        
        campo_mensagem.click()
        time.sleep(1)
        campo_mensagem.send_keys(mensagem)
        time.sleep(1)
        campo_mensagem.send_keys(Keys.RETURN)
        
        print("✅ SUCESSO: DM enviado!")
        time.sleep(3)
        return True
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        return False

# EXECUÇÃO DO TESTE
if __name__ == "__main__":
    # Coloque aqui o username que quer testar
    username_teste = "matue30"  # Altere para o username que quiser testar
    
    print("🚀 TESTE DE ENVIO DE DM")
    print(f"🎯 Alvo: @{username_teste}")
    print("="*50)
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    try:
        driver.get("https://www.instagram.com/")
        fazer_login(driver)
        
        # Teste do envio de DM
        resultado = teste_enviar_dm_direto(username_teste, driver)
        
        if resultado:
            print("🎉 TESTE CONCLUÍDO COM SUCESSO!")
        else:
            print("❌ TESTE FALHOU!")
        
        print("\n⏸️ Pressione Enter para fechar o navegador...")
        input()
        
    except Exception as e:
        print(f"❌ Erro geral: {e}")
    finally:
        driver.quit()
        print("🔒 Navegador fechado!")