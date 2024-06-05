#faça um programa em python que abra e reproduza áudio de um arquivo MP3 ABAIXE 
import pygame #biblioteca externa ao python ( deve ser baixada antes) 
pygame.init()
pygame.mixer.music.load('fex21.mp3') #fex21.mp3 é o nome do arquivo de musica mp3 escolhido
pygame.mixer.music.play() # toca a musica ( ABAIXE O VOLUME UM POUCO ANTES DE TOCAR ELA KKKKKKKKKKKK )
input()
pygame.event.wait()#espera a musica acabar