class Bank:
    # a = float(input())
    def __init__(self,name,balanse):
        self._name = name
        self._balanse = balanse
        
        
    def moneyX(self):
        self._balanse += a
        return self._balanse
    
    def _kill(self):
        self._balanse = 0
        print(self._balanse) 
        
    
    def __jackpot(self):
        self._balanse *= 10
        return self._balanse
    
    def _ob(self):
        b = c
        b += self._balanse
        return b
        
    
    
        
        
    
    def __str__(self):
        return f'{self._name} {self._balanse}'
ac = Bank('Tolon', 800000)
ac2 = Bank('Adyl', 1000)



# a = float(input())
# ac.moneyX()


# ac._kill()
# print(ac._balanse)






# c = ac._balanse  
# print(ac2._ob())




class Bank2(Bank):
    def get_name(self):
        return self._name
    def set_name(self, name2):
        self._name = name2
    def get_balanse(self):
        return self._balanse
    def set_balanse(self,balanse2):
        self._balanse = balanse2
        
# ac3 = Bank2('Beka', 1000)
# print(ac3)
# ac3.set_name('you')
# print(ac3.get_name())
# ac3.set_balanse(3000)
# print(ac3.get_balanse())




class Bank3(Bank):
    @property
    def proname(self):
        return self.name + ' ' + self._balanse
    




ac4 = Bank3('aaaa', 1000)
print(ac4._name)
print(ac4)
ac4._name = 'dkjfk'
print(ac4._name)
print(ac4)
# print(ac4._name)
        
        
        

  