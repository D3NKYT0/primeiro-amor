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
