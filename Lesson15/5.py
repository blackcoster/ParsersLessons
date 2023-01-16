class Test(str):
    def __init__(self,word):
        super().__init__()
    def __len__(self):
        return 25
a = Test('Hello')
print(len(a))