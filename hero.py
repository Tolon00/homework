class SuperHero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_points
        self.catchphrase = catchphrase
        
        
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
     
     
Hero = SuperHero('Flash', 'Алый Бегун', 'скорость', 100, 'Все разбитые сердца до сих пор бьются.')


Hero.namehero()                              
print(Hero.health())
print(Hero)
print(len(Hero))