from playwright.sync_api import sync_playwright

# Abre o Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://shop.samsung.com/br/monitor-curvo-full-hd-samsung-led-27/p")
    page.wait_for_selector(".samsungmaster-global-pdp-shop-4-x-sellingPrice")

    # Coleta todas as citações
    quotes = page.query_selector_all(".samsungmaster-global-pdp-shop-4-x-sellingPrice")
    for quote in quotes:
        print(quote.inner_text())

    browser.close()