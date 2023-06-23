import random

money=10000

for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}的绩效分为{score}, 下一位")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}工资为1000, 余额{money}")
    else:
        print("余额不足")

