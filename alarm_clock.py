

class Alarm_clock:
    def __init__(self):
        self.current_time = ''
        self.is_on = ''
        self.alarm = ''

    def set_time(self):
        self.current_time = input('Please enter the current time: ')
        print(f'The current time is set to {self.current_time}.')

    def turn_on_off(self):
        self.is_on = input('Would you like the alarm on? y/n: ')
        if self.is_on =='y':
            self.is_on = True
            print('The alarm is on.')
        elif self.is_on =='n':
            self.is_on = False
            print('The alarm is off.')
        else:
            print('Oops! Lets try again.')
            self.is_on = input('Would you like the alarm on? y/n: ')

    def set_alarm(self):
        self.alarm = input('Please set your alarm time: ')
        print(f'The alarm is set for {self.alarm}.')



