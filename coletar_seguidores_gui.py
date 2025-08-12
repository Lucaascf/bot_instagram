from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import random
import json
from datetime import datetime

# Configurações
EMAIL = os.getenv("INSTA_EMAIL")
SENHA = os.getenv("INSTA_PASSWORD")
LISTA_USUARIOS = ["_imcryansp._"]
MAX_SEGUIDORES = 20  # Ilimitado
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
options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
options.add_argument("--window-size=1366,768")
options.add_argument("--start-maximized")


def pausa_otima():
    """Pausa otimizada para velocidade máxima segura"""
    time.sleep(random.uniform(1.2, 1.8))


def fazer_login(driver):
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

        login_button = driver.find_element(
            By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(random.uniform(4, 7))
        print("✅ Login OK!")
        return True
    except:
        print("✅ Sessão mantida!")
        return True


def remover_popups(driver):
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


def coletar_seguidores_rapido(driver):
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

    # Pasta Downloads/bot_insta
    downloads_path = os.path.join(
        os.path.expanduser("~"), "Downloads", "bot_insta")
    os.makedirs(downloads_path, exist_ok=True)

    # TXT apenas usernames
    nome_txt = os.path.join(
        downloads_path, f"usernames_multiplos_{timestamp}.txt")
    with open(nome_txt, 'w', encoding='utf-8') as f:
        f.write(
            f"SEGUIDORES DE: {', '.join(['@' + u for u in lista_usuarios])}\n")
        f.write(f"Total únicos: {len(todos_seguidores)}\n")
        f.write("="*40 + "\n\n")
        for seguidor in todos_seguidores.values():
            f.write(f"@{seguidor['username']}\n")

    print(f"🎯 Total únicos: {len(todos_seguidores)} seguidores")
    return nome_txt


def executar_coleta_otimizada(username, driver, wait):
    """Execução principal super otimizada"""
    try:
        # Vai direto ao perfil
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(3)

        if "Page not found" in driver.page_source:
            print(f"❌ Perfil @{username} não encontrado!")
            return False

        print(f"✅ Perfil carregado!")
        remover_popups(driver)

        # Encontra e clica em seguidores
        for selector in [f"//a[@href='/{username}/followers/']", f"//a[contains(@href, '/{username}/followers')]"]:
            try:
                button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, selector)))
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
        seguidores = coletar_seguidores_rapido(driver)

        if seguidores:
            print(f"\n🎉 SUCESSO!")
            print(f"💾 Coletados: {len(seguidores)} seguidores de @{username}")
            return seguidores  # Retorna os seguidores diretamente
        else:
            print("❌ Nenhum seguidor coletado")
            return False

    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

# FUNÇÕES DE COMENTÁRIO


def comentar_no_post(post_url, driver):
    """Comentar super rápido"""
    try:
        print(f"💬 Comentando no post...")

        # Abrir post
        driver.execute_script(f"window.open('{post_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)

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
        time.sleep(0.5)
        buscar_campo().send_keys(comentario)
        time.sleep(0.5)
        buscar_campo().send_keys(Keys.RETURN)

        print("   📤 Comentário enviado!")
        time.sleep(2)

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


def enviar_dm(username, driver):
   """Enviar DM após comentar - versão corrigida"""
   try:
       print(f"📩 Enviando DM para @{username}...")
       
       # Ir para o perfil do usuário
       driver.get(f"https://www.instagram.com/{username}/")
       time.sleep(2)
       
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
                   driver.execute_script("arguments[0].click();", botao)
                   botao_encontrado = True
                   break
           except:
               continue
       
       if not botao_encontrado:
           print("   ❌ Botão 'Enviar mensagem' não encontrado")
           return False
       
       time.sleep(4)
       
       # Procurar campo de mensagem
       campo_mensagem = None
       selectors_campo = [
           "textarea[placeholder*='mensagem']",
           "textarea[placeholder*='message']", 
           "div[contenteditable='true'][role='textbox']",
           "textarea[aria-label*='mensagem']",
           "textarea[aria-label*='message']",
           "div[contenteditable='true']"
       ]
       
       for selector in selectors_campo:
           try:
               campo_mensagem = driver.find_element(By.CSS_SELECTOR, selector)
               if campo_mensagem.is_displayed() and campo_mensagem.is_enabled():
                   break
           except:
               continue
       
       if not campo_mensagem:
           print("   ❌ Campo de mensagem não encontrado")
           return False
       
       # Enviar a mensagem
       mensagem = "ola hehe"
       campo_mensagem.click()
       time.sleep(1)
       campo_mensagem.send_keys(mensagem)
       time.sleep(1)
       campo_mensagem.send_keys(Keys.RETURN)
       
       print("   📤 DM enviado!")
       time.sleep(3)
       return True
       
   except Exception as e:
       print(f"   ❌ Erro ao enviar DM: {str(e)[:50]}...")
       return False


def verificar_perfil(username, driver):
    """Verificar perfil rápido"""
    try:
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(1.5)

        # Verificar se existe
        if any(erro in driver.page_source.lower() for erro in [
            "page not found", "user not found"
        ]):
            print("❌ Perfil não existe")
            return False

        # Verificar se é privado - melhor detecção
        if any(texto in driver.page_source.lower() for texto in [
            "this account is private", "esta conta é privada", "this account is private.",
            "conta privada", "private account", "seguir para ver"
        ]) or "follow to see" in driver.page_source.lower():
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
            
            # Comentar no post
            comentou = comentar_no_post(post_info, driver)
            
            if comentou:
                # Aguardar um pouco antes de enviar DM
                time.sleep(2)
                # Enviar DM
                enviar_dm(username, driver)
            
            return comentou
        else:
            print("📷 Nenhum post encontrado")
            return False

    except Exception as e:
        print(f"❌ Erro: {e}")
        return False


def executar_verificacao_perfis(arquivo_txt, log_callback):
    """Função que executa a verificação de perfis"""
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    try:
        log_callback("🚀 INSTAGRAM AUTO COMMENT")

        # Lê usuários do arquivo
        with open(arquivo_txt, 'r') as f:
            usuarios = [linha.strip().replace('@', '') for linha in f if linha.strip() and not linha.startswith(
                'SEGUIDORES') and not linha.startswith('Total') and not linha.startswith('=')]

        log_callback(f"👤 Total de usuários: {len(usuarios)}")
        log_callback("="*50)

        driver.get("https://www.instagram.com/")

        # Substitui prints por log_callback
        original_print = print

        def custom_print(msg):
            log_callback(str(msg))

        import builtins
        builtins.print = custom_print

        if not fazer_login(driver):
            log_callback("❌ Falha no login")
            return

        for usuario in usuarios:
            log_callback(f"\n🔍 Verificando: @{usuario}")
            verificar_perfil(usuario, driver)
            time.sleep(random.randint(1, 2))

        log_callback("\n✅ Todos os usuários processados!")

        # Restaura print original
        builtins.print = original_print

    except Exception as e:
        log_callback(f"❌ Erro: {e}")
    finally:
        try:
            driver.quit()
            log_callback("🔒 Navegador fechado!")
        except:
            pass


def executar_scraper_com_gui(lista_usuarios, log_callback, gui_instance):
    """Função que será chamada pela GUI"""
    global LISTA_USUARIOS, todos_seguidores

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    wait = WebDriverWait(driver, 15)

    LISTA_USUARIOS = lista_usuarios
    todos_seguidores = {}
    arquivo_final = None

    try:
        log_callback("🚀 INSTAGRAM SCRAPER OTIMIZADO - MÚLTIPLOS PERFIS")
        log_callback(f"🎯 Alvos: {LISTA_USUARIOS}")
        log_callback("="*40)

        driver.get("https://www.instagram.com/")
        fazer_login(driver)
        remover_popups(driver)

        for i, username in enumerate(LISTA_USUARIOS, 1):
            log_callback(
                f"\n🔄 [{i}/{len(LISTA_USUARIOS)}] Processando @{username}")
            log_callback("="*40)

            # Substitui todos os prints por log_callback
            original_print = print

            def custom_print(msg):
                log_callback(str(msg))

            import builtins
            builtins.print = custom_print

            seguidores = executar_coleta_otimizada(username, driver, wait)

            # Restaura print original
            builtins.print = original_print

            if seguidores:
                # Processa seguidores diretamente sem salvar JSON temporário
                novos_adicionados = 0
                for seguidor in seguidores:
                    if seguidor['username'] not in todos_seguidores:
                        todos_seguidores[seguidor['username']] = seguidor
                        novos_adicionados += 1

                log_callback(
                    f"✅ @{username}: {len(seguidores)} seguidores | +{novos_adicionados} novos únicos")
            else:
                log_callback(f"❌ Falha ao coletar @{username}")

            if i < len(LISTA_USUARIOS):
                log_callback("⏳ Aguardando 10s antes do próximo...")
                time.sleep(10)

        if todos_seguidores:
            log_callback(f"\n🎉 COLETA COMPLETA!")
            log_callback(
                f"📊 Seguidores únicos coletados: {len(todos_seguidores)}")

            # Substitui print para salvar_rapido também
            original_print = print

            def custom_print(msg):
                log_callback(str(msg))

            import builtins
            builtins.print = custom_print

            arquivo_final = salvar_rapido(todos_seguidores, LISTA_USUARIOS)

            # Restaura print original
            builtins.print = original_print

            # Ativa botão de verificar perfis na GUI
            gui_instance.ativar_verificacao(arquivo_final)

        else:
            log_callback("\n❌ Nenhum seguidor foi coletado")

    except Exception as e:
        log_callback(f"❌ Erro: {e}")
    finally:
        try:
            driver.quit()
            log_callback("🔒 Fechado!")
        except:
            pass


# EXECUÇÃO COM GUI
if __name__ == "__main__":
    import tkinter as tk
    from tkinter import ttk, scrolledtext
    import threading

    class InstagramScraperGUI:
        def __init__(self, root, start_callback):
            self.root = root
            self.start_callback = start_callback
            self.setup_ui()
            self.pasta_salvamento = os.path.join(
                os.path.expanduser("~"), "Downloads", "bot_insta")
            self.criar_pasta_salvamento()
            self.arquivo_usuarios = None
            self.countdown_active = False

        def criar_pasta_salvamento(self):
            if not os.path.exists(self.pasta_salvamento):
                os.makedirs(self.pasta_salvamento)

        def setup_ui(self):
            self.root.title("Coletor de Seguidores")
            self.root.geometry("500x500")

            main_frame = ttk.Frame(self.root, padding="10")
            main_frame.pack(fill=tk.BOTH, expand=True)

            ttk.Label(
                main_frame, text="Perfis para analisar (separados por vírgula):").pack()
            self.entry_usuarios = ttk.Entry(main_frame, width=50)
            self.entry_usuarios.pack(pady=5)
            self.entry_usuarios.insert(0, "_imcryansp._, matue")

            # Frame para botões
            button_frame = ttk.Frame(main_frame)
            button_frame.pack(pady=5)

            self.btn_iniciar = ttk.Button(
                button_frame,
                text="INICIAR COLETA",
                command=self.iniciar_coleta
            )
            self.btn_iniciar.pack(side=tk.LEFT, padx=5)

            self.btn_verificar = ttk.Button(
                button_frame,
                text="VERIFICAR PERFIS",
                command=self.verificar_perfis
            )
            self.btn_verificar.pack(side=tk.LEFT, padx=5)

            # Botão para selecionar arquivo manualmente
            self.btn_arquivo = ttk.Button(
                button_frame,
                text="ESCOLHER ARQUIVO",
                command=self.escolher_arquivo
            )
            self.btn_arquivo.pack(side=tk.LEFT, padx=5)

            # Label para countdown
            self.lbl_countdown = ttk.Label(
                main_frame, text="", foreground="red")
            self.lbl_countdown.pack()

            ttk.Label(main_frame, text="Logs de execução:").pack()
            self.log_text = scrolledtext.ScrolledText(
                main_frame, height=15, wrap=tk.WORD)
            self.log_text.pack(fill=tk.BOTH, expand=True)

        def log(self, mensagem):
            self.log_text.insert(tk.END, mensagem + "\n")
            self.log_text.see(tk.END)
            self.root.update()

        def iniciar_coleta(self):
            usuarios = [u.strip()
                        for u in self.entry_usuarios.get().split(",") if u.strip()]
            if usuarios:
                self.btn_iniciar.config(state=tk.DISABLED)
                self.btn_verificar.config(state=tk.DISABLED)
                self.btn_arquivo.config(state=tk.DISABLED)
                self.log("="*50)
                self.log(f"Iniciando coleta para: {', '.join(usuarios)}")
                # Executa em thread separada para não travar a GUI
                threading.Thread(target=self.start_callback, args=(
                    usuarios, self.log, self), daemon=True).start()
            else:
                self.log("Erro: Nenhum usuário especificado!")

        def escolher_arquivo(self):
            """Permite escolher arquivo TXT manualmente"""
            from tkinter import filedialog
            downloads_path = os.path.join(
                os.path.expanduser("~"), "Downloads", "bot_insta")
            arquivo = filedialog.askopenfilename(
                title="Escolher arquivo de usuários",
                filetypes=[("Arquivos de texto", "*.txt"),
                           ("Todos os arquivos", "*.*")],
                initialdir=downloads_path if os.path.exists(
                    downloads_path) else "."
            )
            if arquivo:
                self.arquivo_usuarios = arquivo
                self.log(f"📁 Arquivo selecionado: {os.path.basename(arquivo)}")
            else:
                self.log("❌ Nenhum arquivo selecionado")

        def ativar_verificacao(self, arquivo_txt):
            """Ativa o botão de verificar perfis e inicia countdown"""
            self.arquivo_usuarios = arquivo_txt
            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_verificar.config(state=tk.NORMAL)
            self.btn_arquivo.config(state=tk.NORMAL)
            self.log(
                f"\n🎯 Coleta finalizada! Arquivo: {os.path.basename(arquivo_txt)}")
            self.log("📁 Iniciando verificação automática em 5 segundos...")
            self.log(
                "⏰ Clique em 'VERIFICAR PERFIS' para cancelar a verificação automática")
            self.iniciar_countdown()

        def iniciar_countdown(self):
            """Inicia countdown de 5 segundos"""
            self.countdown_active = True
            self.countdown(5)

        def countdown(self, seconds):
            """Countdown regressivo"""
            if self.countdown_active and seconds > 0:
                self.lbl_countdown.config(
                    text=f"Verificação automática em {seconds} segundos...")
                self.root.after(1000, lambda: self.countdown(seconds - 1))
            elif self.countdown_active and seconds == 0:
                self.lbl_countdown.config(text="")
                self.verificar_perfis()

        def verificar_perfis(self):
            """Inicia verificação de perfis"""
            # Se não há arquivo da coleta atual, procura o mais recente na pasta Downloads/bot_insta
            if not self.arquivo_usuarios:
                downloads_path = os.path.join(
                    os.path.expanduser("~"), "Downloads", "bot_insta")
                if os.path.exists(downloads_path):
                    arquivos_txt = [f for f in os.listdir(downloads_path) if f.startswith(
                        'usernames_multiplos_') and f.endswith('.txt')]
                    if arquivos_txt:
                        arquivo_mais_recente = max(
                            arquivos_txt, key=lambda f: os.path.getctime(os.path.join(downloads_path, f)))
                        self.arquivo_usuarios = os.path.join(
                            downloads_path, arquivo_mais_recente)
                        self.log(
                            f"📁 Usando arquivo mais recente: {arquivo_mais_recente}")
                    else:
                        self.log(
                            "❌ Nenhum arquivo de usuários encontrado em Downloads/bot_insta/!")
                        return
                else:
                    self.log("❌ Pasta Downloads/bot_insta/ não encontrada!")
                    return

            if self.arquivo_usuarios and os.path.exists(self.arquivo_usuarios):
                self.countdown_active = False  # Para o countdown
                self.lbl_countdown.config(text="")
                self.btn_verificar.config(state=tk.DISABLED)
                self.log(
                    f"\n🔍 Iniciando verificação de perfis do arquivo: {os.path.basename(self.arquivo_usuarios)}")
                threading.Thread(target=executar_verificacao_perfis, args=(
                    self.arquivo_usuarios, self.log), daemon=True).start()
            else:
                self.log("❌ Arquivo de usuários não encontrado!")
                self.arquivo_usuarios = None

    # Inicia a GUI
    root = tk.Tk()
    app = InstagramScraperGUI(root, executar_scraper_com_gui)
    root.mainloop()