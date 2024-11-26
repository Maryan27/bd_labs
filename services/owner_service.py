from dao.owner_dao import OwnerDAO

class OwnerService:
    def __init__(self, mysql):
        self.dao = OwnerDAO(mysql)

    def get_owners(self):
        return self.dao.get_all_owners()

    def add_owner(self, owner):
        return self.dao.insert_owner(owner)

    def modify_owner(self, owner_id, owner):
        return self.dao.update_owner(owner_id, owner)

    def remove_owner(self, owner_id):
        return self.dao.delete_owner(owner_id)

    def get_owner_with_households(self, owner_id):
        return self.dao.get_owner_with_households(owner_id)

    
    def get_owner_stations(self, owner_id):
        return self.dao.get_owner_stations(owner_id)




