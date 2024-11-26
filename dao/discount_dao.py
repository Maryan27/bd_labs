from models.discount import Discount

class DiscountDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_discounts(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM discounts")
        discounts = cur.fetchall()
        cur.close()
        return [Discount(id=row[0], discount_name=row[1], discount_value=row[2]) for row in discounts]

    def insert_discount(self, discount):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO discounts (discount_name, discount_value) VALUES (%s, %s)", 
                    (discount['discount_name'], discount['discount_value']))
        self.mysql.connection.commit()
        cur.close()

    def update_discount(self, discount_id, discount):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE discounts SET discount_name = %s, discount_value = %s WHERE id = %s", 
                    (discount['discount_name'], discount['discount_value'], discount_id))
        self.mysql.connection.commit()
        cur.close()

    def delete_discount(self, discount_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM discounts WHERE id = %s", (discount_id,))
        self.mysql.connection.commit()
        cur.close()
