from flask_restplus import Namespace, Resource

from app.model.question1 import triangle_model as q1_model
from app.service.question1 import Question1

api = Namespace('question1', description='三角形问题')
q1_model = api.model('Triangle', model=q1_model)


@api.route('/triangle/<method_type>')  # NOQA
@api.param('method_type', 'boundary | equivalence')
@api.response(404, 'Method not found')
class Triangle(Resource):
    @api.doc('Triangle Problem')
    def get(self, method_type):
        """
        三角形问题
        """
        return Question1.triangle(method_type)


@api.route('/triangle/<method_type>/<code_version>')  # NOQA
@api.param('method_type', 'boundary | equivalence')
@api.param('code_version', 'v1 | v2')
@api.response(404, 'Method not found')
class Triangle(Resource):
    @api.doc('Triangle Problem')
    def get(self, method_type, code_version):
        """
        版本-三角形问题
        """
        return Question1.triangle(method_type, code_version)


@api.route('/triangle/')
class TriangleBasic(Resource):
    @api.doc('Triangle Problem Basic Method')
    @api.expect(q1_model)
    def post(self):
        """
        三角形问题的基础实现
        """
        return Question1.triangle_method_test(api.payload)


@api.route('/triangle/<code_version>')  # NOQA
@api.param('code_version', 'v1 | v2')
class TriangleBasic(Resource):
    @api.doc('Triangle Problem Basic Method')
    @api.expect(q1_model)
    def post(self, code_version):
        """
        版本-三角形问题的基础实现
        """
        return Question1.triangle_method_test(api.payload, code_version)
