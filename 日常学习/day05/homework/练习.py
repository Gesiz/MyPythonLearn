def num(**kwargs):
    for key,value in kwargs.items():
        print("key:",key,"value:",value)
num(name="电脑", price=700)