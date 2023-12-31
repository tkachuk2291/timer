import os

from tabulate import tabulate
from clock import Timer
import datetime

start_time = datetime.datetime.now()
timer: Timer = Timer()
timer.set_timer()
timer.turn_off_turn_on_second()
end_time = datetime.datetime.now()


class TimerWritesLogs:

    @staticmethod
    def folder_check():
        os.makedirs("timer_logs", exist_ok=True)

    @staticmethod
    def pomodoro_success() -> None:
        if 20 <= timer.timer_minutes <= 25:
            with open('timer_logs/pomodoro.txt', 'a') as file_p:
                data = [
                    ['Количество минут:', timer.timer_minutes],
                    ['Запуск программы:', start_time.strftime('%Y-%m-%d %H:%M:%S')],
                    ['Вы достигли нормы помодоро!', '+'],
                    ['Время работы программы', end_time - start_time]
                ]
                table = (
                    tabulate(data,
                             tablefmt='fancy_grid',
                             colalign=('left', 'center'),
                             stralign='center')
                )
                file_p.write(table)
                file_p.write('\n\n')
                print(table)

    @staticmethod
    def pomodoro_fail() -> None:

        if timer.timer_minutes < 20:
            with open('timer_logs/bad_pomodoro.txt', 'a') as file:
                data = [
                    ['Количество минут:', timer.timer_minutes],
                    ['Запуск программы:', start_time.strftime("%Y-%m-%d %H:%M")],
                    ['Вы не достигли нормы помодоро!', '-'],
                    ['Время работы программы', end_time - start_time]
                ]
                table = (
                    tabulate(data,
                             tablefmt='fancy_grid',
                             colalign=('left', 'center'),
                             stralign='center')
                )
                file.write(table)
                file.write('\n\n')
                print(table)
