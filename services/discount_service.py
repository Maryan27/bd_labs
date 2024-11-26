from dao.discount_dao import DiscountDAO

class DiscountService:
    def __init__(self, mysql):
        self.dao = DiscountDAO(mysql)

    def get_discounts(self):
        return self.dao.get_all_discounts()

    def add_discount(self, discount):
        return self.dao.insert_discount(discount)

    def modify_discount(self, discount_id, discount):
        return self.dao.update_discount(discount_id, discount)

    def remove_discount(self, discount_id):
        return self.dao.delete_discount(discount_id)
