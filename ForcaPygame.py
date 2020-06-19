
import pygame
import random
import time


try:
    pygame.init()
    pygame.font.init()
except:
    print('Pygame não pode ser inicializado corretamente')

largura = 1280
altura = 700
branco = (202, 81, 0)
marrom = (32, 13, 0)
tamanho_a = 90
tamanho_b = 1280
pos_x = 0
pos_y = 610


fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Forca')
font = pygame.font.Font('FFF_Tusj.ttf', 35)
font2 = pygame.font.Font('FFF_Tusj.ttf', 45)
texto = font.render("Forca", True, (0, 0, 0))
dica = font.render("DICA: ", True, (255, 255, 255))
enforcado = font.render("Enforcado", True, (0, 0, 0))
iforca = pygame.image.load('forca.png')
tracos = pygame.font.Font('FFF_Tusj.ttf', 35)


x = str
teste = []
dicas = []
dicas2 = []
dicas3 = []
letra = ''
a = ' '
aa = font.render(str(a), True, (0, 0, 0))
myline = ''
t = []
erro = 0
sorteio = []


def palavra_secreta():
    global aa, tracos, sorteio, dicas, aa, direita, letra, t, dicas2, dicas3, myline, teste

    lines = open('palavras.txt').read().split()
    myline = random.choice(lines)
    for linha in lines:
        if linha == myline:
            teste = linha
            print(teste)

            with open('dicas.txt') as f:
                for i in f:  # percorrer linhas e enumera-las a partir de 1
                    if teste in i:  # ver se palavra esta na linha
                        dicas = i
                        dicas2 = dicas.split('=')
                        dicas3 = dicas2[1]
                        print(dicas3)

    t = []
    for letra in myline:
        t.append('_')

    aa = font.render(str(t), True, (0, 0, 0))
    tracos = font.render(str(a), True, (0, 0, 0))
    sorteio = font.render(myline, True, (0, 0, 0,))
    dicas = font.render(str(dicas3), True, (255, 255, 255))


direita = 500
sair = True
pygame.mixer.music.load('suspense.mp3')
pygame.mixer.music.play()
palavra_secreta()
termina_jogo = False

while sair:
    while termina_jogo:
        fundo.fill(branco)
        continuar = font.render("Para continuar aperte S para sair aperte N",
                                True, (0, 0, 0))
        fundo.blit(continuar, (200, 600))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
                termina_jogo = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    termina_jogo = False
                    iforca = pygame.image.load('forca.png')
                    x = str
                    teste = []
                    dicas = []
                    dicas2 = []
                    dicas3 = []
                    letra = ''
                    a = ' '
                    aa = font.render(str(a), True, (0, 0, 0))
                    myline = ''
                    t = []
                    erro = 0
                    sorteio = []
                    pygame.mixer.music.load('suspense.mp3')
                    pygame.mixer.music.play()
                    palavra_secreta()
                if event.key == pygame.K_n:
                    sair = False
                    termina_jogo = False
    fundo.fill(branco)
    cont = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            a = event.key
            a = chr(a)
            print(a.upper())

            for n, letra in enumerate(myline):

                if myline[n] == a.upper():

                    t[n] = myline[n]

                    aa = font.render(str(t), True, (0, 0, 0))

                    if '_' not in t:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('APLAUSOS.mp3')
                        pygame.mixer.music.play()
                        iforca = pygame.image.load('forca.png')
                        fundo.blit(iforca, (0, 0))
                        pygame.draw.rect(fundo, marrom, [pos_x, pos_y, tamanho_b, tamanho_a])
                        bb = font2.render(str('Voce Ganhou!!!'), True, (255, 255, 255))
                        fundo.blit(bb, (550, 620))
                        pygame.display.update()
                        time.sleep(2)
                        termina_jogo = True

            if a.upper() not in myline:
                print('Não possui')
                erro = erro + 1
                if erro == 1:
                    iforca = pygame.image.load('forca1.png')
                if erro == 2:
                    iforca = pygame.image.load('forca2.png')
                if erro == 3:
                    iforca = pygame.image.load('forca3.png')
                if erro == 4:
                    iforca = pygame.image.load('forca4.png')
                if erro == 5:
                    iforca = pygame.image.load('forca5.png')
                if erro == 6:
                    iforca = pygame.image.load('forca6.png')
                    fundo.blit(iforca, (0, 0))
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Slide_Whistle_to_Drum.mp3')
                    pygame.mixer.music.play()
                    pygame.draw.rect(fundo, marrom, [pos_x, pos_y, tamanho_b, tamanho_a])
                    cc = font2.render(str('Ahhh, que pena!! Você perdeu!'), True, (255, 255, 255))
                    fundo.blit(cc, (300, 620))
                    pygame.display.update()
                    time.sleep(2)
                    termina_jogo = True

    fundo.blit(iforca, (0, 0))
    fundo.blit(aa, (500, 550))
    fundo.blit(texto, (120, 20))
    fundo.blit(tracos, (500, 550))
    pygame.draw.rect(fundo, marrom, [pos_x, pos_y, tamanho_b, tamanho_a])
    fundo.blit(dica, (30, 630))
    fundo.blit(dicas, (150, 630))

    pygame.display.update()

pygame.quit()
