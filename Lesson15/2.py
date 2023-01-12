class Test(list):
    def append(self, object):
        for i in range(len(self)):
            self[i] **= object

a = Test([1, 2, 3])
print(a)
a.append(2)
print(a)

