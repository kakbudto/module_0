import numpy as np
number = np.random.randint(1,101)      # загадали число
print ("Загадано число от 1 до 100")


def game_core(number):
    '''При использовании операндов сравнения больше и меньше резоннее всего будет вести поиск загаданного числа
    от середины диапазона 1 - 100'''
    num_min = 1 # минимальная граница диапазона возможных чисел
    num_max = 100   # максимальная граница диапазона возможных чисел
    count = 1   # заводим счетчик
    num = 0 # обозначаем переменную в которой будет хранится число

    while num != number:
        count += 1
        mid_num = (num_min + num_max)//2 # рассчитываем середину диапазона
        if mid_num == number:
            num = mid_num           # если число равно рассчетной середине, завершаем цикл
        elif mid_num < number:
            num_min = mid_num + 1   # если число больше середины, увеличиываем нижнюю границу
        else:
            num_max = mid_num - 1   # если число меньше середины, уменьшаем высшую границу

    return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return (score)


score_game(game_core)