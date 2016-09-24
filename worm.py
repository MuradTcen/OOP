'''
    коробка с яблоками: 
                а11..а1н
                ан1.. анн
                масса яблок рандомна
    червяк с весами врывается, если ябоко больше,
    то он сьедает 1/1000
    ползет к следующему
    он должеен сьесть Т-яблок
    где остался червяк
    если ч не насытился, голодный ч ползет сюда
    
    Крит. масса - рандомная
    настройки для распределения масс, размер ящика
    два языка интерфейса
    ингтерфейсные сообщения из файла 
    
    
    Technical specification:
    We have a one worm. His name is Garry.
    He is in a box with apples. He has a weighing-machine.
    He weigh every apple, if weight of apple more than KRIT_MASS,
    he eat PART_APPLE procent of apple and will go to next apple
    until he eat SIZE_EAT.   
    
'''
import random

MIN_S_E = 100
MAX_S_E = 250
KRIT_MASS = 150
PART_APPLE = 1/15
SIZE_EAT=100
M = 10
N = 5
Box = []

class Apple:
    def __init__(self,i):
        self.size=random.randint(MIN_S_E,MAX_S_E)
        self.eated = False
        self.coord = i
        
    def getCoord(self):
        return self.coord
        
    def setEated(self):
        self.eated = True
        
    def getEated(self):
        return self.eated
        
    def getSize(self):
        return self.size
            
class Worm:
     
     def __init__(self):
        self.eat = 0
        self.place = 0
        self.full=False
        
     def set_full(self):
        self.full=True
        
     def getEat(self):
        if self.eat < SIZE_EAT:
            return True
        else:
            return False
             
     def eating(self,apple):
        print ('Mass of apple',apple.coord,'is',apple.getSize())
        if apple.getSize() >= KRIT_MASS:
            apple.setEated()
            if (self.eat+PART_APPLE*apple.getSize())<=SIZE_EAT:
                self.eat += PART_APPLE*apple.getSize()
                print ('Worm ate:',apple.coord)
                print ('Mass of worm is',round(self.eat,2)) 
            else:
                self.set_full()  


     def lifeCycle(self):
        while (self.getEat() and not self.full): 
            self.eating()
            #if self.full==True: return
            self.lifeCycle()
     
           
def main():
    print ('Do you want use english? Y/N')
    inp=input()
    if inp=='Y': interface=open('eng_interface.txt','r')
    else: interface=open('rus_interface.txt','r')
    print (interface.read())
    
    garry = Worm()
    for i in range(M*N):
        Box.append(Apple(i))
    i=0
    while i<M*N:
        if garry.getEat():
            garry.eating(Box[i])
        else: break
        i+=1
        
    interface.close()
    #---------------------------
        
if __name__=="__main__":
    main()
    
