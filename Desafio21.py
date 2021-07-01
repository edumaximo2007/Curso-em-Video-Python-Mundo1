from pygame import mixer
mixer.init()
mixer.music.load('01.mp3')
mixer.music.play()
print('-=-'*10)
print('''\033[7m]           DESAFIO 21           \033[m''')
print('-=-'*10)
print('\033[1mFaça um programa em Python que abra e reproduza o áudio de um arquivo MP3.\033[m')
print('')
pause = str(input('Pausar a music: '))
player = str(input('Play music:'))






