from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('activity')
parser.add_argument('user_id')
parser.add_argument('user')
parser.add_argument('timestamp')

def abort_if_log_doesnt_exist(log_id):
    abort(404, message="Log {} doesn't exist".format(log_id))


class LogAPI(Resource):
    def get(self, log_id):
        log = Log.query.get(log_id, None)
        if log:
            abort_if_log_doesnt_exist(log_id)
        return log.serialize
        

class LogListAPI(Resource):
    def get(self):
        return [log.serialize for log in Log.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        activity = args['activity']
        user_id = args['user_id']
        timestamp = datetime.now()
        new_log =  Log(activity=activity, user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return new_log.serialize, 201
        
api.add_resource(LogListAPI, '/log')
api.add_resource(LogAPI, '/log_list/<log_id>')