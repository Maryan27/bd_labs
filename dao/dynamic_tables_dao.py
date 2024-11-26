class DynamicTablesDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def execute_procedure(self):
        cur = self.mysql.connection.cursor()
        try:
            
            cur.callproc('create_dynamic_tables_and_distribute_data')
            self.mysql.connection.commit()
            cur.close()
            return {"message": "Procedure executed successfully"}
        except Exception as e:
            cur.close()
            raise Exception(f"Error executing procedure: {str(e)}")