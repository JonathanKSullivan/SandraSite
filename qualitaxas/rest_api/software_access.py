from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('api_token')
parser.add_argument('secret_token')
parser.add_argument('software_id')
parser.add_argument('company_id')

def abort_if_software_access_doesnt_exist(software_access_id):
    abort(404, message="Software Access {} doesn't exist".format(software_access_id))


class SoftwareAccess(Resource):
    def get(self, software_access_id):
        software_access = SoftwareAccess.query.get(software_access_id, None)
        if software_access:
            abort_if_software_access_doesnt_exist(software_access_id)
        return software_access.serialize
        

    def delete(self, software_access_id):
        software_access = SoftwareAccess.query.get(software_access_id, None)
        if software_access:
            abort_if_software_access_doesnt_exist(software_access_id)
        db.session.delete(software_access)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, software_access_id):
        software_access = SoftwareAccess.query.get(software_access_id, None)
        if software_access:
            abort_if_software_access_doesnt_exist(software_access_id)
        args = parser.parse_args()
        software_access.api_token = args['api_token']
        software_access.secret_token = args['secret_token']
        software_access.software_id = args['software_id']
        software_access.company_id = args['company_id']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return software_access.serialize, 201

class SoftwareAccessList(Resource):
    def get(self):
        return [software_access.serialize for software_access in SoftwareAccess.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        api_token = args['api_token']
        secret_token = args['secret_token']
        software_id = args['software_id']
        company_id = args['company_id']
        new_software_access =  SoftwareAccess(api_token=api_token, 
                                              secret_token=secret_token,
                                              software_id=software_id, 
                                              company_id=company_id)
        new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_software_access)
        db.session.commit()
        return new_software_access.serialize, 201

api.add_resource(SoftwareAccessList, '/software_access_list')
api.add_resource(SoftwareAccess, '/software_access/<software_access_id>')