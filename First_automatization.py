import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select



user_name = "Kokos"
invalid_email = "ggrgegge.pl"
password = "123425"
password2 = "123"
class PepperRegistration (unittest. TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://-----.pl")  // Skasowałem stronę, przez etyke
        self.driver.implicitly_wait(400)
        self.driver.maximize_window()


    # OCZEKIWANY REZULTAT
    # 1. 5 błędów, puste pola "Nazwa użytkownika, email, hasło, checklisty"
    def test_empty_field(self):
        driver=self.driver
        #1. Lokalizacja i akceptacja pola cookie
        coockie_btn = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div/div/div/div[2]/div[2]/button[1]/span")
        coockie_btn.click()
        sleep(5)
        #2. Lokalizacja pola "Zarejestruj/zaloguj" i kliknięcie
        register_btn = driver.find_element(By.XPATH, "/html/body/main/div[1]/header/div/div/div[3]/button[2]")
        register_btn.click()
        sleep(5)
        #3. Lokalizacja pola "Utwórz nowe konto"
        create_an_account = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[3]/div[1]/a")
        create_an_account.click()
        sleep(5)
        #4. Potwierdzenie utworzenia nowego konta, bez wpisania danych
        create_an_account_submit = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[3]/div[2]/ul/li/div/button")
        create_an_account_submit.click()
        sleep(50)

        #Otrzymany rezultat
        # 1. 5 błędów, puste pola "Nazwa użytkownika, email, hasło, checklisty"

        error_notice = driver.find_element(By.CSS_SELECTOR, "#registerModalForm")
        print(error_notice.text)
        def tearDown(self):
            self.driver.quit()

        if __name__ == "__main__":
            unittest.main()

    # OCZEKIWANY REZULTAT
    #1. Niepoprawny adres email = brak rejestracji
    def test_invalid_email(self):
        driver = self.driver
        #1 Akceptacja coockie
        coockie_btn = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div/div/div/div[2]/div[2]/button[1]/span")
        coockie_btn.click()
        sleep(5)
        #2. Proces tworzenia konta, odnalezienie pola "Zarejestruj/zaloguj"
        register_btn = driver.find_element(By.XPATH, "/html/body/main/div[1]/header/div/div/div[3]/button[2]")
        register_btn.click()
        sleep(5)
        #3. Lokalizacja przycisku "Utwórz konto"
        create_an_account = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[3]/div[1]/a")
        create_an_account.click()
        sleep(5)
        #4. Uzupełnienie danych do rejestracji
        email_input = driver.find_element(By.ID, "registerModalForm-email")
        email_input.send_keys(invalid_email)

        user_name_input = driver.find_element(By.ID, "registerModalForm-username")
        user_name_input.send_keys(user_name)

        password_input = driver.find_element(By.ID, "registerModalForm-password")
        password_input.send_keys(password)

        checkbox= driver.find_element(By.XPATH, " //*[@id = 'registerModalForm'] / ul / li[4] / div / label / span[1] / span").click()
        checkbox2 = driver.find_element(By.XPATH," //*[@id = 'registerModalForm'] / ul / li[4] / div / label / span[1] / span").click()


        confirm = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[3]/div[2]/ul/li/div/button")
        confirm.click()
        sleep(30)
        error_notice = driver.find_element(By.CSS_SELECTOR, "#registerModalForm-email")
        print(error_notice.text)

        #OTRZYMANY REZULTAT
        #1. Niepoprawny adres email - brak rejestracji
        def tearDown(self):
            self.driver.quit()

        if __name__ == "__main__":
            unittest.main()

    # OCZEKIWANY REZULTAT
    # 1. Niepoprawne hasło= brak rejestracji
    def test_invalid_password(self):
        driver = self.driver
        # 1 Akceptacja coockie
        coockie_btn = driver.find_element(By.XPATH,"/html/body/main/div[3]/div[1]/div/div/div/div[2]/div[2]/button[1]/span")
        coockie_btn.click()
        sleep(20)
        # 2. Proces tworzenia konta, odnalezienie pola "Zarejestruj/zaloguj"
        register_btn = driver.find_element(By.XPATH, "/html/body/main/div[1]/header/div/div/div[3]/button[2]")
        register_btn.click()
        sleep(20)
        # 3. Lokalizacja przycisku "Utwórz konto"
        create_an_account = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[3]/div[1]/a")
        create_an_account.click()
        sleep(20)
        # 4. Uzupełnienie danych do rejestracji
        email_input = driver.find_element(By.ID, "registerModalForm-email")
        email_input.send_keys(invalid_email)

        user_name_input = driver.find_element(By.ID, "registerModalForm-username")
        user_name_input.send_keys(user_name)

        password_input = driver.find_element(By.ID, "registerModalForm-password")
        password_input.send_keys(password2)

        checkbox = driver.find_element(By.XPATH," //*[@id = 'registerModalForm'] / ul / li[4] / div / label / span[1] / span").click()
        checkbox2 = driver.find_element(By.XPATH," //*[@id = 'registerModalForm'] / ul / li[4] / div / label / span[1] / span").click()

        confirm = driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[3]/div[2]/ul/li/div/button")
        confirm.click()
        sleep(30)
        error_notice = driver.find_element(By.CSS_SELECTOR, "#li.formList-row:nth-child(3) > div:nth-child(2)")
        print(error_notice.text)

        # OTRZYMANY REZULTAT
        # 1. Niepoprawny adres email - brak rejestracji
        def tearDown(self):
            self.driver.quit()

        if __name__ == "__main__":
            unittest.main()

