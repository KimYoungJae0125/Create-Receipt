
class Money:
    title = ""
    description = ""
    amount = 0

    def __init__(self):
        pass

    def __init__(self, title, description, amount):
        self.title = title
        self.description = description
        self.amount = amount

    def get(self):
        return {
            "title" : self.title,
            "description" : self.description,
            "amount" : self.amount,
        }

