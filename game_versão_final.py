from tkinter import *

# Declaração das variáveis globais
texto2 = None
texto3 = None
botao_sim2 = None
botao_nao2 = None

liberdade = 0
vida = 3
vida_inimigo = 4



def inicio():
    nome = Nome.get()
    Nome.destroy()
    botao.destroy()
    global botao_sim
    global botao_nao
    botao_atacar = None

    texto.config(text=f"Parabéns {nome}, você foi escolhido para os mais novos testes de sonhos conscientes da DreamScape.\nEu serei seu assistente robô. Lembre-se, os sonhos podem ser perigosos. Você está pronto para sonhar?")

    botao_sim = Button(janela, command=lambda: sonhar(nome), text="Sim")
    botao_sim.grid(row=3, column=0, pady=10, padx=10)

    botao_nao = Button(janela, command=lambda: morte1(nome), text="Socorro, por favor não!")
    botao_nao.grid(row=3, column=1, pady=10, padx=10)

def morte1(nome):
    botao_sim.destroy()
    botao_nao.destroy()
    texto.config(text=f'Sem problemas usuário {nome}. A pena por não participar é a MORTE')

    over = Label(janela, text="GAME OVER")
    over.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

def sonhar(nome):
    global texto2
    global texto3
    global botao_sim2
    global botao_nao2

    texto.config(text='NADA ALÉM DO ESPERADO... Ficamos felizes por sua escolha. Deite-se na cama da DreamScape e deixe que seus sonhos ganhem vida,\n não se preocupe estarei de olho em você.')

    texto2 = Label(janela, text="Um longo tempo se passou")
    texto2.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    texto3 = Label(janela, text=f"olá *prisioneiro {nome}*, digo, olá usuário {nome}. este é seu mundo do sonhos, pelo jeito esse mundo é muito colorido,\n a luz que reflete nas àguas machucam meus olhos robóticos. Ah olhe um ser vindo do seu subconsciente,\nvamos falar com ele? Se quiser falar com ele, diga 'Sim'. Se não, você pode dizer 'Não' e montar naquele\n unicórnio voador e atirar arco-íris nos moradores desse mundo estranho.")

    texto3.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

    botao_sim2 = Button(janela, command=lambda: luta05(nome, texto3, botao_nao2, botao_sim2), text='Sim')
    botao_sim2.grid(row=4, column=0, pady=10, padx=10, columnspan=2)

    botao_nao2 = Button(janela, command=lambda: luta0(nome, texto3, botao_nao2, botao_sim2), text='Não')
    botao_nao2.grid(row=4, column=1, pady=10, padx=10, columnspan=2)

def luta0(nome, texto3, botao_nao2, botao_sim2):
    texto3.destroy()
    botao_nao2.destroy()
    botao_sim2.destroy()
    botao_nao.destroy()
    botao_sim.destroy()

    texto.config(text="Enquanto atira arco-íris pode ver um castelo. percebendo seu interesse seu unicórnio de\n forma repentina fala que nele há 44 portas, porém, apenas a porta número 63 é a correta")

    texto2.config(text=f"Foi realmente divertido! Parece que o ser do seu subconsciente não gostou muito disso. ele está vindo atacar.")

    botao_luta = Button(janela, command=lambda: luta1(nome, botao_luta), text="lutar")
    botao_luta.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

def luta05(nome, texto3, botao_nao2, botao_sim2):
    texto3.destroy()
    botao_nao2.destroy()
    botao_sim2.destroy()
    botao_nao.destroy()
    botao_sim.destroy()
    texto2.destroy()
    botao_sim.destroy()
    botao_nao.destroy()

    texto.config(text="Enquanto se aproxima o ser faz uma pose de luta.")

    botao_luta = Button(janela, command=lambda: luta1(nome, botao_luta), text="lutar")
    botao_luta.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

def luta1(nome, botao_luta=None):
    
    
    if botao_luta is None:
       
        botao_luta = Button(janela, command=lambda: luta1(nome, botao_luta), text="lutar")
        botao_luta.grid(row=3, column=0, pady=10, padx=10, columnspan=2)
    else:
        
        botao_luta.config(command=lambda: batalha_ataque(nome, botao_defender))
    botao_luta.destroy()
    texto2.destroy()

    texto.config(text="Você vai *atacar* ou *defender*? ")

    botao_defender = Button(janela, command=lambda: batalha_defesa(nome, botao_atacar, botao_defender), text="defender")
    botao_defender.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    botao_atacar = Button(janela, command=lambda: batalha_ataque(nome, botao_defender, botao_atacar), text="atacar")
    botao_atacar.grid(row=2, column=2, pady=10, padx=10, columnspan=2)

def batalha_ataque(nome, botao_defender, botao_atacar):
    botao_defender.destroy()
    global vida
    global vida_inimigo
    
    vida -= 1
    vida_inimigo -= 1
    
    if vida and vida_inimigo < 0:
        botao_defender.destroy()
        botao_atacar.destroy()
        texto.config(text="Vocês lutaram até a morte... \n GAME OVER")

    elif vida == 0:
        botao_defender.destroy()
        botao_atacar.destroy()

        texto.config(text="Sua vida chegou ao fim")
        over = Label(janela, text="GAME OVER")
        over.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    elif vida_inimigo == 0:
        botao_defender.destroy()
        botao_atacar.destroy()
        texto.destroy()

        portas = Button(janela, command=lambda: fasefinal(nome, portas, texto), text='ir para o castelo')
        portas.grid(row=3, column=2, pady=10, padx=10, columnspan=2) 


    elif vida and vida_inimigo > 0:
        botao_defender.destroy()
        botao_atacar.destroy()

        texto_batalha = Label(janela, text=f"Ambos levam 1 de dano. Ps: você tem {vida} de vida")
        texto_batalha.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        continuar = Button(janela, command=lambda: luta2(nome, continuar), text='continuar')
        continuar.grid(row=2, column=2, pady=10, padx=10, columnspan=2)

def batalha_defesa(nome, botao_atacar, botao_defender):
    global vida
    botao_atacar.destroy()
    botao_defender.destroy()
    
    vida += 1
    X = 1
    
    texto_batalha = Label(janela, text=f"Você defende e recupera {X} de vida. Agora você tem {vida} de vida")
    texto_batalha.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
    
    continuar = Button(janela, command=lambda: luta2(nome, continuar), text='continuar')
    continuar.grid(row=3, column=2, pady=10, padx=10, columnspan=2)

def luta2(nome,continuar):
    continuar.destroy()

    texto.config(text="Você vai *atacar* ou *defender*? ")

    botao_defender = Button(janela, command=lambda: batalha_defesa(nome, botao_atacar, botao_defender), text="defender")
    botao_defender.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

    botao_atacar = Button(janela, command=lambda: batalha_ataque(nome, botao_atacar, botao_defender), text="atacar")
    botao_atacar.grid(row=2, column=2, pady=10, padx=10, columnspan=2)


def fasefinal(nome, texto, portas):
    portas.destroy()
    texto.destroy()

    texto2 = Label(janela, text='Ele... evaporou em uma nuvem??? Considero uma vitória!Ah olhe! ele largou um bilhete falando a porta certa é a soma dos multiplos de 3 até 20. \n vamos em direção aquele castelo, meus sistemas dizem que há 100 portas aqui. Qual deve ser a certa?\n escolha uma porta')
    texto2.grid(row=2, column=2, pady=10, padx=10, columnspan=2)

    texto_portas = Label(janela, text="Escolha uma porta")
    texto_portas.grid(row=3, column=2, pady=10, padx=10, columnspan=2)

    porta33 = Button(janela, command=lambda: morte2(porta27, porta33, porta63, porta71, texto_portas, texto2), text='porta 33')
    porta33.grid(row=4, column=4, pady=10, padx=10, columnspan=2)

    porta27 = Button(janela,command=lambda: morte2(porta27, porta33, porta63, porta71, texto_portas, texto2), text='porta 27')
    porta27.grid(row=4, column=2, pady=10, padx=10, columnspan=2)

    porta71 = Button(janela, command=lambda: morte2(porta27, porta33, porta63, porta71, texto_portas, texto2), text='porta 71')
    porta71.grid(row=5, column=2, pady=10, padx=10, columnspan=2)

    porta63 = Button(janela, command=lambda: final(nome, porta27, porta33, porta63, porta71, texto_portas, texto2), text='porta 63')
    porta63.grid(row=5, column=4, pady=10, padx=10, columnspan=2)

def morte2(porta27, porta33, porta63, porta71, texto_portas, texto2):
    texto2.destroy()
    porta27.destroy()
    porta33.destroy()
    porta63.destroy()
    porta71.destroy()

    texto_portas.config(text='uma armadilha arranca parte da sua forma física, consequentemente tirando parte de sua conciência. Você morre \n GAME OVER')


def final(nome, porta27, porta33, porta63, porta71, texto_portas, texto2):
    porta27.destroy()
    porta33.destroy()
    porta63.destroy()
    porta71.destroy()
    texto_portas.destroy()
    texto2.destroy()


    texto2 = Label(janela,text=f"Esse parece o caminho para sair e nunca mais voltar \n obrigado por sonhas usuário {nome} você agora está livre e pode ir embora.")
    texto2.grid(row=2, column=2, pady=10, padx=10, columnspan=2)

    texto3 = Label(text="Obrigao por sonhar! \n Fim")
    texto3.grid(row=3, column=2, pady=10, padx=10, columnspan=2)

janela = Tk()
janela.title("jogo")
janela.geometry("400x300")
janela.resizable(width=True, height=True)
janela.config(bg="#410ddb")

texto = Label(janela, text="Qual é o seu número de identificação? ")
Nome = Entry(janela)
botao = Button(janela, command=inicio, text='Enviar')

texto.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
Nome.grid(row=1, column=0, pady=10, padx=10, columnspan=2)
botao.grid(row=2, column=0, pady=10, padx=10, columnspan=2)

janela.mainloop()