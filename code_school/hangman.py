from words import words_list
import random


class Hangman:
    def __init__(self,nickname,):
        self.nickname=nickname
        print('Hello ',nickname)
        self.score=0
        self.usedletters=set()
        self.alphabet='abcdefghijklmnopqrstuvwxyz'
        self.turns=6
        self.words_list=words_list
        self.game_over= False
    def new_word(self,):
        self.word=random.choice(self.words_list)
        self.word_letters=set(self.word)
        self.result=list('* '*len(self.word))
        if len(self.word)==len(self.word_letters):
            self.bonus=5
        else:
            self.bonus=0
    def check_word(self,letter):
        if letter in self.word_letters:
            self.word_letters.remove(letter)
            self.score+=5+self.bonus
            self.result=[i if i in self.usedletters else '*' for i in self.word]
        else:
            self.turns-=1
            print('Invalid Letter')
    def new_game(self,):
        #self.new_word()
        print('* '*len(self.word))
        if self.turns>0 and len(self.word_letters)>0:
            letter=input('Guess a letter, '+self.nickname+'. Your score is '+str(self.score)+'\n')
            if letter in self.alphabet:
                if not letter in self.usedletters:
                    self.usedletters.add(letter)
                    self.check_word(letter)
                else:
                    print('Letter already used')
                for i in self.result:
                    print(i,end=' ')
                print()
            else:
                print('Invalid character')
            print(self.usedletters)
        else:
            self.game_over=True
            self.turns=6
            self.usedletters=set()
player=Hangman('Guest')
while True:
    answer = input('Would you like to play hangman? (y/n)')
    if answer.lower() == 'y':
        player.game_over=False
        player.new_word()
        while not (player.game_over):
            player.new_game()
    else:
        break

