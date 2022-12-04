import random
class Hero:
    def __init__(self,name,career,ATK,Life,Mana):
        self.__name = name
        self.__career = career
        self.ATK = ATK
        self.Life = Life
        self.Mana = Mana
    
    
    def ShowName(self):
        print("Name of the Hero is {}".format(self.__name))
    def ShowCareer(self):
        print("Name of the Hero is {}".format(self.__career))
    def ShowLife(self):
        return self.Life
    def ShowMana(self):
        return self.Mana
    def ShowATK(self):
        return self.ATK
    def Life_Improve(self,number):
        self.Life += number

    def Mana_Improve(self,number):
        self.Mana += number
    
    def ATK_Improve(self,number):
        self.ATK += number
def battle(player1:Hero,player2:Hero):
    player1_mana = player1.ShowMana()
    player2_life = player2.ShowLife() 
    if player1.Mana >= 0:
        n=random.randint(1,3)
        if n == 1 and player1_mana >=100:
            player1_mana -= 100
            player1