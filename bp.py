

# flask蓝图，设立两个蓝图分别为chatpdf和caj2pdf




from flask import Blueprint


chatpdf = Blueprint('chatpdf', __name__, url_prefix='/chatpdf')
caj2pdf = Blueprint('caj2pdf', __name__, url_prefix='/caj2pdf')

from chatpdf import cp_controller

def init_bp(app):
    app.register_blueprint(chatpdf)
    app.register_blueprint(caj2pdf)