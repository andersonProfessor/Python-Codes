# -*- coding: utf-8 -*-
"""GuessGame

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ctMZcHH2D55Smf58WHXhH9UpOALrmiKa
"""

# GuessGame - O Jogo da Advinhação

from random import randint
from playsound import playsound

play = True

while play:
  print('*'*50)
  print('Bem-vindo ao GuessGame - O Jogo da Advinhação\n')
  print('[0] - Easy \n[1] - Medium \n[2] - Hard \n[3] - Very Hard')
  print('*'*50)

  level = int(input('Selecione o nível da partida: '))

  while level < 0 or level > 3:
    print('Nível inválido, tente novamente!!!\n')
    level = int(input('Selecione o nível da partida: '))    
    
  if level == 0:
    print('\n')
    print('='*60)
    print('Você escolheu o nível EASY, está preparado? Vamos lá...')
    print('='*60)
    cpu = randint(0,10)
    player = int(input('\nTente advinhar qual número eu pensei: '))
    pts = 0
    while player != cpu:
      if player < cpu:
        playsound('errou.mp3')
        print('\nPassou perto, mas o número que pensei é maior!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
      else:
        playsound('errou.mp3')
        print('\nQuase hein, mas o número que pensei é menor!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
    
    playsound('acertou.mp3')
    print(f'\nIncrível, você acertou!!! Precisou de {pts+1} tentativas para advinhar!!!\n')
    retry = input('Quer jogar novamente? S/N: ')
    if retry.upper() == 'N':
      play = False

  if level == 1:
    print('\n')
    print('='*60)
    print('Você escolheu o nível MEDIUM, está preparado? Vamos lá...')
    print('='*60)
    cpu = randint(0,100)
    player = int(input('\nTente advinhar qual número eu pensei: '))
    pts = 0
    while player != cpu:
      if player < cpu:
        playsound('errou.mp3')
        print('\nPassou perto, mas o número que pensei é maior!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
      else:
        playsound('errou.mp3')
        print('\nQuase hein, mas o número que pensei é menor!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
    
    playsound('acertou.mp3')
    print(f'\nIncrível, você acertou!!! Precisou de {pts+1} tentativas para advinhar!!!\n')
    retry = input('Quer jogar novamente? S/N: ')
    if retry.upper() == 'N':
      play = False

  if level == 2:
    print('\n')
    print('='*60)
    print('Você escolheu o nível HARD, está preparado? Vamos lá...')
    print('='*60)
    cpu = randint(0,1000)
    player = int(input('\nTente advinhar qual número eu pensei: '))
    pts = 0
    while player != cpu:
      if player < cpu:
        playsound('errou.mp3')
        print('\nPassou perto, mas o número que pensei é maior!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
      else:
        playsound('errou.mp3')
        print('\nQuase hein, mas o número que pensei é menor!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
    
    playsound('acertou.mp3')
    print(f'\nIncrível, você acertou!!! Precisou de {pts+1} tentativas para advinhar!!!\n')
    retry = input('Quer jogar novamente? S/N: ')
    if retry.upper() == 'N':
      play = False

  if level == 3:
    print('\n')
    print('='*60)
    print('Você escolheu o nível VERY HARD, está preparado? Vamos lá...')
    print('='*60)
    cpu = randint(0,1000)
    player = int(input('\nTente advinhar qual número eu pensei: '))
    pts = 0
    cont = 1
    while player != cpu:
      if player < cpu:
        if (cont == 10):
            print('\nVocê passou do limite de 10 tentativas!!! Escolherei um novo número!!!')
            cpu = randint(0,1000)
            cont = 1        
        playsound('errou.mp3')
        print('\nPassou perto, mas o número que pensei é maior!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
        cont = cont + 1        
      else:
        if (cont == 10):
            print('\nVocê passou do limite de 10 tentativas!!! Escolherei um novo número!!!')
            cpu = randint(0,1000)
            cont = 1
        playsound('errou.mp3')
        print('\nQuase hein, mas o número que pensei é menor!!!\n')
        player = int(input('Tente advinhar qual número eu pensei: '))
        pts = pts + 1
        cont = cont + 1
    
    playsound('acertou.mp3')
    print(f'\nIncrível, você acertou!!! Precisou de {pts+1} tentativas para advinhar!!!\n')
    retry = input('Quer jogar novamente? S/N: ')
    if retry.upper() == 'N':
      play = False
