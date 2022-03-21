# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Spamming bot")


def logging(message):
    logger.info(message)
    # print(message)


class Bot:
    def __init__(self):
        profile = webdriver.Chrome('./drivers/chromedriver_v99.exe')
        """Instancia do selenium """
        self.driver = profile
        logging("Iniciando browser")
        self.message = "iwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhdhqww e woiwej llllll"
        self.input_label = "Message #spammar"

    def login(self):
        driver = self.driver
        driver.get("https://discord.com/channels/911248622421704704/925735083313348618")
        time.sleep(15)
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )

    def addMarket(self, start: int=0, limit:int=300, value:int=20, reindex:bool=True):
        logging("Iniciando venda de pokemons")
        logging(f"ID de inicio {start}")
        logging(f"ID final {limit}")
        logging(f"Valor de venda {value}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        i = start
        self.type_like_a_person("p!cleanup", input, True)
        time.sleep(10)
        while i < limit:
            time.sleep(10)
            self.type_like_a_person("p!market add {} {}".format(i, value), input, True)
            time.sleep(6)
            self.confirm()
            i += 1
        self.type_like_a_person("p!reindex", input, True) if reindex else ""
        time.sleep(5)
        self.type_like_a_person("p!cleanup", input, True)
        time.sleep(5)
        self.type_like_a_person("Venda de pokemons concluída", input)
    
    def removeMarket(self, pokes: list[int],reindex:bool=True):
        logging("Removendo pokemons do mercado")
        logging(f"Total de pokemons a serem removidos: {len(pokes)}")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person("p!cleanup", input, True)
        time.sleep(10)
        for poke in pokes:
            time.sleep(5)
            self.type_like_a_person("p!market remove {}".format(poke), input, True)
            time.sleep(6)
            self.confirm()
        self.type_like_a_person("p!reindex", input, True) if reindex else ""
        time.sleep(5)
        self.type_like_a_person("p!cleanup", input, True)
        time.sleep(5)
        self.type_like_a_person("Restauração de pokemons concluída", input)

    def spamming(self, level:int):
        logging("Iniciando spamming")
        logging(f"Spamming para {level} níveis, utilizando {68 * level} mensagens.")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        i = 0
        total_messages = 68 * level
        while i < total_messages:
            logging(f"Mensagem nº {i}.")
            self.type_like_a_person(self.message, input)
            time.sleep(random.randint(1, 5) / 30)
            i += 1

    def evolveByCandies(self, amount:int):
        logging(f"Iniciando evolução através de rare candies")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        candies = 0
        balance = amount
        while balance > 75:
            self.type_like_a_person("p!buy rare candies", input, True)
            time.sleep(2)
            balance -= 75
            candies += 1
        logging(
            f"Iniciando evolução através de rare candies finalizada, utilizando {candies} candies, com um investimento total de {amount - balance}P¢"
        )
    def buyXpBooster(self, level:int = 1):
        logging(f"Iniciando evolução através de rare candies")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person(f"p!buy Xp Booster {level if level > 1 else ''}", input, True)
        time.sleep(2)
        logging(
            f"XP Booster bought."
        )

    def changePoke(self, pokeId:int):
        logging("Changing selected pokemon")
        driver = self.driver
        input = driver.find_element(
            By.XPATH, "//div[@aria-label='{}']".format(self.input_label)
        )
        input.click()
        self.type_like_a_person("p!s {}".format(pokeId), input, True)

    def confirm(self):
        driver = self.driver
        try:
            confirm = driver.find_element(By.XPATH, "//div[@class='label-31sIdr']")
            confirm.click()
            time.sleep(1)
        except:
            print("Não foi possível localizar o confirm")
    
    @staticmethod
    def type_like_a_person(sentence, single_input_field, Timing=False):
        """Este código irá basicamente permitir que você simule a digitação como uma pessoa"""
        # print("going to start typing message into message share text area")
        text = sentence if Timing else sentence.split()
        for letter in text:
            single_input_field.send_keys(letter)
            time.sleep(0.015) if Timing else ""
        single_input_field.send_keys(Keys.RETURN)

