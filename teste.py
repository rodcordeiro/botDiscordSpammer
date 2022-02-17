import time


def type_like_a_person(sentence, spamming=False):
    """Este código irá basicamente permitir que você simule a digitação como uma pessoa"""
    print("going to start typing message into message share text area")
    for letter in sentence:
        print(letter)
        time.sleep(0.7) if spamming == False else ""


type_like_a_person("Este é o {} sem tempo".format(189), True)
type_like_a_person("Este é o {} com tempo".format(20))
