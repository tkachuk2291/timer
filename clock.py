from word_checker import Checker
import time
import sys

minutes_seconds_timer: Checker = Checker()


class Timer:

    def __init__(self) -> None:
        self.timer: int = 0
        self.timer_minutes: int = 0
        self.customer_answer = ''
        self.customer: int = 0
        self.customer_time: float = 0.0
        self.customer_answer: str = ''

    def seconds_timer(self) -> bool:
        print('Включить подсчет секунд?(да/нет)')
        self.customer_answer = input()
        if self.customer_answer == 'да':
            print('Подсчет секунд включен')
            return True
        elif self.customer_answer == 'нет':
            print('Подсчет секунд выключен')
            return False
        else:
            print('Ответ должен быть: да или нет')
            return False

    def set_timer(self) -> None:
        print('Привествую в программе "Таймер Помодоро", готовы начать?(да/нет)')
        self.customer_answer = input()
        if self.customer_answer == "да":
            print('Введите кол-во минут:')
            self.customer = int(input())
            if self.customer <= 0:
                print('Введите количество больше 0')
                return
            else:
                print(f'Заданое кол-во минут: {self.customer}')
                print('Введите скорость:')
                self.customer_time = float(input())
                print(f'Заданая скорость: {self.customer_time}')
                time.sleep(1)
            self.customer *= 60
        elif self.customer_answer == "нет":
            sys.exit(0)
        else:
            print("Введите корректное значения")
            sys.exit(0)
    def minutes_seconds_timer(self) -> None:
        print('Начинаю Подсчет!')
        for i in range(self.customer):
            time.sleep(self.customer_time)
            self.timer += 1
            print(f'Прошло {self.timer} '
                  f'{minutes_seconds_timer.check_seconds(self.timer)}')

            if self.timer == 60:
                self.timer = 0
                self.timer_minutes += 1
                print(
                    f'Прошло {self.timer_minutes} {minutes_seconds_timer.check_minutes(self.timer_minutes)} | 0 секунд')

    def minutes_only_timer(self) -> None:
        print('Начинаю Подсчет!')
        for i in range(self.customer):
            time.sleep(self.customer_time)
            self.timer += 1
            if self.timer == 60:
                self.timer_minutes += 1
                self.timer = 0
                print(f'Прошло {self.timer_minutes} {minutes_seconds_timer.check_minutes(self.timer_minutes)}')

    def turn_off_turn_on_second(self) -> None:
        time.sleep(0)
        timer_sec: bool = self.seconds_timer()
        if timer_sec is True:
            self.minutes_seconds_timer()

        elif timer_sec is False:
            self.minutes_only_timer()
