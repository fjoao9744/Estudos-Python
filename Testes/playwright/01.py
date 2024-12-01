from playwright.sync_api import sync_playwright

# Abre o Playwright
with sync_playwright() as p:
    # Lança um navegador Chromium no modo headless
    browser = p.chromium.launch(headless=True)
    '''
    # Chromium
    browser = p.chromium.launch()

    # Firefox
    browser = p.firefox.launch()

    # WebKit
    browser = p.webkit.launch()

    '''
    page = browser.new_page()

    # Acessa um site
    page.goto("https://docs.python.org/3/tutorial/classes.html#private-variables")

    # Coleta o título da página
    title = page.title()
    print("Título da página:", title)

    # Fecha o navegador
    browser.close()