from flask import Blueprint, request

main_bp = Blueprint('general', __name__)


@main_bp.route('/hello', methods=['GET'])
def index():
    name = request.args.get('hello', 'World')
    return f"Hello {name}", 200
