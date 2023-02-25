
class Receipt:
    amount = 0
    store = ""
    content = ""
    price = 0

    def __init__(self):
        pass

    def __init__(self, amount, store, content, price):
        self.amount = amount
        self.store = store
        self.content = content
        self.price = price

    def get(self):
        return {
            "amount" : self.amount,
            "store" : self.store,
            "content" : self.content,
            "price" : self.price,
        }