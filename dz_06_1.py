import time
class TrafficLight:
    __color = 'Red'
    __color_1 = 'Yellow'
    __color_2 = 'Green'

    def running(self):
        print(TrafficLight.__color)
        time.sleep(7)
        print(TrafficLight.__color_1)
        time.sleep(2)
        print(TrafficLight.__color_2)
        time.sleep(4)
t = TrafficLight()
t.running()