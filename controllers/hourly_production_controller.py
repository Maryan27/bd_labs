from flask import Blueprint, request, jsonify
from services.hourly_production_service import HourlyProductionService
import logging

logging.basicConfig(level=logging.INFO)

def create_hourly_production_controller(mysql):
    hourly_production_controller = Blueprint('hourly_production', __name__)
    service = HourlyProductionService(mysql)

    @hourly_production_controller.route('/hourly_production', methods=['GET'])
    def get_hourly_productions():
        productions = service.get_hourly_productions()
        return jsonify({"status": "success", "data": [production.to_dict() for production in productions]}), 200

    @hourly_production_controller.route('/hourly_production', methods=['POST'])
    def create_hourly_production():
        data = request.json
        if not data or 'panel_id' not in data or 'timestamp' not in data or 'energy_produced' not in data:
            return jsonify({"status": "error", "message": "Invalid data"}), 400

        try:
            service.add_hourly_production(data)
            logging.info("Hourly production created successfully")
            return jsonify({"status": "success", "message": "Hourly production created"}), 201
        except Exception as e:
            logging.error(f"Error creating hourly production: {str(e)}")
            return jsonify({"status": "error", "message": str(e)}), 500

    @hourly_production_controller.route('/hourly_production/<int:production_id>', methods=['PUT'])
    def update_hourly_production(production_id):
        data = request.json
        if not data or 'panel_id' not in data or 'timestamp' not in data or 'energy_produced' not in data:
            return jsonify({"status": "error", "message": "Invalid data"}), 400

        try:
            service.modify_hourly_production(production_id, data)
            logging.info(f"Hourly production {production_id} updated successfully")
            return jsonify({"status": "success", "message": "Hourly production updated"}), 200
        except Exception as e:
            logging.error(f"Error updating hourly production {production_id}: {str(e)}")
            return jsonify({"status": "error", "message": str(e)}), 500

    @hourly_production_controller.route('/hourly_production/<int:production_id>', methods=['DELETE'])
    def delete_hourly_production(production_id):
        try:
            service.remove_hourly_production(production_id)
            logging.info(f"Hourly production {production_id} deleted successfully")
            return jsonify({"status": "success", "message": "Hourly production deleted"}), 200
        except Exception as e:
            logging.error(f"Error deleting hourly production {production_id}: {str(e)}")
            return jsonify({"status": "error", "message": str(e)}), 500

    return hourly_production_controller