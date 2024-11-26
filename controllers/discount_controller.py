from flask import Blueprint, request, jsonify
from services.discount_service import DiscountService

def create_discount_controller(mysql):
    discount_controller = Blueprint('discount', __name__, url_prefix='/discount')  

    service = DiscountService(mysql)

    @discount_controller.route('', methods=['GET'])  
    def get_discounts():
        discounts = service.get_discounts()
        return jsonify([discount.to_dict() for discount in discounts])

    @discount_controller.route('', methods=['POST'])  
    def create_discount():
        data = request.json
        if not data or 'discount_name' not in data or 'discount_value' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.add_discount(data)
            return jsonify({"message": "Discount created"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @discount_controller.route('/<int:discount_id>', methods=['PUT'])  
    def update_discount(discount_id):
        data = request.json
        if not data or 'discount_name' not in data or 'discount_value' not in data:
            return jsonify({"error": "Invalid data"}), 400

        try:
            service.modify_discount(discount_id, data)
            return jsonify({"message": "Discount updated"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @discount_controller.route('/<int:discount_id>', methods=['DELETE'])  
    def delete_discount(discount_id):
        try:
            service.remove_discount(discount_id)
            return jsonify({"message": "Discount deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return discount_controller


