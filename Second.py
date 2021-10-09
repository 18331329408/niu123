import random
import time
randint = random.randint(1, 30)  # 随机产生的数字
while True:
    print(randint)
    num=input("请输入一个数字")
    if num.isdigit():
        num=int(num)
        if num == randint:
            print("OK")
            break
        elif num >randint:
            print("猜大了")
        elif num <randint:
            print("猜小了")
    else:
        print("别瞎输入")
        time.sleep(10)
