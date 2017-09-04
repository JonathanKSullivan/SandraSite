from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('url')

def abort_if_software_doesnt_exist(software_id):
    abort(404, message="Software {} doesn't exist".format(software_id))


class SoftwareAPI(Resource):
    def get(self, software_id):
        software = Software.query.get(software_id, None)
        if software:
            abort_if_software_doesnt_exist(software_id)
        return software.serialize
        

    def delete(self, software_id):
        software = Software.query.get(software_id, None)
        if software:
            abort_if_software_doesnt_exist(software_id)
        db.session.delete(software)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, software_id):
        software = Software.query.get(software_id, None)
        if software:
            abort_if_software_doesnt_exist(software_id)
        args = parser.parse_args()
        software.name = args['name']
        software.url = args['url']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return software.serialize, 201

class SoftwareListAPI(Resource):
    def get(self):
        return [software.serialize for software in Software.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        name = args['name']
        url = args['url']
        new_software =  Software(name=name, url=url)
        new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_software)
        db.session.commit()
        return new_software.serialize, 201

api.add_resource(SoftwareListAPI, '/software_list')
api.add_resource(SoftwareAPI, '/software/<software_id>')