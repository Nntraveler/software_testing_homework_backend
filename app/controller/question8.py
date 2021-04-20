from flask_restplus import Namespace, Resource

from app.model.question8 import model
from app.service.question8 import Question8 as question8Service

api = Namespace('question8', description='万年历问题')
model = api.model('Calender', model)


@api.route('/calendar/<method_type>')  # NOQA
@api.param('method_type',
           'boundary | equivalence-weak-general ｜ equivalence-strong-general ｜ equivalence-weak-robust ｜ '
           'equivalence-strong-robust')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Calendar Problem')
    def get(self, method_type):
        """
        万年历问题
        """
        return question8Service.calendar(method_type)


@api.route('/calendar/')
class CalenderBasic(Resource):
    @api.doc('Calender Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        万年历问题的基础实现
        """
        return question8Service.calendar_method_test(api.payload)
