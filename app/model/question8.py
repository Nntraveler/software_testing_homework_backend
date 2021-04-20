from flask_restplus import fields

model = {
    'year': fields.Integer(required=True, description='年'),
    'month': fields.Integer(required=True, description='月'),
    'day': fields.Integer(required=True, description='日')
}

MODELS = []
