class Discount:
    def __init__(self, id, discount_name, discount_value):
        self.id = id
        self.discount_name = discount_name
        self.discount_value = discount_value

    def to_dict(self):
        return {
            "id": self.id,
            "discount_name": self.discount_name,
            "discount_value": str(self.discount_value)
        }
