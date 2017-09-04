from flask_restful import reqparse, abort, Api, Resource
from flask_oauthlib.client import OAuth
from qualitaxas import app

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('password_hash')
parser.add_argument('picture')
parser.add_argument('role')
parser.add_argument('phone')
parser.add_argument('company_admin')
parser.add_argument('company_id')

def abort_if_user_doesnt_exist(user_id):
        abort(404, message="User {} doesn't exist".format(user_id))

class UserAPI(Resource):
    def get(self, user_id):
        user = User.query.get(user_id, None)
        if user:
            abort_if_user_doesnt_exist(user_id)
        return user.serialize
        

    def delete(self, user_id):
        user = User.query.get(user_id, None)
        if user:
            abort_if_user_doesnt_exist(user_id)
        db.session.delete(user)
        new_log = Log(activity="User {user} has deleted Correspondence {user}".format(user = user), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, user_id):
        user = User.query.get(user_id, None)
        if user:
            abort_if_user_doesnt_exist(user_id)
        args = parser.parse_args()
        user.name = args['name']
        user.email = args['email']
        user.password_hash = User.hash_password(args['password'])
        user.picture = args['picture']
        user.role = args['role']
        user.phone = args['phone']
        user.company_admin = args['company_admin']
        user.company_id = args['company_id']
        new_log = Log(activity="User {user} has changed Correspondence {user}".format(user = user), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return user.serialize, 201

class UserListAPI(Resource):
    def get(self):
        return [user.serialize for user in User.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        name = args['name']
        email = args['email']
        password_hash = User.hash_password(args['password'])
        picture = args['picture']
        role = args['role']
        phone = args['phone']
        company_admin = args['company_admin']
        company_id = args['company_id']
        active = True
        date = datetime.now()
        new_user =  User(name = name, email = email, 
                         password_hash = password_hash, picture = picture, 
                         role = role, phone = phone, company_id = company_id, 
                         active = active, date = date)
        new_log = Log(activity="User {user} has created Correspondence {user}".format(user = user, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_user)
        db.session.commit()
        return new_user.serialize, 201

api.add_resource(UserListAPI, '/user_list')
api.add_resource(UserAPI, '/user/<user_id>')


















