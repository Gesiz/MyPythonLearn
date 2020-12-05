class InputNotNumber(ValueError):
    def __init__(self, num):
        super(InputNotNumber, self).__init__()
        self.num = num

    def __str__(self):
        return f"您输入的值为{self.num}并不是整形数据"


while True:
    num = input("请输入代转换的数字")
    try:
        int(num)
    except Exception as e:
        # raise ValueError from None
        print(e)

    else:
        break
