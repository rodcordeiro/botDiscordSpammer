# -*- coding: utf-8 -*-
import sys, getopt
from bot import Bot
from decouple import config
from utils import Loger

logger = Loger('main')

import time


def main(argv):
    opts, args = getopt.getopt(argv,"ht:x:m:r:g:c:p:s:",["two-factor=","xp-boster=","market=","remove-market=","get-mega=","candies=","pokemon-select=","spamming="])
    has2f = False
    twofactorcode = ''
    actions = {}
    for opt, arg in opts:
        if opt == '-h':
            logger.info('Bot spammer for Poketwo! Look below for examples of the commands. For better understanding, read the code! (sorry, theres no doc for this masterpiece ://) ')
            print ('python .  -t 685040 # Two factor authentication code')
            print ('python .  -x 3')
            print ('python .  -m 78,79,15... # Pokemon id')
            print ('python .  -r 78,79,15... # Market id')
            print ('python .  -p 12 # Pokemon id')
            print ('python .  -s 20 # Number of lvls to evolve')
            print('\nIn case of exception, read it before any issues. Maybe its self explanatory')
            sys.exit()
        elif opt in ("-t", "--two-factor"):
            logger.info('enabling two factor authentication')
            twofactorcode = arg
            has2f = True
        elif opt in ("-x", "--xp-boster"):
            logger.info('XP booster enabled')
            actions['buyXpBooster'] = arg
        elif opt in ("-m", "--market"):
            logger.info('Market action enabled')
            actions['addMarket'] = arg.split(',')
        elif opt in ("-r", "--remove-market"):
            logger.info('Removing pokemons from market enabled')
            actions['removeMarket'] = arg.split(',')
        elif opt in ("-g", "--get-mega"):
            logger.info('Mega evolution enabled')
            actions['get_mega'] = arg
        elif opt in ("-c", "--candies"):
            logger.info('Evolution by candies enabled')
            actions['evolveByCandies'] = arg
        elif opt in ("-p", "--pokemon-select"):
            logger.info('Changing pokemon enabled')
            actions['changePoke'] = arg
        elif opt in ("-s", "--spamming"):
            logger.info(f"Spamming for {arg} levels")
            actions['spamming'] = arg

    bot = Bot()
    if has2f:
        bot.login(config("LOGIN"), config("PASSWORD"), has2F=has2f,twoFacCode=twofactorcode)
    else:
        bot.login(config("LOGIN"), config("PASSWORD"), has2F=has2f)
    
    for act in actions:
        bot.solve_for(act,actions[act])

if __name__ == "__main__":
   main(sys.argv[1:])