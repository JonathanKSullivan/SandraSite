from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('document_type_id')
parser.add_argument('location')

def abort_if_document_doesnt_exist(document_id):
    abort(404, message="Document {} doesn't exist".format(document_id))


class DocumentAPI(Resource):
    def get(self, document_id):
        document = Document.query.get(document_id, None)
        if document:
            abort_if_document_doesnt_exist(document_id)
        return document.serialize
        

    def delete(self, document_id):
        document = Document.query.get(document_id, None)
        if document:
            abort_if_document_doesnt_exist(document_id)
        db.session.delete(document)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, document_id):
        document = Document.query.get(document_id, None)
        if document:
            abort_if_document_doesnt_exist(document_id)
        args = parser.parse_args()
        document.document_type_id = args['document_type_id']
        document.location = args['location']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return document.serialize, 201

class DocumentListAPI(Resource):
    def get(self):
        return [document.serialize for document in Document.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        document_type_id = args['document_type_id']
        location = args['location']
        new_document =  Document(type_name=type_name, location=location,
                                 document_type_id=document_type_id)
        new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_document)
        db.session.commit()
        return new_document.serialize, 201

api.add_resource(DocumentListAPI, '/document_list')
api.add_resource(DocumentAPI, '/document/<document_id>')