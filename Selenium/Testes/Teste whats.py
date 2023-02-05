from playwright.sync_api import sync_playwright
import time

texto = "Texto"
telefone = "numero"
link = f'https://web.whatsapp.com/send?phone=55{telefone}&text={texto}'

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # headless
    pagina = navegador.new_page()
    pagina.goto(link)
    pagina.keyboard.down('Enter')
    time.sleep(10)