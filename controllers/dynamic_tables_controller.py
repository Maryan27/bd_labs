from flask import Blueprint, jsonify
from services.dynamic_tables_service import DynamicTablesService

def create_dynamic_tables_controller(mysql):
    dynamic_tables_controller = Blueprint('dynamic_tables', __name__)
    service = DynamicTablesService(mysql)

    @dynamic_tables_controller.route('/execute_procedure', methods=['GET'])
    def execute_procedure():
        try:
            result = service.run_procedure()
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return dynamic_tables_controller