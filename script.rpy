init python:
    class Me:
        def __init__(self, nome, snome):
            self.n = nome
            self.sn = snome

    if(persistent.cap_1 == None):
        persistent.cap_1 = True
    if(persistent.cap_2 == None):
        persistent.cap_2 = False
    if(persistent.cap_3 == None):
        persistent.cap_3 = False
    if(persistent.cap_4 == None):
        persistent.cap_4 = False

    if(persistent.cap_5 == None):
        persistent.cap_5 = False
    if(persistent.cap_6 == None):
        persistent.cap_6 = False
    if(persistent.cap_7 == None):
        persistent.cap_7 = False
    if(persistent.cap_8 == None):
        persistent.cap_8 = False

    if(persistent.cap_9 == None):
        persistent.cap_9 = False
    if(persistent.cap_10 == None):
        persistent.cap_10 = False
    if(persistent.cap_11 == None):
        persistent.cap_11 = False
    if(persistent.cap_12 == None):
        persistent.cap_12 = False

    if(persistent.cap_13 == None):
        persistent.cap_13 = False
    if(persistent.cap_14 == None):
        persistent.cap_14 = False
    if(persistent.cap_15 == None):
        persistent.cap_15 = False
    if(persistent.cap_16 == None):
        persistent.cap_16 = False


init:
    # nome e sobrenome (escolhidos pelo player)
    $name = "Me"
    $sname = "Yoshida"

    # nome e sobrenomes (defaults)
    $Aiko = "Kobayashi "
    $Ayame = "Watanabe"
    $Eidan = "Yamamoto"
    $Hana = "Yamazaki"
    $Hoshi = "Tanaka"
    $Mayonaise = "Kobayashi"
    $Miho = "Takahashi"
    # $Miki = "Yoshida" (protagonista)
    $Nana = "Nakamura"
    $Sakura = "Murakami"
    $Sora = "Miyazaki"
    $Zilch = "Hashimoto"


label start:
    call screen capitulos
    return
