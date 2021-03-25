from flask_restplus import Namespace, Resource

from app.model.question2 import model
from app.service.question2 import Question2

api = Namespace('question2', description='佣金问题')
model = api.model('Commission', model=model)


@api.route('/commission/<method_type>')  # NOQA
@api.param('method_type', 'boundary-input | boundary-output')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Commission Problem')
    def get(self, method_type):
        """
        佣金问题
        """
        return Question2.commission(method_type)


@api.route('/commission/')
class CalenderBasic(Resource):
    @api.doc('Commission Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        佣金问题的基础实现
        """
        return Question2.commission_method_test(api.payload)
