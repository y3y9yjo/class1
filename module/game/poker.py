import random 
def poker():
    color_all = ["黑桃","紅心","方塊","梅花"]
    color = random.randint(0,3)
    num = random.randint(1,13)
    return color_all[color],num
