from flask_restplus import Namespace, Resource

from app.model.question6 import model
from app.service.question6 import Question6

api = Namespace('question6', description='电信收费问题')
model = api.model('Commission', model=model)


@api.route('/charge/<method_type>')  # NOQA
@api.param('method_type', 'boundary | equivalence | decision | final')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Charge Problem')
    def get(self, method_type):
        """
        电信收费问题
        """
        return Question6.charge(method_type)


@api.route('/charge/')
class CalenderBasic(Resource):
    @api.doc('Charge Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        电信收费问题的基础实现
        """
        return Question6.charge_method_test(api.payload)


@api.route('/charge/<code_version>')  # NOQA
@api.param('code_version', 'v1 | v2')
class CalenderBasic(Resource):
    @api.doc('Charge Problem Basic Method')
    @api.expect(model)
    def post(self, code_version):
        """
        版本-电信收费问题的基础实现
        """
        return Question6.charge_method_test(api.payload, code_version)


@api.route('/charge/<method_type>/<code_version>')  # NOQA
@api.param('method_type', 'boundary | equivalence | decision')
@api.param('code_version', 'v1 | v2')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Charge Problem')
    def get(self, method_type, code_version):
        """
        版本-电信收费问题
        """
        return Question6.charge(method_type, code_version)
