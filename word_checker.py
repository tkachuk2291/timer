import sys

timer_lists_a = [1, 21, 31, 41, 51]
timer_lists_ib = [2, 3, 4, 22, 23, 24,
                  32, 33, 34, 42, 43,
                  44, 52, 53, 54]
timer_lists_d = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                 14, 15, 16, 17, 18, 19, 20, 25,
                 26, 27, 28, 29, 30, 35, 36, 37,
                 38, 39, 40, 45, 46, 47, 48, 49,
                 50, 55, 56, 57, 58, 59, 60]


class Checker:
    @staticmethod
    def check_seconds(second: int) -> str:
        if second in timer_lists_a:
            return 'секунда'
        elif second in timer_lists_ib:
            return 'секунды'
        elif second in timer_lists_d:
            return 'секунд'

    @staticmethod
    def check_minutes(minutes: int) -> str:
        if minutes in timer_lists_a:
            return 'минута'
        elif minutes in timer_lists_ib:
            return 'минуты'
        elif minutes in timer_lists_d:
            return 'минут'


class CheckCorrectWords:

    @staticmethod
    def check_quantity() -> str:
        sum_seconds = (len(timer_lists_a)
                       + len(timer_lists_ib)
                       + len(timer_lists_d))
        if sum_seconds == 61:
            return f'Список прошел проверку, количество: {sum_seconds}'
        else:
            print(f'Список не валиден, проверьте количество, '
                  f'данное количество: {sum_seconds}')
            return '0'

    @staticmethod
    def duplicate() -> str:
        duplicate_list = {}
        sum_list = timer_lists_a + timer_lists_ib + timer_lists_d
        for num in sum_list:
            if sum_list.count(num) > 1:
                if num in duplicate_list:
                    duplicate_list[num] += 1
                else:
                    duplicate_list[num] = 1
        print(f'Список не прошел проверку, найдены дубликаты {duplicate_list}')
        return '0'


result = CheckCorrectWords()

if result.check_quantity() == '0':
    result.duplicate()
    sys.exit(1)
else:
    pass
