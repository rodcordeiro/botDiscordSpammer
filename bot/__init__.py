# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from enum import Enum
import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Spamming bot")


def logging(message):
    logger.info(message)
    # print(message)


class Bot:
    def __init__(self, actions_url="./.actions"):
        # WebDriver options
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")

        # Actions
        self.actions_url = actions_url
        self.actions = {}
        self._get_actions()

        profile = webdriver.Chrome(
            options=options, executable_path="./drivers/chromedriver_v101.exe"
        )
        """Instancia do selenium """
        self.driver = profile
        logging("Iniciando browser")
        self.message = "iwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhdhqww e woiwej llllll"
        self.input_label = "Message #spammar"
        self.default_channel = "https://discord.com/channels/911248622421704704/925735083313348618"


    def login(self, username: str, password: str, has2F: bool = False,openPage:bool = True)->None:
        """
        Login Method
        :param username: Discord username
        :type username: :obj:`str`
        :param password: Discord password
        :type password: :obj:`str`
        :param has2F: If discord has two factor authentication
        :type has2F: :obj:`bool`
        :param openPage: Defines it should open the login page
        :type openPage: :obj:`bool`
        """
        driver = self.driver
        self.username = username
        self.password = password
        self.has2F = has2F

        if openPage:
            driver.get(self.default_channel)
        time.sleep(5)
        # <input class="inputDefault-3FGxgL input-2g-os5 inputField-2RZxdl" name="email" type="text" placeholder="" aria-label="E-mail ou número de telefone" autocomplete="off" maxlength="999" spellcheck="false" aria-labelledby="uid_17" value="">
        input_element = driver.find_element(By.XPATH, "//input[@name='email']")
        self.type_like_a_person(username, input_element, True)

        # <input class="inputDefault-3FGxgL input-2g-os5" name="password" type="password" placeholder="" aria-label="Senha" autocomplete="off" maxlength="999" spellcheck="false" aria-labelledby="uid_19" value="">
        input_element = driver.find_element(By.XPATH, "//input[@name='password']")
        self.type_like_a_person(password, input_element, True)
        time.sleep(2)
        try:
            input_element.send_keys(Keys.RETURN)
        except:
            logging("Input not found")
            pass
        if has2F is not False:
            time.sleep(2)
            # <input class="inputDefault-3FGxgL input-2g-os5" name="" type="text" placeholder="Código de verificação de 6 dígitos/código de backup de 8 dígitos" aria-label="Digite o código de recuperação/autorização do Discord" autocomplete="one-time-code" maxlength="10" spellcheck="false" aria-labelledby="uid_21" value="">
            input_element = driver.find_element(
                By.XPATH,
                "//input[@aria-label='Digite o código de recuperação/autorização do Discord']",
            )
            code = input("Please, inform your two factor authentication code: ")
            self.type_like_a_person(code, input_element, True)
        time.sleep(5)

    def addMarket(
        self, start: int = 0, limit: int = 300, value: int = 20, reindex: bool = True
    ):
        logging("Iniciando venda de pokemons")
        logging(f"ID de inicio {start}")
        logging(f"ID final {limit}")
        logging(f"Valor de venda {value}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        i = int(start)
        self.type_like_a_person("@Pokétwo cleanup", input, True)
        time.sleep(10)
        while i < int(limit):
            time.sleep(10)
            self.type_like_a_person("@Pokétwo market add {} {}".format(i, value), input, True)
            time.sleep(6)
            self.confirm()
            i += 1
        self.type_like_a_person("@Pokétwo reindex", input, True) if reindex else ""
        time.sleep(5)
        self.type_like_a_person("@Pokétwo cleanup", input, True)
        time.sleep(5)
        self.type_like_a_person("Venda de pokemons concluída", input)

    def removeMarket(self, pokes: list[int], reindex: bool = True):
        logging("Removendo pokemons do mercado")
        logging(f"Total de pokemons a serem removidos: {len(pokes)}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person("@Pokétwo cleanup", input, True)
        time.sleep(10)
        for poke in pokes:
            time.sleep(2)
            self.type_like_a_person("@Pokétwo market remove {}".format(poke), input, True)
            time.sleep(6)
            self.confirm()
        self.type_like_a_person("@Pokétwo reindex", input, True) if reindex else ""
        time.sleep(5)
        self.type_like_a_person("@Pokétwo cleanup", input, True)
        time.sleep(5)
        self.type_like_a_person("Restauração de pokemons concluída", input)

    def spamming(self, level: int):
        logging("Iniciando spamming")
        logging(
            f"Spamming para {level} níveis, utilizando {68 * int(level)} mensagens."
        )
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        i = 0
        total_messages = 68 * int(level)
        while i < total_messages:
            logging(f"Mensagem nº {i}.")
            self.type_like_a_person(self.message, input)
            time.sleep(random.randint(1, 5) / 30)
            i += 1

    def get_mega(self, Variation=None):
        def isValid(var: str):
            if var == None:
                return ""
            if var.lower() == "x":
                return "X"
            if var.lower() == "y":
                return "Y"
            return ""

        logging("Evoluindo pokemon para Mega")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person(f"{isValid(Variation)} Mega Evolution", input, True)
        time.sleep(random.randint(1, 5) / 30)

    def evolveByCandies(self, amount: int):
        logging(f"Iniciando evolução através de rare candies")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        candies = 0
        balance = int(amount)
        while balance > 75:
            self.type_like_a_person("@Pokétwo buy rare candies", input, True)
            time.sleep(2)
            balance -= 75
            candies += 1
        logging(
            f"Iniciando evolução através de rare candies finalizada, utilizando {candies} candies, com um investimento total de {int(amount) - balance}P¢"
        )

    def buyXpBooster(self, level: int = 1):
        logging(f"Iniciando compra de XP Booster {level}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person(
            f"@Pokétwo buy Xp Booster {level if int(level,base=10) > 1 else ''}", input, True
        )
        time.sleep(2)
        logging(f"XP Booster bought.")

    def changePoke(self, pokeId: int):
        logging("Changing selected pokemon")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person("@Pokétwo s {}".format(pokeId), input, True)

    def confirm(self):
        driver = self.driver
        try:
            confirm = driver.find_element(By.XPATH, "//div[@class='label-31sIdr']")
            confirm.click()
            time.sleep(1)
        except:
            logging("Não foi possível localizar o confirm. Tentando novamente")
            time.sleep(2)
            try:
                confirm = driver.find_element(By.XPATH, "//div[@class='label-31sIdr']")
                confirm.click()
                time.sleep(1)
            except:
                logging("Não foi possível localizar o confirm.")

    def vote(self):
        driver = self.driver
        driver.get('https://top.gg/bot/716390085896962058/vote')
        time.sleep(5)
        try:
            login_button = driver.find_element(
                By.XPATH, "//a[@href='/login?redir=%2Fbot%2F716390085896962058%2Fvote']"
            )
        except:
            print("Login button not found")
            return driver.get(self.default_channel)
        login_button.click()
        time.sleep(5)
        self.login(self.username,self.password,self.has2F,False)
        try:
            authorize_button = driver.find_element(By.XPATH,"//div[@class='footer-3Gu_Tl']/button[text()='Autorizar']")
        except:
            print("Authorize button not found")
            return driver.get(self.default_channel)
        print(authorize_button)
        authorize_button.click()
        time.sleep(25)
        vote_button = driver.find_element(By.XPATH,"//button[text()='Vote']")
        vote_button.click()
        time.sleep(3)
        driver.get(self.default_channel)
        time.sleep(3)
        
        
    @staticmethod
    def type_like_a_person(sentence, single_input_field, Timing=False):
        """Este código irá basicamente permitir que você simule a digitação como uma pessoa"""
        text = sentence if Timing else sentence.split()
        for letter in text:
            single_input_field.send_keys(letter)
            time.sleep(0.015) if Timing else ""
        single_input_field.send_keys(Keys.RETURN)
