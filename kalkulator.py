class Kalkulator:
    def __init__(self, first, value, second):
        self.first = first
        self.value = value
        self.second = second
        
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def truediv(self):
        return self.first / self.second
    
    
    def printt(self):
        if self.value == '+':
            print(self.add())
        elif self.value == '-':
            print(self.sub())
        elif self.value == '*':
            print(self.mul())
        elif self.value == '/':
            print(self.truediv())
        else:
            print(f'такое операция как {self.value} нет')
chisla = Kalkulator(1, '+', 4)
chisla.printt()