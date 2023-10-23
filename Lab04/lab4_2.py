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

def main():
        r = Robot()
        r.move(20)
        r.recharge(10)
        r.move(20)

if __name__ == "__main__":
    main()