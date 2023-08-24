class katsuo(nigiri):
    top = "かつお"
    topping = "nege"
    price = 100

    def show_attribtes(self):
        super().show_attributes()
        print("topping: {}".format(self.topping))
