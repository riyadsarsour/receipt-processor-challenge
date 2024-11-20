from flask import Blueprint, request, jsonify
from .process_pts import get_receipt_points
import uuid

bp = Blueprint('main', __name__)

receipts = {}


@bp.route('/receipts/process', methods=['POST'])
def process_receipts():
    receipt = request.json
    if receipt is None:
        return jsonify({"error": "The receipt is invalid"}), 400

    receipt_id = str(uuid.uuid4())
    receipts[receipt_id] = receipt

    return jsonify({"id": receipt_id}), 200

@bp.route('/receipts/<string:id>/points', methods=['GET'])
def get_points(id):
    if id not in receipts:
        return jsonify({"error": "No receipt found for that id"}), 404
    points = get_receipt_points(receipts[id])
    return jsonify({"points": points}), 200