# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

from utils import Loger


logger = Loger("Spamming bot")

def gracefully_shutdown(function):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = function(*args, **kwargs)
            end_time = time.time()
            logger.debug(f"Method Name: {function.__name__}, Args: {args}, Kwargs: {kwargs}, Execution Time: {end_time - start_time}")
            return result
        except KeyboardInterrupt:
            logger.info('exiting after keyboard.')
            sys.exit()
    return wrapper


class Bot:
    def __init__(self, lang: str = 'en'):
        # WebDriver options
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")
        
        profile = webdriver.Chrome(
            options=options, executable_path="./drivers/chromedriver_v111.exe"
        )
        """Instancia do selenium """
        self.driver = profile
        logger.debug("Iniciando browser")
        self.message = "iwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhdhqww e woiwej llllll"
        self.lang = lang
        self.input_label = "Message #spammar" if lang == "en"  else "Conversar em #spammar"
        self.authorize_button_labe = 'Authorize' if lang == "en"  else "Autorizar"
        self.default_channel = "https://discord.com/channels/911248622421704704/925735083313348618"


    @gracefully_shutdown
    def login(self, username: str, password: str, has2F: bool = False,openPage:bool = True,twoFacCode= int )->None:
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
        try:
            input_element = driver.find_element(By.XPATH, "//input[@name='email']")
        except:
            logger.error('Email input not found')
            return
        self.type_like_a_person(username, input_element, True)

        # <input class="inputDefault-3FGxgL input-2g-os5" name="password" type="password" placeholder="" aria-label="Senha" autocomplete="off" maxlength="999" spellcheck="false" aria-labelledby="uid_19" value="">
        input_element = driver.find_element(By.XPATH, "//input[@name='password']")
        self.type_like_a_person(password, input_element, True)
        time.sleep(2)
        try:
            input_element.send_keys(Keys.RETURN)
        except:
            logger.error("Input not found")
            pass
        if has2F is not False:
            time.sleep(2)
            # <input class="inputDefault-3FGxgL input-2g-os5" name="" type="text" placeholder="Código de verificação de 6 dígitos/código de backup de 8 dígitos" aria-label="Digite o código de recuperação/autorização do Discord" autocomplete="one-time-code" maxlength="10" spellcheck="false" aria-labelledby="uid_21" value="">
            input_element = driver.find_element(
                By.XPATH,
                "//input[@aria-label='Digite o código de recuperação/autorização do Discord']",
            )
            code = 0
            if twoFacCode:
                code = twoFacCode
            else:
                code = input("Please, inform your two factor authentication code: ")
            self.type_like_a_person(code, input_element, True)
        time.sleep(5)

    @gracefully_shutdown
    def addMarket(
        self, start: int = 0, limit: int = 300, value: int = 20, reindex: bool = True
    ):
        logger.info("Iniciando venda de pokemons")
        logger.info(f"ID de inicio {start}")
        logger.info(f"ID final {limit}")
        logger.info(f"Valor de venda {value}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        i = int(start)
        self.type_like_a_person("<@716390085896962058> cleanup", input, True)
        time.sleep(10)
        while i < int(limit):
            logger.debug(f"adding {i} to market")
            time.sleep(10)
            self.type_like_a_person("<@716390085896962058> market add {} {}".format(i, value), input, True)
            time.sleep(6)
            self.confirm()
            i += 1
        logger.debug('Reindexing pokemons')
        self.type_like_a_person("<@716390085896962058> reindex", input, True) if reindex else ""
        time.sleep(5)
        logger.debug('Cleaning messages')
        self.type_like_a_person("<@716390085896962058> cleanup", input, True)
        time.sleep(5)
        self.type_like_a_person("Venda de pokemons concluída", input)

    def removeMarket(self, pokes: list[int], reindex: bool = True):
        logger.info("Removendo pokemons do mercado")
        logger.info(f"Total de pokemons a serem removidos: {len(pokes)}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person("<@716390085896962058> cleanup", input, True)
        time.sleep(10)
        for poke in pokes:
            time.sleep(2)
            self.type_like_a_person("<@716390085896962058> market remove {}".format(poke), input, True)
            time.sleep(6)
            self.confirm()
        self.type_like_a_person("<@716390085896962058> reindex", input, True) if reindex else ""
        time.sleep(5)
        self.type_like_a_person("<@716390085896962058> cleanup", input, True)
        time.sleep(5)
        self.type_like_a_person("Restauração de pokemons concluída", input)

    @gracefully_shutdown
    def spamming(self, level: int):
        logger.info("Iniciando spamming")
        logger.info(
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
            logger.info(f"Mensagem nº {i}.")
            self.type_like_a_person(self.message, input)
            time.sleep(random.randint(1, 5) / 30)
            i += 1

    @gracefully_shutdown
    def get_mega(self, Variation=None):
        def isValid(var: str):
            if var == None:
                return ""
            if var.lower() == "x":
                return "X"
            if var.lower() == "y":
                return "Y"
            return ""

        logger.info("Evoluindo pokemon para Mega")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person(f"{isValid(Variation)} Mega Evolution", input, True)
        time.sleep(random.randint(1, 5) / 30)

    @gracefully_shutdown
    def evolveByCandies(self, amount: int):
        logger.info(f"Iniciando evolução através de rare candies")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        candies = 0
        balance = int(amount)
        while balance > 75:
            self.type_like_a_person("<@716390085896962058> buy rare candies", input, True)
            time.sleep(2)
            balance -= 75
            candies += 1
        logger.info(
            f"Iniciando evolução através de rare candies finalizada, utilizando {candies} candies, com um investimento total de {int(amount) - balance}P¢"
        )

    @gracefully_shutdown
    def buyXpBooster(self, level: int = 1):
        logger.info(f"Iniciando compra de XP Booster {level}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person(
            f"<@716390085896962058> buy Xp Booster {level if int(level) > 1 else ''}", input, True
        )
        time.sleep(2)
        logger.info(f"XP Booster bought.")

    @gracefully_shutdown
    def changePoke(self, pokeId: int):
        logger.info("Changing selected pokemon")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person("<@716390085896962058> s {}".format(pokeId), input, True)

    @gracefully_shutdown
    def confirm(self):
        driver = self.driver
        try:
            confirm = driver.find_element(By.XPATH, "//div[@class='label-31sIdr']")
            confirm.click()
            logger.debug("Confirmed")
            time.sleep(1)
        except:
            logger.error("Não foi possível localizar o confirm. Tentando novamente")
            time.sleep(2)
            try:
                confirm = driver.find_element(By.XPATH, "//div[@class='label-31sIdr']")
                confirm.click()
                time.sleep(1)
            except:
                logger.error("Não foi possível localizar o confirm.")
    
    @gracefully_shutdown
    def solve_for(self, name: str,*args):
        if hasattr(self, name) and callable(func := getattr(self, name)):
            func(*args)
    
    @staticmethod
    def vote(self):
        driver = self.driver
        logger.info('Opening authorizing page')
        driver.get('https://top.gg/login?redir=%2Fbot%2F716390085896962058%2Fvote')
        time.sleep(5)
        logger.info('Authorizing...')
        try:
            authorize_button = driver.find_element(By.XPATH,f"//button/div[text()='{self.authorize_button_labe}']")
        except:
            logger.error("Authorize button not found")
            return driver.get(self.default_channel)
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
