import random

class Robot:

    def __init__(self):
        self.batteryCharge = 5.0

    def move(self, steps):
        print('start moving')
        for i in range(1,steps):
            if self.batteryCharge > 0:
                print(f'{i} ')
                self.batteryCharge -= 0.5
                i += 1
            else:
                print('Out of battery')
                break
        print('Stop moving')
    
    def recharge(self, charge):
        try:
            print(f'Recharge for {charge}')
            self.batteryCharge += charge
            print(f'Battery level: {self.batteryCharge}')
        except:
            print('Invalid input for recharging!')

class Robot1(Robot):
    '''Child class of robot with speaking capability.'''
    def __init__(self):
        self.content = []   

    def set_content(self, new_content):
        self.content = new_content

    def speak(self):
        i = random.randint(0, len(self.content)-1)
        print(self.content[i])

def main():
        r = Robot1()
        u1 = ["Exterminate, Exterminate!", "I obey!", "You cannot escape.", "Robots do not feel fear.", "The Robots must survive!" ] 
        r.set_content(u1)
        r.speak()
        r.speak()
        r.speak()



if __name__ == "__main__":
    main()


