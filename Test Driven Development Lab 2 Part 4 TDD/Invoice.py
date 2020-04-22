class Invoice:
    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items["qnt"] = qnt
        self.items["unit_price"] = price
        self.items["discount"] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v["unit_price"]) * int(v["qnt"])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v["qnt"]) * float(v["unit_price"])) * float(v["discount"]) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

    # TODO: Sam and Jinquan: Implement CheckInStock Function
    def checkInStock(self, products, item):
        for i, v in products.items():
            if i == item:
                if v['qnt'] > 0:
                    print("Product In Stock")
                    return True
                else:
                    print("Product Out Of Stock")
                    return False
        else:
            print("Product not found")
            return False

    # TODO: Ed and Tommy: Implement RemoveItem Function
    def removeItem(self, products, item):
        modifiedProducts = {i: v for i, v in products.items()}
        modifiedProducts.pop(item)
        return modifiedProducts
