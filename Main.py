def play_game():
    pool = """------------
|_1_||_2_||_3_|
|_4_||_5_||_6_|
|_7_||_8_||_9_|"""

    def print_pool(p):
        print(p)
    t = True
    com = ''
    com1 = ''
    nums = '123456789'
    print_pool(pool)
    while t:
        # Ход крестиков
        x = input("Поставишь крест? (1-9): ")
        while x not in nums:
            x = input("Поставишь крест? (1-9): ")
        if x not in pool:
            print("Эта ячейка уже занята или недопустима. Попробуйте снова.")
            continue
        pool = pool.replace(x, 'x')
        nums = nums.replace(x, '')
        com += x
        print_pool(pool)
        # Ход нолика
        o = input("Поставишь ноль? (1-9): ")
        while o not in nums:
            o = input("Поставишь ноль? (1-9): ")
        if o not in pool:
            print("Эта ячейка уже занята или недопустима. Попробуйте снова.")
            continue
        pool = pool.replace(o, 'o')
        nums = nums.replace(o, '')
        com1 += o
        print_pool(pool)
# Запуск игры
play_game()
