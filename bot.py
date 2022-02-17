from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


class DiscordBot:
    def __init__(self):
        profile = webdriver.Firefox()
        self.driver = profile
        """Instancia do selenium """
        self.message = "iwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhbe wihweiub ewkrjeqiruiqnwe qe qwrioiqje woijdwuii dhqww e woiwej dfhqqoihn ekj rqeeopjdiwqjeqwdb ewjhdhqww e woiwej llllll"

    def login(self):
        driver = self.driver
        driver.get("https://discord.com/channels/911248622421704704/925735083313348618")
        time.sleep(15)
        print(self.driver)
        self.selling()

    def selling(self):
        driver = self.driver
        input = driver.find_element(By.XPATH, "//div[@aria-label='Message #spammar']")
        input.click()
        i = 29
        self.type_like_a_person("p!cleanup", input)
        while i < 292:
            i += 1
            self.type_like_a_person("p!market add {} 20".format(i), input)
            input.send_keys(Keys.RETURN)
            time.sleep(5)
            try:
                confirm = driver.find_element(By.XPATH, "//div[@class='label-31sIdr']")
                confirm.click()
                time.sleep(1)
            except:
                print("Não foi possível localizar o confirm")
        self.type_like_a_person("p!cleanup", input)
        self.type_like_a_person("Venda de pokemons concluída", input)
        self.evolveByCandies()
        self.spamming()
        self.type_like_a_person("p!s 34", input)
        self.evolveByCandies()
        self.spamming()
        self.type_like_a_person("p!reindex", input)
        self.type_like_a_person("p!cleanup", input)
        driver.get("https://discord.com/channels/911248622421704704/925735083313348618")
        time.sleep(15)
        input = driver.find_element(By.XPATH, "//div[@aria-label='Message #spammar']")
        input.click()
        self.type_like_a_person("Envio finalizado", input)
        self.type_like_a_person("Envio finalizado", input)


    def spamming(self):
        driver = self.driver
        input = driver.find_element(By.XPATH, "//div[@aria-label='Message #spammar']")
        input.click()
        i = 0
        while i < 5000:
            self.type_like_a_person(self.message, input)
            input.send_keys(Keys.RETURN)
            time.sleep(random.randint(1, 5) / 30)
            i += 1

    def evolveByCandies(self):
        driver = self.driver
        input = driver.find_element(By.XPATH, "//div[@aria-label='Message #spammar']")
        input.click()
        balance = 2000
        while balance > 75:
            self.type_like_a_person("p!buy rare candies", input)
            input.send_keys(Keys.RETURN)
            time.sleep(random.randint(1, 5) / 30)
            balance -= 75

    @staticmethod
    def type_like_a_person(sentence, single_input_field, Timing=False):
        """Este código irá basicamente permitir que você simule a digitação como uma pessoa"""
        # print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(0.7) if Timing else ""


bot = DiscordBot()
bot.login()
