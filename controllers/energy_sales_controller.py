from flask import Blueprint, request, jsonify
from services.energy_sales_service import EnergySalesService

def create_energy_sales_controller(mysql):
    energy_sales_controller = Blueprint('energy_sales', __name__, url_prefix='/energy_sales')
    service = EnergySalesService(mysql)

    @energy_sales_controller.route('', methods=['GET'])
    def get_energy_sales():
        try:
            sales = service.get_energy_sales()
            return jsonify([sale.to_dict() for sale in sales]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @energy_sales_controller.route('', methods=['POST'])
    def create_energy_sales():
        data = request.json
        required_fields = ['station_id', 'energy_sold', 'price_per_kWh', 'timestamp']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        try:
            service.add_energy_sales(data)
            return jsonify({"message": "Energy sale created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @energy_sales_controller.route('/<int:sale_id>', methods=['PUT'])
    def update_energy_sales(sale_id):
        data = request.json
        try:
            service.modify_energy_sales(sale_id, data)
            return jsonify({"message": "Energy sale updated"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @energy_sales_controller.route('/<int:sale_id>', methods=['DELETE'])
    def delete_energy_sales(sale_id):
        try:
            service.remove_energy_sales(sale_id)
            return jsonify({"message": "Energy sale deleted"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return energy_sales_controller
