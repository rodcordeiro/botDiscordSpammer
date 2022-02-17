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
            print(i)
            input.send_keys("p")
            input.send_keys("!")
            input.send_keys("m")
            input.send_keys("a")
            input.send_keys("r")
            input.send_keys("k")
            input.send_keys("e")
            input.send_keys("t")
            input.send_keys(" ")
            input.send_keys("a")
            input.send_keys("d")
            input.send_keys("d")
            input.send_keys(" ")
            for j in str(i).split():
                input.send_keys(j)
                time.sleep(1)
            input.send_keys(" ")
            input.send_keys("2")
            input.send_keys("0")
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
        self.type_like_a_person("p!s 34", input)
        self.spamming()
        self.type_like_a_person("p!s 227", input)
        self.spamming()

    def spamming(self):
        driver = self.driver
        input = driver.find_element(By.XPATH, "//div[@aria-label='Message #spammar']")
        input.click()
        i = 0
        while i < 3000:
            self.type_like_a_person(self.message, input, True)
            input.send_keys(Keys.RETURN)
            time.sleep(random.randint(1, 5) / 30)

    @staticmethod
    def type_like_a_person(sentence, single_input_field, spamming=False):
        """Este código irá basicamente permitir que você simule a digitação como uma pessoa"""
        print("going to start typing message into message share text area")
        for letter in sentence.split():
            single_input_field.send_keys(letter)
            time.sleep(0.7) if spamming == False else ""


bot = DiscordBot()
bot.login()
