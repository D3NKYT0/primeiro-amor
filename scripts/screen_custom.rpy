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
            hotspot(16, 23, 293, 124) action Jump("capitulo_1")
        if(persistent.cap_2):
            hotspot(332, 23, 303, 124) action Jump("capitulo_2")
        if(persistent.cap_3):
            hotspot(641, 23, 293, 124) action Jump("capitulo_3")
        if(persistent.cap_4):
            hotspot(951, 23, 307, 124) action Jump("capitulo_4")

        if(persistent.cap_5):
            hotspot(16, 23, 293, 124) action Jump("capitulo_5")
        if(persistent.cap_6):
            hotspot(332, 23, 303, 124) action Jump("capitulo_6")
        if(persistent.cap_7):
            hotspot(641, 23, 293, 124) action Jump("capitulo_7")
        if(persistent.cap_8):
            hotspot(951, 23, 307, 124) action Jump("capitulo_8")

        if(persistent.cap_9):
            hotspot(16, 23, 293, 124) action Jump("capitulo_9")
        if(persistent.cap_10):
            hotspot(332, 23, 303, 124) action Jump("capitulo_10")
        if(persistent.cap_11):
            hotspot(641, 23, 293, 124) action Jump("capitulo_11")
        if(persistent.cap_12):
            hotspot(951, 23, 307, 124) action Jump("capitulo_12")

        if(persistent.cap_13):
            hotspot(16, 23, 293, 124) action Jump("capitulo_13")
        if(persistent.cap_14):
            hotspot(332, 23, 303, 124) action Jump("capitulo_14")
        if(persistent.cap_15):
            hotspot(641, 23, 293, 124) action Jump("capitulo_15")
        if(persistent.cap_16):
            hotspot(951, 23, 307, 124) action Jump("capitulo_16")
