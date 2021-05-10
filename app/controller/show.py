from flask_restplus import Namespace, Resource

from app.model.show import model
from app.service.show import ShowCSV

api = Namespace('show_csv', description='csv展示')
model = api.model('Show', model=model)


@api.route('/csv/<problem_num>/<method_type>')  # NOQA
@api.param('problem_num', 'triangle...')
@api.param('method_type', 'boundary | equivalence | decision | final')
@api.response(404, 'Method not found')
class CsvGetter(Resource):

    @api.doc('Display CSV Table')
    def get(self, problem_num, method_type):
        """
        展示CSV表格
        """
        return ShowCSV.get_csv(problem_num, method_type)


@api.route('/')
class CalenderBasic(Resource):

    @api.doc('Get Problem Item')
    def get(self):
        """
        获得问题项目
        """
        return ShowCSV.get_csv_dir()
