from dao.dynamic_tables_dao import DynamicTablesDAO

class DynamicTablesService:
    def __init__(self, mysql):
        self.dao = DynamicTablesDAO(mysql)

    def run_procedure(self):
        return self.dao.execute_procedure()