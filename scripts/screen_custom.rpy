screen capitulos:
    # musica de fundo
    on "show" action Play("sound", "audio/bg/shopping.mp3", loop=True)
    on "hide" action Stop("sound")
    on "repalced" action Stop("sound")
    add "images/cap_bg.png"
    imagemap:
        ground "images/cap_ground.png"
        hover "images/cap_hover.png"

        hotspot(16, 23, 293, 124) action Jump("capitulo_1")
        if(persistent.cap_2):
            hotspot(332, 23, 303, 124) action Jump("capitulo_2")
        if(persistent.cap_3):
            hotspot(641, 23, 293, 124) action Jump("capitulo_3")
        if(persistent.cap_4):
            hotspot(951, 23, 307, 124) action Jump("capitulo_4")
