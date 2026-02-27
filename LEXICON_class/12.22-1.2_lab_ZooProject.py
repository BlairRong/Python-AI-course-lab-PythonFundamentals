"""
Project: Zoo Simulation System
In this project, you will design and implement an object-oriented simulation of a zoo. The
goal is to apply what you have learned about object-oriented programming by building a
system where animals and visitors interact over time.
The project is designed with a low entry threshold and a high potential ceiling. Everyone is
expected to complete the minimum requirements, while more advanced solutions will
naturally extend the system with better structure, robustness, and realism.
Project Requirements
Minimum Requirements (Core Functionality)
- Implement an object-oriented zoo simulation system.
- Include a base Animal class with common attributes such as name, age, and energy level.
- Include subclasses for different animal types (for example Herbivores and Carnivores).
- Implement at least three concrete animal species with unique behaviors.
- Include a Visitor class that can interact with animals (for example feeding them).
- Simulate at least one full day in the zoo where animals eat, sleep, and interact.
- Demonstrate inheritance and method overriding.
- The program must run without errors and clearly show the simulation flow through
output.
Extended Requirements (Improved Design & Behavior)
- Manage animal energy levels consistently across all actions.
- Implement meaningful interactions between animals (for example hunting, playing, or
resting).
- Ensure that behaviors affect future simulation steps, not just printed output.
- Structure the simulation so that it can run for multiple days without code changes.
- Reduce duplicated logic through proper class design.
- Demonstrate thoughtful use of encapsulation and reuse.
Advanced Requirements (High-Quality Simulation Design)
- Make it easy to add new animal species without modifying existing logic.
- Maintain a balanced predator-prey system that avoids unrealistic extinction.
- Separate simulation logic from execution logic.
- Handle edge cases gracefully, regardless of interaction order.
- Write clean, readable code with clear structure and comments where needed.
- Demonstrate deliberate and well-reasoned design choices.
Optional Extension Tasks
- Allow the simulation to run for a configurable number of days.
- Introduce random events that influence animal or visitor behavior.
- Add a simple text-based interface for user interaction.
- Track and display statistics such as energy levels or population changes over time.

"""



#12.22 personal zoo project

import random
from abc import ABC, abstractmethod                    #abstract method, more safety

class Animal(ABC):
    def __init__(self, name, age, max_energy = 100):   #2.Include a base Animal class with common attributes such as name, age, and energy level.
        self._name = name
        self._age = age
        self._max_energy = max_energy                  #9.Manage animal energy levels consistently across all actions.
        self._energy_level = max_energy // 2           #setting the beginning energy is the half of max energy
        self._is_sleeping = False                      #12.Structure the simulation so that it can run for multiple days without code changes.
        
    @property                                          #property method
    def name(self):
        return self._name                             
    def energy_level(self):
        return self._energy_level
    @property
    def is_alive(self):
        return self._energy_level > 0
    
    def __str__(self):
        return f'{self._name}({self.__class__.__name__}), age {self._age}, energy: {self._energy_level}/{self._max_energy}'
    def _change_energy(self, amount):                  #14. Demonstrate thoughtful use of encapsulation, enerygy change method
        old_energy = self._energy_level
        self._energy_level = max(0, min(self._max_energy, self._energy_level + amount))
        return self._energy_level - old_energy
    def can_perform_actions(self, enerygy_cost):       #check animal status
        if self._is_sleeping:
            print(f"{self._name} is sleeping and cannot perform actions")
            return False
        return self._energy_level >= enerygy_cost

    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self, hours = 8):
        pass
    @abstractmethod
    def interact(self, other = None):
        pass
    def get_daily_energy_loss(self):
        return 5
        

class Herbivores(Animal):                               #3.Include subclasses for different animal types (for example Herbivores 食草动物 and Carnivores 食肉动物).
    def __init__(self, name, age):
        super().__init__(name, age)
        self._food_type = "Vegetation"
    def eat(self):                                      #7.method overriding, subtype polymorphism
        if self._is_sleeping:                           #12.Structure the simulation so that it can run for multiple days without code changes.
            print(f"{self._name}is sleeping, cannot eat.")
            return False
        energy_gained = self._change_energy(20)
        print(f"{self._name} is eating {self._food_type}. Energy + {energy_gained}")
        return True
    def sleep(self, hours = 8):
        if self._is_sleeping:
            print(f"{self._name} is already sleeping.")
            return False
        self._is_sleeping = True
        energy_gained = self._change_energy(hours * 2)
        print(f"{self._name} is sleeping for {hours} hours. Energy + {energy_gained} ")
        return True
    def wake_up(self):
        if not self._is_sleeping:
            return True
        self._is_sleeping = False
        print(f"{self._name} is wake up.")
        return True
    def interact(self, other=None):
        if not self.can_perform_actions(5):
            return False
        if other is None:
            energy_used = self._change_energy(-5)
            print(f"{self._name} is exploring the habitat. Energy {energy_used}")
            return True
        elif isinstance(other,Herbivores):              #isinstance 食草动物遇到食草动物一起玩耍
            energy_used = self._change_energy(-3)
            print(f"{self._name}and {other.name} are playing together. Energy {energy_used}") #10.Implement meaningful interactions between animals (for example hunting, playing, or resting).
            return True
        elif isinstance(other,Carnivores):              #食草动物遇到食肉动物会逃跑
            energy_used = self._change_energy(-10)
            print(f"{self._name} runs away from {other.name}. Energy {energy_used}")
            return True
        return False    

class Carnivores(Animal):                               #7.Demonstrate inheritance
    def __init__(self, name, age):
        super().__init__(name, age)
        self._food_type = "meat"
    def eat(self):
        if self._is_sleeping:                           #12.Structure the simulation so that it can run for multiple days without code changes.
            print(f"{self._name}is sleeping and cannot eat.")
            return False
        energy_gained = self._change_energy(25)
        print(f"{self._name} is eating {self._food_type}. Energy + {energy_gained}")
        return True
    def sleep(self, hours = 8):
        if self._is_sleeping:
            print(f"{self._name} is already sleeping.")
            return False
        self._is_sleeping = True
        energy_gained = self._change_energy(hours * 1)
        print(f"{self._name} is sleeping for {hours} hours. Energy + {energy_gained} ")
        return True
    def wake_up(self):
        if not self._is_sleeping:
            return True
        self._is_sleeping = False
        print(f"{self._name} is wake up.")
        return True
    def interact(self, other=None):
        if not self.can_perform_actions(8):
            return False
        if other is None:
            energy_used = self._change_energy(-8)
            print(f"{self._name} is patrolling its territory. Energy {energy_used}")
            return True
        elif isinstance(other, Herbivores):              #isinstance 食肉动物遇到食草动物 要捕猎
            energy_used = self._change_energy(-5)
            print(f"{self._name} is try to hunting {other.name}. Energy {energy_used}") #10.Implement meaningful interactions between animals (for example hunting, playing, or resting).
            return True
        elif isinstance(other, Carnivores):              #食肉动物遇到食肉动物 会休息
            energy_used = self._change_energy(+3)
            print(f"{self._name} is resting with {other.name}. Energy {energy_used}")
            return True
        return False    

class Kangaroo(Herbivores):                            #4.Implement at least three concrete animal species with unique behaviors.
    def __init__(self, name, age):
        super().__init__(name, age)                    #grass and leaves = food_type
    def eat(self):                                     #7.method overriding
        if super().eat():
            print(f"{self._name} is eating baz baz baz...")
            return True
        return False
    def interact(self, other = None):                  #7.method overriding
        if other is None:
            if self.can_perform_actions(10):
                energy_used = self._change_energy(-10)
                print(f"{self._name} is doing a back jump! Energy {energy_used}")
                return True
            return super().interact(other)
    def get_daily_energy_loss(self):
        return 8
        
    def back_jump(self):                               #4.unique behaviors
        if self.energy_level >= 8:                
            self.energy_level -= 8
            print(f"{self.name} is back jumping duang duang duang~")
            return self.energy_level
        else:
            print(f"{self.name} is too tired to back jump")
            return self.energy_level 
        
class MountainGoat(Herbivores):                  
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level, "mountain grass")
    def __str__(self):
        return f"{super().__str__()}, it says: I'm a Mountain Goat!"
    def eat(self):
        print(f"{self.name} the goat is eating cheto cheto...")
        self.energy_level += 10
        return self.energy_level
    def interact(self): 
        if self.energy_level >= 4:                  
            self.energy_level -= 4
            print(f"{self.name} is interacting yayaya~~")
            return self.energy_level
        else:
            print(f"{self.name} is too tired")
            return self.energy_level
    def mountain_jump(self):
        if self.energy_level >= 6:
            self.energy_level -= 6
            print(f"{self.name} is jumping on the mountain hop hop hop~")
            return self.energy_level
        else:
            print(f"{self.name} is too tired to jump")
            return self.energy_level

class PolarBear(Carnivores):
    def __init__(self, name, age, energy_level):
        super().__init__(name, age, energy_level, "fish and seals")
    def __str__(self):
        return f"{super().__str__()}, it says: I'm a Polar Bear!"
    def eat(self):
        print(f"{self.name} the bear is eating yum yum...")
        self.energy_level += 15
        return self.energy_level
    def interact(self):
        if self.energy_level >= 10:                 
            self.energy_level -= 10
            print(f"{self.name} is interacting mmmmmm~~")
            return self.energy_level
        else:
            print(f"{self.name} is too tired to interact")
            return self.energy_level
    def swimming(self):
        if self.energy_level >= 12:
            self.energy_level -= 12
            print(f"{self.name} is swimming in cold water siu siu siu~~")
            return self.energy_level
        else:
            print(f"{self.name} is too tired to swim")
            return self.energy_level 
        
class Visitor:                                                #5.Include a Visitor class that can interact with animals (for example feeding them).
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Visitor: {self.name}."  
    def feed_animal(self, animal):
        print(f"{self.name} is feeding the animal called {animal.name}.")
        return animal.eat()   #new add


def simulate_zoo_day():                                       #6.Simulate at least one full day in the zoo where animals eat, sleep, and interact.
    print('\n===== ZOO SIMULATION - A DAY IN THE ZOO ======') #以下内容全部都在这个函数里
        
    #create animal
    kangaroo = Kangaroo('Candy', 3, 50)
    goat = MountainGoat('Star', 4, 40)
    bear = PolarBear('Snowball', 5, 60)

    #create visitor
    visitor1 = Visitor("John")
    visitor2 = Visitor('Alice')

    #put animals and vistors into a list
    animals = [kangaroo, goat, bear]
    visitors = [visitor1, visitor2]

    #show all the animals
    print("\n=== ANIMALS IN THE ZOO ===")
    for animal in animals:
        print(animal)

    #show all the visitors
    print("\n=== VISITORS ===")
    for visitor in visitors:
        print(visitor)

    #simulate one day in the zoo #use for loop
    times_of_day = ["Morning", "Afternoon", "Evening"]

    for time in times_of_day:
        print(f"\n== TIME: {time} ==")

        if time == 'Morning':                         
            #animal eat and visitor feed animal 
            print("\nMorning Activities:")
            for animal in animals:
                animal.eat()   
            #visitor feeding animal
            print("\nVisitors Feeding Animals:")
            visitor1.feed_animal(kangaroo)
            visitor2.feed_animal(bear)
    
        elif time == 'Afternoon': 
            #animal interact and show unique behavior
            print("\nAfternoon Activities:")
            for animal in animals:
                animal.interact()
            #show the animal unique behaviors
            print("\nAnimal Special Behavior:")
            kangaroo.back_jump()
            goat.mountain_jump()
            bear.swimming()

        elif time == 'Evening': 
            #animal eat and sleep
            print("\nEvening Activities:")
            for animal in animals:
                animal.eat()

            print("Night Activities:")
            for animal in animals:
                animal.sleep()
    
    print(f"\n== END OF DAY - ANIMAL STATUS ==")
    for animal in animals:
        print(f"{animal.name}: Energy level = {animal.energy_level}")  

if __name__ == "__main__":
    simulate_zoo_day()





#12.23 personal project output example

import random
from abc import ABC, abstractmethod                         #abstract method, more safety

class Animal(ABC):
    def __init__(self, name, age, max_energy = 100):        #2.Include a base Animal class with common attributes such as name, age, and energy level.
        self._name = name
        self._age = age
        self._max_energy = max_energy                       #9.Manage animal energy levels consistently across all actions.
        self._energy_level = max_energy // 2                #setting the beginning energy is the half of max energy
        self._is_sleeping = False                           #12.Structure the simulation so that it can run for multiple days without code changes.

    @property                                               #property method
    def name(self):
        return self._name                             
    def energy_level(self):
        return self._energy_level
    @property
    def is_alive(self):
        return self._energy_level > 0
    
    def __str__(self):
        return f'{self._name}({self.__class__.__name__}), age {self._age}, energy: {self._energy_level}/{self._max_energy}'
    def _change_energy(self, amount):                       #14. Demonstrate thoughtful use of encapsulation, enerygy change method
        old_energy = self._energy_level
        self._energy_level = max(0, min(self._max_energy, self._energy_level + amount))
        return self._energy_level - old_energy
    def can_perform_actions(self, enerygy_cost):             #check animal status
        if self._is_sleeping:
            print(f"{self._name} is sleeping and cannot perform actions")
            return False
        return self._energy_level >= enerygy_cost

    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self, hours = 8):
        pass
    @abstractmethod
    def interact(self, other = None):
        pass
    def get_daily_energy_loss(self):
        return 5
        

class Herbivores(Animal):                                    #3.Include subclasses for different animal types (for example Herbivores 食草动物 and Carnivores 食肉动物).
    def __init__(self, name, age):
        super().__init__(name, age)
        self._food_type = "Vegetation"
    def eat(self):                                           #7.method overriding, subtype polymorphism
        if self._is_sleeping:                                #12.Structure the simulation so that it can run for multiple days without code changes.
            print(f"{self._name}is sleeping, cannot eat.")
            return False
        energy_gained = self._change_energy(20)
        print(f"{self._name} is eating {self._food_type}. Energy + {energy_gained}")
        return True
    def sleep(self, hours = 8):
        if self._is_sleeping:
            print(f"{self._name} is already sleeping.")
            return False
        self._is_sleeping = True
        energy_gained = self._change_energy(hours * 2)
        print(f"{self._name} is sleeping for {hours} hours. Energy + {energy_gained} ")
        return True
    def wake_up(self):
        if not self._is_sleeping:
            return True
        self._is_sleeping = False
        print(f"{self._name} is wake up.")
        return True
    def interact(self, other=None):
        if not self.can_perform_actions(5):
            return False
        if other is None:
            energy_used = self._change_energy(-5)
            print(f"{self._name} is exploring the habitat. Energy {energy_used}")
            return True
        elif isinstance(other,Herbivores):                  #isinstance 食草动物遇到食草动物一起玩耍
            energy_used = self._change_energy(-3)
            print(f"{self._name}and {other.name} are playing together. Energy {energy_used}") #10.Implement meaningful interactions between animals (for example hunting, playing, or resting).
            return True
        elif isinstance(other,Carnivores):                  #食草动物遇到食肉动物会逃跑
            energy_used = self._change_energy(-10)
            print(f"{self._name} runs away from {other.name}. Energy {energy_used}")
            return True
        return False    

class Carnivores(Animal):                                   #7.Demonstrate inheritance
    def __init__(self, name, age):
        super().__init__(name, age)
        self._food_type = "meat"
    def eat(self):
        if self._is_sleeping:                              #12.Structure the simulation so that it can run for multiple days without code changes.
            print(f"{self._name}is sleeping and cannot eat.")
            return False
        energy_gained = self._change_energy(25)
        print(f"{self._name} is eating {self._food_type}. Energy + {energy_gained}")
        return True
    def sleep(self, hours = 8):
        if self._is_sleeping:
            print(f"{self._name} is already sleeping.")
            return False
        self._is_sleeping = True
        energy_gained = self._change_energy(hours * 1)
        print(f"{self._name} is sleeping for {hours} hours. Energy + {energy_gained} ")
        return True
    def wake_up(self):
        if not self._is_sleeping:
            return True
        self._is_sleeping = False
        print(f"{self._name} is wake up.")
        return True
    def interact(self, other=None):
        if not self.can_perform_actions(8):
            return False
        if other is None:
            energy_used = self._change_energy(-8)
            print(f"{self._name} is patrolling its territory. Energy {energy_used}")
            return True
        elif isinstance(other, Herbivores):                  #isinstance 食肉动物遇到食草动物 要捕猎
            energy_used = self._change_energy(-5)
            print(f"{self._name} is try to hunting {other.name}. Energy {energy_used}") #10.Implement meaningful interactions between animals (for example hunting, playing, or resting).
            return True
        elif isinstance(other, Carnivores):                 #食肉动物遇到食肉动物 会休息
            energy_used = self._change_energy(+3)
            print(f"{self._name} is resting with {other.name}. Energy {energy_used}")
            return True
        return False    

class Kangaroo(Herbivores):                                  #4.Implement at least three concrete animal species with unique behaviors.
    def __init__(self, name, age):
        super().__init__(name, age)                    
    def eat(self):                                           #7.method overriding
        if super().eat():
            print(f"{self._name} is eating baz baz baz...")
            return True
        return False   
    def interact(self, other = None):                         #7.method overriding
        if other is None:
            if self.can_perform_actions(10):
                energy_used = self._change_energy(-10)
                print(f"{self._name} is doing a back jump! Energy {energy_used}") #4 unique behaviors
                return True
            return super().interact(other)
    def get_daily_energy_loss(self):
        return 8

class MountainGoat(Herbivores):                  
    def __init__(self, name, age):
        super().__init__(name, age)                    
    def interact(self, other = None):                         #7.method overriding
        if other is None:
            if self.can_perform_actions(8):
                energy_used = self._change_energy(-8)
                print(f"{self._name} is climb the rocky terrain! Energy {energy_used}") #4 unique behaviors
                return True
            return super().interact(other)
    def get_daily_energy_loss(self):
        return 4

class PolarBear(Carnivores):
    def __init__(self, name, age):
        super().__init__(name, age)                    
    def interact(self, other = None):                         #7.method overriding
        if other is None:
            if self.can_perform_actions(12):
                energy_used = self._change_energy(-12)
                print(f"{self._name} swims in the ice water! Energy {energy_used}") #4 unique behaviors
                return True
            return super().interact(other)
    def get_daily_energy_loss(self):
        return 10
    
class Visitor:                                                #5.Include a Visitor class that can interact with animals (for example feeding them).
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def __str__(self):
        return f"Visitor: {self._name}."  
    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self._name} trys to feed {animal.name}...")
            return animal.eat() 
        return False


#12.29 
class Zoo:                                                     #12.Structure the simulation so that it can run for multiple days without code changes.
    def __init__(self):
        self._animals = []
        self._visitors = []
        self._day_count = 0
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)                       #append method #15
            print(f"Added {animal.name} to the zoo")
    def add_visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitors.append(visitor)
            print(f"Added {visitor.name} enters the zoo")
    def _wake_all_animals(self):
        for animal in self._animals:
            if isinstance(animal,(Herbivores, Carnivores)):
                animal.wake_up()
    def _apply_daily_energy_loss(self):
        for animal in self._animals:
            energy_loss = animal.get_daily_energy_loss()
            animal._change_energy(-energy_loss)
    def simulate_day(self):                                    
        self._day_count += 1
        print(f"==== DAY{self._day_count} IN THE ZOO ===")

        self._wake_all_animals()                             #wake up all animals
        self._apply_daily_energy_loss()                      #use daily energy loss 




#12.22/23/29/30 Project: Zoo Simulation System                       

import random                                                     ##后面用到Random Module 
from abc import ABC, abstractmethod                               #20.use ABC method
class Animal(ABC):                                                #1.Implement an object-oriented zoo simulation system.
    def __init__(self, name, age, energy=50):                     ##2.Include a base Animal class with common attributes such as name, age, and energy level.  energy = 50 是给Animal类构造函数设置的默认参数，如果创建一个animal对象时，没有特别指定能量值，它就会默认值50，这是味了保证动物一开始有个默认值，不至于一开始是0，但我也可以在创建动物的是传入值，比如 kangaroo，3， 60， 60就是初始能量值
        self.name = name                                          #18.handle wdge cases gracefully, regardless of interaction order 处理边界情况 不检查类型 但有默认值
        self.age = age
        self.energy = max(0, min(100, energy))                    ##9&18.manage animal energy levels consistently across all actions 能量管理一致：0-100范围, 能量边界 min(0, max(100,...))  built in function max(0,...) 返回0到...最大的那个数， min(100, energy):返回100到energy中最小的那个，
        self.is_alive = True   
    @abstractmethod                                                                                              
    def eat(self):
        pass
    def sleep(self):
        pass
    def interact(self, other = None):
        pass

class Herbivores(Animal):                                         #3.Include subclasses for different animal types (for example Herbivores 食草动物 and Carnivores 食肉动物).
    def eat(self):                                           
        self.energy = min(100, self.energy +15)                   ##min()函数是确保能量增加后不超过100，如果能量+15后超过100则取100         
        return f"{self.name} is eating grass."
    def sleep(self):
        self.energy = min(100, self.energy +10)                    
        return f"{self.name} is sleeping."
    def interact(self, other = None):                             ##other=None 这是给参数other设置默认值为None, 这意味着调用 interact方法时，可以传入一个动物对象作为参数（表示和这个动物互动），也可以不传，不传的话就是下面的这些行为 自己玩耍 或者不玩耍. 在Carnivores的interact方法中，如果other是Herbivores，就会发生捕猎行为           
        if self.energy < 5:                                       #11.Ensure that behaviouis affect futur simulation steps, not just printed output
            return f"{self.name} is too tired to play."
        self.energy -= 5
        return f"{self.name} is playing."
            
class Carnivores(Animal):                                         #3.Include subclasses for different animal types (for example Herbivores 食草动物 and Carnivores 食肉动物).
    def eat(self):                                           
        self.energy = min(100, self.energy +20)                    
        return f"{self.name} is eating meat."
    def sleep(self):
        self.energy = min(100, self.energy +12)                    
        return f"{self.name} is sleeping."
    def interact(self, other = None):                            
        if self.energy < 8:                                       #11.Ensure that behaviouis affect futur simulation steps, not just printed output
            return f"{self.name} is too tired to hunt."
        self.energy -= 8
        if isinstance(other, Herbivores):                         ##在Carnivores的interact方法中，如果other是Herbivores，就会发生捕猎行为
            return f"{self.name} is trying to hunt {other.name}."
        return f"{self.name} is roaming around."                                                               

class Kangaroo(Herbivores):                                       #4.Implement at least three concrete animal species with unique behaviors.
    def eat(self):                                                #7.inheritance and method overriding
        self.energy = min(100, self.energy + 12)                  #13. class design
        return f"{self.name} is munching on leaves."                          
    def interact(self, other = None):                                      
        if self.energy < 6:
            return f"{self.name} is too tired."
        self.energy -= 6
        return f"{self.name} is hopping around!"                  #4.unique behaviors            

class MountainGoat(Herbivores):                                   #7.inheritance
    def eat(self):                                                #7.method overriding
        self.energy = min(100, self.energy + 14)
        return f"{self.name} is eating mountain grass."                          
    def interact(self, other = None):                                      
        if self.energy < 7:
            return f"{self.name} is too tired."
        self.energy -= 7
        return f"{self.name} is climbing the mountain."           #4.unique behaviors            

class PolarBear(Carnivores):                                      #7.inheritance
    def eat(self):                                                #7.method overriding
        self.energy = min(100, self.energy + 25)
        return f"{self.name} is eating fish."                          
    def interact(self, other = None):                                      
        if self.energy < 10:
            return f"{self.name} is too tired."
        self.energy -= 7
        return f"{self.name} is swimming."                        #4.unique behaviors            
    
class Visitor:                                                    #5.Include a Visitor class that can interact with animals (for example feeding them).
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):                                ##参数 animal是Animal对象或者其子类对象，Aniaml类有name属性，所以animal.name就是访问这个动物的名字。
        return f"{self.name} trys to feed {animal.name}."

class Ecosystem:                                                  #16&20.maintain a balanced predator-prey system that avoids unrealistic extinction 平衡的捕食系统, 平衡系统设计，管理动物园中的动物，并模拟动物之间的互动
    def __init__(self):
        self.herbivores = []
        self.carnivores = []
    def add_animal(self, animal):                                 #17.separate simulation logic from execution logic 分离逻辑 生态系统管理与动物管理分离
        if isinstance(animal, Herbivores):                        #14.封装 encapsulation and reuse
            self.herbivores.append(animal) 
        else:
            self.carnivores.append(animal)                      
    def simulate_interaction(self):                               #模拟捕食系统 避免灭绝
        if not self.herbivores or not self.carnivores:            #18.处理边界： 空列表检查
            return "Not enought animals to simulate interaction."
        carnivore = random.choice(self.carnivores)                #16.平衡:食肉动物不会杀死食草动物
        herbivore = random.choice(self.herbivores)                #20.demonstrate deliberate and well-reasoned degin choices                                             
        success_chance = 0.3 if herbivore.energy > 30 else 0.6    #食草动物能量越低越容易被捕食 
        if random.random() < success_chance and carnivore.energy > 15:
            carnivore.energy = min(100, carnivore.energy + 20)
            herbivore.energy = max(0, herbivore.energy - 25)
            return f"{carnivore.name} is hunting {herbivore.name} successfully!"  #10. interactions between animals hunting playing and resting 
        else:
            carnivore.energy = max(0, carnivore.energy - 10)
            return f"{carnivore.name} failed to hunt {herbivore.name}."

class ZooSimulator:                                               #17.separate simulation logic from execution logic 分离逻辑 生态系统管理与动物管理分离
    def __init__(self):
        self.ecosystem = Ecosystem()
        self.visitors = []
        self.day = 0
    def add_animal(self, animal):
        self.ecosystem.add_animal(animal)
    def add_visitor(self, visitor):
        self.visitors.append(visitor)
    
    def simulate_day(self):                                       #6.simulate at least one full day in the zoo where animals eat, sleep, and interact
        self.day += 1  
        print(f"\n--- Day {self.day} at the Zoo ---")
        all_animals = self.ecosystem.herbivores + self.ecosystem.carnivores
        
        print(f'\nMorning Activities:')
        for animal in all_animals:
            print(f"{animal.eat()}")
        if self.visitors:
            visitor = random.choice(self.visitors)
            animal = random.choice(all_animals)
            print(f"{visitor.feed_animal(animal)}")
        
        print(f"\nAfternoon Activities:")
        for animal in all_animals:
            if animal.energy > 10:                                #18.处理边界情况：低能量检查
                print(f"{animal.interact()}")
        print(f"{self.ecosystem.simulate_interaction()}")         #生态系统互动

        print(f"\nEvening Activities:")
        for animal in all_animals:
            print(f"{animal.sleep()}")
        for animal in all_animals:                                #自然能量消耗
            animal.energy = max(0, animal.energy -5)
        
        self._show_status()                                       #8.显示动物状态 the program must run without errors and clearly show the simulation flow through output
    def _show_status(self):
        print(f"\nAnimal Status Report:")
        for animal in self.ecosystem.herbivores + self.ecosystem.carnivores:
            status = "Health" if animal.energy > 40 else "Weak" if animal.energy >20 else "Danger"
            print(f"{animal.name} energy is: {animal.energy}, status is {status}.")

def simulate_multiple_days(simulator, days):                      #12. structure the simulation so that it can run for multiple days without code changes.
    for _ in range(days):
        simulator.simulate_day()

def main():                                                       #main function 整合所有功能
    simulator = ZooSimulator()                                    #create simulator
    simulator.add_animal(Kangaroo("Kangaroo Candy", 3, 60))       #create animal information, 60就是传入的参数 初始能量值
    simulator.add_animal(MountainGoat("MountainGoat Star", 4, 50))
    simulator.add_animal(PolarBear("PolarBear Snowball", 5, 70))
    
    class Tiger(Carnivores):                                      #15.easy to add new animal species  use inheritance method                                
        def eat(self):                                                
            self.energy = min(100, self.energy + 22)
            return f"{self.name} is eating deer."
        def interact(self, other = None):                                      
            if self.energy < 12:
                return f"{self.name} is too tired."
            self.energy -= 12
            return f"{self.name} is roahing."
    simulator.add_animal(Tiger("Tiger Toto", 6, 80))             #add new animal information
    
    simulator.add_visitor(Visitor("John"))                       #create visitor information
    simulator.add_visitor(Visitor("Alice"))

    #模拟开始
    print("\n--- Zoo Simulation System --- START")
    simulate_multiple_days(simulator, 3)                         #模拟3天
    print(f"\n--- Zoo Simulation System --- END")

if __name__ == "__main__":                                       #call 调用主函数
    main()



#2025.12.22/23/29/30 2026.1/2 Project: Zoo Simulation System                       

import random                                                     ##后面用到Random Module 
from abc import ABC, abstractmethod                               #20.use ABC method
class Animal(ABC):                                                #1.Implement an object-oriented zoo simulation system.
    def __init__(self, name, age, energy=50):                     ##2.Include a base Animal class with common attributes such as name, age, and energy level.  energy = 50 是给Animal类构造函数设置的默认参数，如果创建一个animal对象时，没有特别指定能量值，它就会默认值50，这是味了保证动物一开始有个默认值，不至于一开始是0，但我也可以在创建动物的是传入值，比如 kangaroo，3， 60， 60就是初始能量值
        self.name = name                                          #18.handle wdge cases gracefully, regardless of interaction order 处理边界情况 不检查类型 但有默认值
        self.age = age
        self.energy = max(0, min(100, energy))                    ##9&18.manage animal energy levels consistently across all actions 能量管理一致：0-100范围, 能量边界 min(0, max(100,...))  built in function max(0,...) 返回0到...最大的那个数， min(100, energy):返回100到energy中最小的那个，
        self.is_alive = True
    def __str__(self):                                         #1.2 new add
        status = "alive" if self.is_alive else "dead"
        return f"{self.name} {self.age} years, energy:{self.energy}, {status}"
    def check_if_alive(self):                                  #1.2 use is_alive
        if self.energy == 0:
            self.is_alive == False
        return self.is_alive   
    @abstractmethod                                                                                              
    def eat(self):
        pass
    @abstractmethod                                            #1.2 new add
    def sleep(self):
        pass
    @abstractmethod                                            #1.2 new add
    def interact(self, other = None):
        pass

class Herbivore(Animal):                                       #1.2改为单数singular 3.Include subclasses for different animal types (for example Herbivores 食草动物 and Carnivores 食肉动物).
    def eat(self):                                           
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot eat."
        self.energy = min(100, self.energy +15)                   ##min()函数是确保能量增加后不超过100，如果能量+15后超过100则取100         
        return f"{self.name} is eating grass."
    def sleep(self):
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot sleep."
        self.energy = min(100, self.energy +10)                    
        return f"{self.name} is sleeping."
    def interact(self, other = None):                             ##other=None 这是给参数other设置默认值为None, 这意味着调用 interact方法时，可以传入一个动物对象作为参数（表示和这个动物互动），也可以不传，不传的话就是下面的这些行为 自己玩耍 或者不玩耍. 在Carnivores的interact方法中，如果other是Herbivores，就会发生捕猎行为           
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead."
        if self.energy < 5:                                       #11.Ensure that behaviouis affect futur simulation steps, not just printed output
            return f"{self.name} is too tired to play."
        self.energy -= 5
        if other is None:                                      #1.2 Interaction design: let interact(other) actually interact You wrote interact(self, other=None) but you almostalways call animal.interact() without an “othr”.If you want to upgrade:randomly pick a partner animal and call interact(partner) sometimes,then your Carnivores.interact() hunting message becomes meaningful without relying only on Ecosystem.
            return f"{self.name}is playing alone."
        elif isinstance(other, Herbivore):
            return f"{self.name} is playing with {other.name}."
        elif isinstance(other, Carnivore):
            return f"{self.name} runs away from {other.name}!"
                    
class Carnivore(Animal):                                       #1.2改为单数singular 3.Include subclasses for different animal types (for example Herbivores 食草动物 and Carnivores 食肉动物).
    def eat(self):
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot eat."                                           
        self.energy = min(100, self.energy +20)                    
        return f"{self.name} is eating meat."
    def sleep(self):
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot sleep."
        self.energy = min(100, self.energy +12)                    
        return f"{self.name} is sleeping."
    def interact(self, other = None): 
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead."                           
        if self.energy < 8:                                       #11.Ensure that behaviouis affect futur simulation steps, not just printed output
            return f"{self.name} is too tired to hunt."
        self.energy -= 8
        if isinstance(other, Herbivore):                       ##1.2 new add. 在Carnivores的interact方法中，如果other是Herbivores，就会发生捕猎行为
            if self.energy > 10 and random.random() < 0.5:     #1.2 50% 成功率
                prey_energy_loss = 30
                other.energy = max(0, other.energy - prey_energy_loss)
                other.check_if_alive()
                self.energy = min(100, self.energy + 20)
                return f"{self.name} is successfully hunts {other.name}."
            else:
                return f"{self.name} tries to hunt {other.name} but fails."
        elif isinstance(other, Carnivore):
            return f"{self.name} and {other.name} are challenging each other."
        else:
            return f"{self.name} is roaming around."                                                              

class Kangaroo(Herbivore):                                        #4.Implement at least three concrete animal species with unique behaviors.
    def eat(self):                                                #7.inheritance and method overriding
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot eat."
        self.energy = min(100, self.energy + 12)                  #13. class design
        return f"{self.name} is munching on leaves."                          
    def interact(self, other = None): 
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead."                                     
        if self.energy < 6:
            return f"{self.name} is too tired to hop."
        self.energy -= 6
        if other is None:                                      #1.2 new add
            return f"{self.name} is hopping around!"               #4.unique behaviors 
        else:
            return super().interact(other)                     #1.2 new add       

class MountainGoat(Herbivore):                                     #7.inheritance
    def eat(self):
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot eat."                                                #7.method overriding
        self.energy = min(100, self.energy + 14)
        return f"{self.name} is eating mountain grass."                          
    def interact(self, other = None):  
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead."                                    
        if self.energy < 7:
            return f"{self.name} is too tired to climb."
        self.energy -= 7
        if other is None:
            return f"{self.name} is climbing the mountain"          #4.unique behaviors 
        else:
            return super().interact(other)
            
class PolarBear(Carnivore):                                         #7.inheritance
    def eat(self): 
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot eat."                                                 #7.method overriding
        self.energy = min(100, self.energy + 25)
        return f"{self.name} is eating fish."                          
    def interact(self, other = None):
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead."                                        
        if self.energy < 10:
            return f"{self.name} is too tired to swimming."
        self.energy -= 10
        if other is None:
            return f"{self.name} is swimming in cold water."        #4.unique behaviors 
        else:
            return super().interact(other)                         

class Tiger(Carnivore):                                             #15.easy to add new animal species  use inheritance method                                
    def eat(self):  
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead and cannot eat."                                                
        self.energy = min(100, self.energy + 22)
        return f"{self.name} is eating deer."
    def interact(self, other = None):
        if not self.check_if_alive():                          #1.2 new add
            return f"{self.name} is dead."                                        
        if self.energy < 12:
            return f"{self.name} is too tired roar."
        self.energy -= 12
        if other is None:                                      #1.2 new add
            return f"{self.name} is roahing loudly!"
        else:
            return super().interact(other)

class Visitor:                                                    #5.Include a Visitor class that can interact with animals (for example feeding them).
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):                                ##参数 animal是Animal对象或者其子类对象，Aniaml类有name属性，所以animal.name就是访问这个动物的名字。
        if not animal.is_alive:                               #1.2 new add
            return f"{self.name} is trys to feed {animal.name} but is dead."  
        return f"{self.name} tries to feed {animal.name}. {animal.eat()}."

class Ecosystem:                                                  #16&20.maintain a balanced predator-prey system that avoids unrealistic extinction 平衡的捕食系统, 平衡系统设计，管理动物园中的动物，并模拟动物之间的互动
    def __init__(self):
        self.herbivores = []
        self.carnivores = []
    def add_animal(self, animal):                                 #17.separate simulation logic from execution logic 分离逻辑 生态系统管理与动物管理分离
        if isinstance(animal, Herbivore):                         #14.封装 encapsulation and reuse
            self.herbivores.append(animal) 
        elif isinstance(animal, Carnivore):                  #1.2 new add make it feel more real you could add: if herbivore energy hits 0 -> remove it from ecosystem list (or mark dead). This also prevents unrealistic infinite prey surviving forever.
            self.carnivores.append(animal)
    def remove_dead_animals(self):                           #1.2 new add
        self.herbivores = [animal for animal in self.herbivores if animal.is_alive]
        self.carnivores = [animal for animal in self.carnivores if animal.is_alive]                            
    def simulate_interaction(self):                               #模拟捕食系统 避免灭绝
        alive_herbivores = [h for h in self.herbivores if h.is_alive]
        alive_carnivores = [c for c in self.carnivores if c.is_alive]
        if not alive_herbivores or not alive_carnivores:     #1.2 new add 18.处理边界： 空列表检查
            return "Not enought animals to simulate interaction."
        carnivore = random.choice(alive_carnivores)                #16.平衡:食肉动物不会杀死食草动物
        herbivore = random.choice(alive_herbivores)                #20.demonstrate deliberate and well-reasoned degin choices                                             
        success_chance = 0.3 if herbivore.energy > 30 else 0.6    #食草动物能量越低越容易被捕食 
        if random.random() < success_chance and carnivore.energy > 15:
            carnivore.energy = min(100, carnivore.energy + 20)
            herbivore.energy = max(0, herbivore.energy - 25)
            herbivore.check_if_alive()
            result = f"{carnivore.name} successfully hunt {herbivore.name}"  #10. interactions between animals hunting playing and resting 
            if not herbivore.is_alive:
                result += f"{herbivore.name} has died."
            return result
        else:
            carnivore.energy = max(0, carnivore.energy - 10)
            carnivore.check_if_alive()
            return f"{carnivore.name} failed to hunt {herbivore.name}."
    def get_all_animals(self):                               #1.2 new add
        return [animal for animal in self.herbivores + self.carnivores if animal.is_alive]

class ZooSimulator:                                               #17.separate simulation logic from execution logic 分离逻辑 生态系统管理与动物管理分离
    def __init__(self):
        self.ecosystem = Ecosystem()
        self.visitors = []
        self.day = 0
    def add_animal(self, animal):
        self.ecosystem.add_animal(animal)
    def add_visitor(self, visitor):
        self.visitors.append(visitor)
    def _animal_interaction(self, animal, all_animals):     #1.2 new add 处理动物之间的互动
        if len(all_animals) > 1:
            other_animals = [a for a in all_animals if a != animal]
            if other_animals:
                other = random.choice(other_animals)
                return animal.interact(other)
            return animal.interact()

    def simulate_day(self):                                       #6.simulate at least one full day in the zoo where animals eat, sleep, and interact
        self.day += 1  
        print(f"\n--- Day {self.day} at the Zoo ---")
        self.ecosystem.remove_dead_animals()                #1.2 remove dead animals
        all_animals = self.ecosystem.get_all_animals()
        if not all_animals:                                 #1.2check if still have alive animal
            print("All animals have died. Simulation ended.")
            return False
        print(f"\nAnimals alive: {len(all_animals)}")
        
        print(f'\nMorning Activities:')
        for animal in all_animals:
            print(f"{animal.eat()}")
        if self.visitors and all_animals:                   #1.2 new add 
            visitor = random.choice(self.visitors)
            animal = random.choice(all_animals)
            print(f"\n{visitor.feed_animal(animal)}")
        
        print(f"\nAfternoon Activities:")
        for animal in all_animals:
            print(f"{self._animal_interaction(animal,all_animals)}") #1.2 new add
        interaction_result = self.ecosystem.simulate_interaction()
        print(f"\n Ecosystem interaction: {interaction_result}")

        print(f"\nEvening Activities:")
        for animal in all_animals:
            print(f"{animal.sleep()}")
        for animal in all_animals:                          #1.2 new add 自然能量消耗
            old_energy = animal.energy
            animal.energy = max(0, animal.energy -5)
            energy_loss = old_energy - animal.energy
            animal.check_if_alive()
            print(f"{animal.name} loses {energy_loss} energy during the night.")
        
        self._show_status() 
        return True                                       #1.2 new add 8.显示动物状态 the program must run without errors and clearly show the simulation flow through output
    def _show_status(self):
        all_animals = self.ecosystem.get_all_animals()
        if not all_animals:
            print("\nNo animals alive.")
            return
        print(f"\n==== Animal Status Report ==== :")
        for animal in all_animals:
            if animal.energy > 60:
                status = "Excellent"
            elif animal.energy > 40:
                status = "Healthy"
            elif animal.energy > 20:
                status = "Weak"
            elif animal.energy >0:
                status = "Danger"
            else:
                status = "Dead"        
            print(f"{animal.name}: Energy = {animal.energy}, Status is {status}.")

def simulate_multiple_days(simulator, days):                   #1.2 new add 12. structure the simulation so that it can run for multiple days without code changes.
    for day in range(1, days + 1):
        print("\n\n=====STARTING SIMULATION FOR DAY {day}=====")
        if not simulator.simulate_day():
            print("\nSimulation ended early because all animals died.")
            break

def main():                                                       #main function 整合所有功能
    simulator = ZooSimulator()                                    #create simulator
    simulator.add_animal(Kangaroo("Kangaroo Candy", 3, 60))       #create animal information, 60就是传入的参数 初始能量值
    simulator.add_animal(MountainGoat("MountainGoat Star", 4, 50))
    simulator.add_animal(PolarBear("PolarBear Snowball", 5, 70))
    simulator.add_animal(Tiger("Tiger Toto", 6, 80))             #add new animal information
    
    simulator.add_visitor(Visitor("John"))                       #create visitor information
    simulator.add_visitor(Visitor("Alice"))

    #模拟开始
    print("\n--- Zoo Simulation System --- START")
    simulate_multiple_days(simulator, 3)                         #模拟3天
    print(f"\n--- Zoo Simulation System --- END")

if __name__ == "__main__":                                       #call 调用主函数
    main()


