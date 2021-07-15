label capitulo_1:
    # primeira cena
    scene bg bedroom_day

    # musica de fundo
    play music "audio/bg/sleeping.mp3"
    queue music "audio/bg/sleeping.mp3"

    "{cps=20}{color=#eb4dc7}zzzzZZZ...{/color}{/cps}"
    "{cps=20}{color=#eb4dc7}(eu deveria acordar ne? zzZ){/color}{/cps}"
    "{cps=20}{color=#eb4dc7}(será... zzZ){/color}{/cps}"
    play sound "audio/assobio.mp3"
    "{cps=20}{color=#eb4dc7}(parece que estou ouvindo algo! zzZ){/color}{/cps}"
    play sound "audio/assobio.mp3"
    "{cps=20}{color=#eb4dc7}(... zzzzZ ... só vai embora... zzZ){/color}{/cps}"
    play sound "audio/assobio.mp3"
    "{cps=20}{color=#eb4dc7}(... aaaafff! zzZ!!!){/color}{/cps}"
    "{cps=20}{color=#eb4dc7}(serio que eu vou ter que ir ver quem é?...){/color}{/cps}"
    "{cps=20}{color=#928807}{b}Ahhh! Acorda aiiiiiiii.....{b}{/color}{/cps}"
    play sound "audio/assobio.mp3"
    "{cps=20}{color=#eb4dc7}(droga... é a {b}Nana{/b}){/color}{/cps}"
    "{cps=20}{color=#eb4dc7}Pode subir {b}Nana{/b}!!!!{/color}{/cps}"
    "{cps=20}{color=#eb4dc7}(antes que eu mude de ideia...){/color}{/cps}"
    "{cps=20}{color=#928807}{b}Até que enfim... \nTo entrando!!!{b}{/color}{/cps}"

    play music "audio/bg/moments.mp3"
    queue music "audio/bg/moments.mp3"

    # mostra a nana
    show nana normal at right:
        zoom 0.75
    with dissolve

    nana normal "{cps=20}Oiiiiieeee, Bom diaaaa! Acordaaaaa!!{/cps}"
    nana falante "{cps=20}Você sabe que a gente ja estamos atrasadas ne?!{/cps}"
    nana sorrindo "{cps=20}Vamos, vamos, vamos...{/cps}"
    nana sorrindo "{cps=20}rsrsrsrsrs!{/cps}"

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me normal "{cps=20}zzzZ! Como você consegue acordar com toda essa disposição?!{/cps}"
    me falante "{cps=20}Que horas são?{/cps}"

    nana falante "{cps=20}São exatamente, {b}A HORA DA GENTE IR!{/b}, então levanta!!!{/cps}"

    me sorrindo "{cps=20}ta, ta, ta!! estou indo...{/cps}"
    me normal "{cps=20}Só preciso de um minuto, pra ir no banheiro e tomar um café{/cps}"
    me falante "{cps=20}Você ta energica hoje em?!{/cps}"

    nana normal "{cps=20}hum...{/cps}"
    nana falante "{cps=20}Você realmente não lembra né?!{/cps}"

    me normal "{cps=20}Do que exatamente?{/cps}"

    scene bg kitchen_a

    # mostra a nana
    show nana normal at right:
        zoom 0.75
    with dissolve

    nana normal "{cps=20}Hoje é aniversário do {b}Eidan{/b} e você sabe como eu tenho uma queda por ele!{/cps}"
    nana falante "{cps=20}Além disso, você me prometeu ajudar com algo pra ele hoje!!{/cps}"
    nana sorrindo "{cps=20}ah!! Só de pensar... no {b}Eidan S2{/b} me agradecendo por tudo o que a gente vai fazer hoje!!!{/cps}"

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me sorrindo "{cps=20}Então {b}ESSE{/b} é o motivo de tudo isso não é?! rsrs!{/cps}"
    me falante "{cps=20}Quer algo pra comer?{/cps}"

    nana falante "{cps=20}Não, obg!\nEstou anciosa demais pra comer!{/cps}"

    hide nana normal with fade
    hide miki normal with fade

    "{cps=20}{color=#eb4dc7}-=SOM DE ALGUEM NO BANHEIRO=-{/color}{/cps}"
    "{cps=20}{color=#eb4dc7}(Espero que tudo ocorra bem hoje, pelo bem da {b}Nana{/b}){/color}{/cps}"

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me falante "{cps=20}Tudo pronto, vamos?{/cps}"

    # mostra a nana
    show nana normal at right:
        zoom 0.75
    with dissolve

    nana falante "{cps=20}Sim, sim! Só termina esse seu café da manhã de uma vez!{/cps}"

    me sorrindo "{cps=20}rsrs!{/cps}"
    me falante "{cps=20}finalizado! Vou só da tchau pra minha mãe!{/cps}"

    scene bg bedroom_parents_day

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me sorrindo "{cps=20}Tchau mãe!!?{/cps}"
    me falante "{cps=20}Mãe!? ... \n Ih! Não está...{/cps}"

    scene bg outside

    # mostra a nana
    show nana normal at right:
        zoom 0.75
    with dissolve

    nana falante "{cps=20}Até que enfim!{/cps}"

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me normal "{cps=20}Minha mãe ja saiu, eu nem vi!{/cps}"

    nana falante "{cps=20}Quem manda dormir ate tarde!{/cps}"

    me sorrindo "{cps=20}Olha só quem fala! Só acordou agora por causa {b}DO EIDAN{/b}{/cps}"

    nana sorrindo "{cps=20}ah!! assim eu fico com vergonhaaaa!!!{/cps}"

    me falante "{cps=20}Então o que estamos esperando?! VAMOS!{/cps}"

    nana sorrindo "{cps=20}ISSO!!!{/cps}"

    hide nana normal with fade
    hide miki normal with fade

    "{cps=20}{color=#eb4dc7}-=ANDANDO PARA A ESCOLA=-{/color}{/cps}"

    scene bg way

    "{cps=20}{color=#eb4dc7}-=ANDANDO PARA A ESCOLA=-{/color}{/cps}"

    scene bg street_a

    "{cps=20}{color=#eb4dc7}-=ANDANDO PARA A ESCOLA=-{/color}{/cps}"

    scene bg street_b

    "{cps=20}{color=#eb4dc7}-=ANDANDO PARA A ESCOLA=-{/color}{/cps}"

    scene bg school

    # mostra a nana
    show nana normal at right:
        zoom 0.75
    with dissolve

    nana falante "{cps=20}Finalmente!!{/cps}"

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me falante "{cps=20}Vamos logo que já estamos praticamente atrasadas!{/cps}"

    nana falante "{cps=20}Sim sim!!{/cps}"

    # musica de fundo
    play music "audio/bg/school-1.mp3"
    queue music "audio/bg/school-2.mp3"

    scene bg school_entrance

    # mostra a nana
    show nana normal at right:
        zoom 0.75
    with dissolve

    nana falante "{cps=20}Vamos!!{/cps}"

    # mostra a miki
    show miki normal at left:
        zoom 0.48
    with dissolve

    me falante "{cps=20}rsrs!{/cps}"

    # fim do capitulo
    # $persistent.cap_2 = True
    return
