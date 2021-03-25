from flask_restplus import Namespace, Resource

from app.model.question6 import model
from app.service.question6 import Question6 as question6Service

api = Namespace('question6', description='打印机问题')
model = api.model('Printer', model=model)


@api.route('/printer/<method_type>')  # NOQA
@api.param('method_type', 'printer | printer-robust')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Printer Problem')
    def get(self, method_type):
        """
        打印机问题
        """
        return question6Service.printer(method_type)


@api.route('/printer/')
class CalenderBasic(Resource):
    @api.doc('Printer Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        打印机问题问题的基础实现
        """
        return question6Service.printer_method_test(api.payload)
