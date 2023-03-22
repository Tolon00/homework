class SuperHero:
    people = 'people'
    fly = False
    def __init__(self,name,nickname,superpower,health_points,catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        
        
    def namehero(self):
        print(f'имя героя {self.name}')
    
    
    def health(self):
        return self.health_point * 2
    
    
    def __str__(self):
        return f'прозвище героя {self.nickname}\n' \
               f'суперспособность героя {self.superpower}\n' \
               f'здоровье  {self.health_point}' 
    
    
    def __len__(self):
        return len(self.catchphrase)  
     
     
Hero = SuperHero('Flash', 'Алый Бегун', 'скорость', 100, 'Все разбитые сердца до сих пор бьются.', 200)


Hero.namehero()                              
print(Hero.health())
print(Hero)
print(len(Hero))





class Superhero2(SuperHero):   #воз
    fly = True
    def health(self):
        return self.health_point ** 2
    
    
    def phrase(self):
        print('fly in the True_phrase')
    
    
    


class Superhero3(SuperHero):   #кос
    speedoflight = True
    teleportation = True
    fly = True
    def health(self):
        return self.health_point ** 2
    
    def phrase(self):
        print('fly in the True_phrase')
    
    
   
hero2 = Superhero2('Старк', 'Железный человек', 'ум', 95, 'Он - живая боевая машина… А я простой человек в железном костюме.', 150)
hero3 = Superhero3('Дарксайд', 'Бог зла', 'омега лучи', 300, 'Это могучее тело - моя церковь.', 250)


print(hero2.health())
print(hero3.health())
hero3.phrase()



class Villain(Superhero3):
    people = 'monster'
    
    
    def gen_x(self):...
        
    
    def crit(self):
        self.damage **= 2
        print(self.damage)
        
        
vil = Villain('jkjk', 'kdjfs', 'sjfkdk', 100, 'sllsjflf', 120)


Villain.crit(hero2)          