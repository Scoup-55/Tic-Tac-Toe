def play_game():
    pool = """------------
|_1_||_2_||_3_|
|_4_||_5_||_6_|
|_7_||_8_||_9_|"""
    def check_win(com):
        wins = [
            ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),
            ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),
            ('1', '5', '9'), ('3', '5', '7')
        ]
        for a, b, c in wins:
            if a in com and b in com and c in com:
                return True
        return False
    def rest(res):
        if res == 'да':
            play_game()
        else:
            print("Спасибо за игру!")
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
        if check_win(com):
            print("x победил!")
            break
        if len(nums) == 0:
            print("Ничья!")
            break
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
        if check_win(com1):
            print("0 победил!")
            break
        if len(nums) == 0:
            print("Ничья!")
            break
    # Спрашиваем, хотите ли играть снова
    rest(input("Хотите сыграть снова? (да/нет): "))
# Запуск игры
play_game()
