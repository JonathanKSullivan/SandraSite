from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app, db
from qualitaxas.model import DocumentType

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('typeName')


def abort_if_document_type_doesnt_exist(document_type_id):
    abort(404, message="DocumentType {} doesn't exist".format(document_type_id))


class DocumentTypeAPI(Resource):
    def get(self, document_type_id):
        document_type = DocumentType.query.get(document_type_id, None)
        if document_type:
            abort_if_document_type_doesnt_exist(document_type_id)
        return document_type.serialize
        

    def delete(self, document_type_id):
        document_type = DocumentType.query.get(document_type_id, None)
        if document_type:
            abort_if_document_type_doesnt_exist(document_type_id)
        db.session.delete(document_type)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)

        db.session.commit()
        return '', 204


    def put(self, document_type_id):
        document_type = DocumentType.query.get(document_type_id, None)
        if document_type:
            abort_if_document_type_doesnt_exist(document_type_id)
        args = parser.parse_args()
        document_type.type_name = args['type_name']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return document_type.serialize, 201

class DocumentTypeListAPI(Resource):
    def get(self):
        return [document_type.serialize for document_type in DocumentType.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        type_name = args['typeName']
        new_document_type =  DocumentType(type_name=type_name)
        # new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
        #                         new_correspondence = new_correspondence), 
        #                         user_id=user_id, timestamp=timestamp)
        # db.session.add(new_log)
        db.session.add(new_document_type)
        db.session.commit()
        return new_document_type.serialize, 201

api.add_resource(DocumentTypeListAPI, '/document_type_list')
api.add_resource(DocumentTypeAPI, '/document_type/<document_type_id>')