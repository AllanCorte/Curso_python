from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from pathlib import Path

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / \
    'chromedriver.exe'  # Corrigido o nome do executável


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Exemplo de opções: '--headless', '--disable-gpu'
    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com')

    # Espera até encontrar o input de busca
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    search_input.send_keys('Hello World!')

    # Dorme por 10 segundos para visualizar o resultado
    sleep(TIME_TO_WAIT)
