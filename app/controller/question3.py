from flask_restplus import Namespace, Resource

from app.model.question3 import model
from app.service.question3 import Question3

api = Namespace('question3', description='佣金问题')
model = api.model('Commission', model=model)


@api.route('/commission/<method_type>')  # NOQA
@api.param('method_type', 'boundary-input | boundary-output')
@api.response(404, 'Method not found')
class Commission(Resource):
    @api.doc('Commission Problem')
    def get(self, method_type):
        """
        佣金问题
        """
        return Question3.commission(method_type)


@api.route('/commission/<method_type>/<code_version>')  # NOQA
@api.param('method_type', 'boundary-input | boundary-output')
@api.param('code_version', 'v1 | v2')
@api.response(404, 'Method not found')
class Commission(Resource):
    @api.doc('Commission Problem')
    def get(self, method_type, code_version):
        """
        版本-三角形问题
        """
        return Question3.commission(method_type, code_version)


@api.route('/commission/')
class CommissionBasic(Resource):
    @api.doc('Commission Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        佣金问题的基础实现
        """
        return Question3.commission_method_test(api.payload)
