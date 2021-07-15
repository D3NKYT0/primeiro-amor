screen capitulos:
    # musica de fundo
    on "show" action Play("sound", "audio/bg/shopping.mp3", loop=True)
    on "hide" action Stop("sound")
    on "repalced" action Stop("sound")
    add "images/cap_bg.png"
    imagemap:
        ground "images/cap_ground.png"
        hover "images/cap_hover.png"

        if(persistent.cap_1):
            hotspot(15, 15, 289, 153) action Jump("capitulo_1")
        if(persistent.cap_2):
            hotspot(329, 12, 299, 155) action Jump("capitulo_2")
        if(persistent.cap_3):
            hotspot(645, 9, 307, 160) action Jump("capitulo_3")
        if(persistent.cap_4):
            hotspot(968, 12, 303, 159) action Jump("capitulo_4")

        if(persistent.cap_5):
            hotspot(10, 183, 301, 170) action Jump("capitulo_5")
        if(persistent.cap_6):
            hotspot(324, 186, 306, 165) action Jump("capitulo_6")
        if(persistent.cap_7):
            hotspot(645, 186, 308, 169) action Jump("capitulo_7")
        if(persistent.cap_8):
            hotspot(962, 182, 308, 172) action Jump("capitulo_8")

        if(persistent.cap_9):
            hotspot(5, 364, 307, 169) action Jump("capitulo_9")
        if(persistent.cap_10):
            hotspot(326, 363, 306, 172) action Jump("capitulo_10")
        if(persistent.cap_11):
            hotspot(643, 364, 313, 172) action Jump("capitulo_11")
        if(persistent.cap_12):
            hotspot(965, 365, 307, 170) action Jump("capitulo_12")

        if(persistent.cap_13):
            hotspot(8, 542, 304, 170) action Jump("capitulo_13")
        if(persistent.cap_14):
            hotspot(323, 544, 309, 167) action Jump("capitulo_14")
        if(persistent.cap_15):
            hotspot(645, 543, 310, 170) action Jump("capitulo_15")
        if(persistent.cap_16):
            hotspot(963, 542, 307, 171) action Jump("capitulo_16")
