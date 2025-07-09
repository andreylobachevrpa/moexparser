from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        # Открываем хром, установка драйвера
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )

    def open_browser(self):
        """Метод для перехода на moex"""
        # Переходим на сайт
        self.driver.get("https://www.moex.com/ru/derivatives/currency-rate.aspx")

    def acceptance_agreement(self):
        """Метод для подтверждения согласия"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='disclaimer__buttons']//a[normalize-space()='Согласен']",
                )
            )
        )
        element.click()

    def currency_and_date_selection(self, currency_type: str, month_info: dict):
        """Метод для выбора валюты и временных промежутков"""
        # Нажатие на список валют
        currency_selection = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[normalize-space()='Выберите валюты:']/following::div[@class='ui-select__placeholder']",
                )
            )
        )
        currency_selection.click()
        # Выбор нужной пары
        currency = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-select-option__content']//a[contains(normalize-space(), '{currency_type}')]",
                )
            )
        )
        currency.click()
        # Нажатие на календарь
        first_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='app']/form/div[2]//*[@id='keysParams']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            first_date,
        )
        first_date.click()
        # Нажатие на список для выбора года первой даты
        first_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='ui-dropdown ui-calendar -opened']//div[@class='ui-calendar__controls']/div[2]/div/div[@class='ui-select__placeholder']",
                )
            )
        )
        first_year.click()
        # Выбор года для первой даты
        select_first_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-dropdown ui-calendar__dropdown -opened']/div/div/div[normalize-space()='{month_info['year']}']",
                )
            )
        )
        select_first_year.click()
        # Нажатие на список для выбора месяца первой даты
        first_month = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='ui-dropdown ui-calendar -opened']//div[@class='ui-calendar__controls']/div[1]/div/div[@class='ui-select__placeholder']",
                )
            )
        )
        first_month.click()
        # Выбор месяца для первой даты
        select_first_month = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-dropdown ui-calendar__dropdown -opened']/div/div/div[contains(normalize-space(),'{month_info['month_number']}')]",
                )
            )
        )
        select_first_month.click()
        # Выбор числа для первой даты
        select_fist_day = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-dropdown ui-calendar -opened']//div[contains(@class, 'ui-calendar__cell -day')][contains(., '{month_info['first_day']}')]",
                )
            )
        )
        select_fist_day.click()
        # Нажатие на календарь
        second_date = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='app']/form/div[3]//*[@id='keysParams']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            second_date,
        )
        second_date.click()
        # Нажатие на список для выбора года второй даты
        second_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='ui-dropdown ui-calendar -opened']//div[@class='ui-calendar__controls']/div[2]/div/div[@class='ui-select__placeholder']",
                )
            )
        )
        second_year.click()
        # Выбор года для второй даты
        select_second_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-dropdown ui-calendar__dropdown -opened']/div/div/div[normalize-space()='{month_info['year']}']",
                )
            )
        )
        select_second_year.click()
        # Нажатие на список для выбора месяца второй даты
        second_month = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[@class='ui-dropdown ui-calendar -opened']//div[@class='ui-calendar__controls']/div[1]/div/div[@class='ui-select__placeholder']",
                )
            )
        )
        second_month.click()
        # Выбор месяца для второй даты
        select_second_month = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-dropdown ui-calendar__dropdown -opened']/div/div/div[contains(normalize-space(),'{month_info['month_number']}')]",
                )
            )
        )
        select_second_month.click()
        # Выбор числа для второй даты
        select_second_day = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@class='ui-dropdown ui-calendar -opened']//div[contains(@class, 'ui-calendar__cell -day')][contains(., '{month_info['last_day']}')]",
                )
            )
        )
        select_second_day.click()
        show_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[@class='ui-button__label'][normalize-space()='Показать']",
                )
            )
        )
        show_button.click()
    def get_data(self):
        """Метод для считывания таблицы"""
        table = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ui-table__container']//table")
            )
        )
        data = []
        for row in table.find_elements(By.XPATH, ".//tbody/tr"):
            cells = row.find_elements(By.TAG_NAME, "td")
            data.append([cell.text for cell in cells])
        return data