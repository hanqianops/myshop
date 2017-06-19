
class A:
    def __init__(self):
        self.cart = {"A":"aaa","B":"bbb"}

    def __iter__(self):
        for item in self.cart.values():
            yield item
    def __len__(self):
        return len(self.cart)

f = A()
for i in f:
    print(i)
