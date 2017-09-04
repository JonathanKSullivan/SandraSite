from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app
from qualitaxas.model import Testimonial, Log

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('headline')
parser.add_argument('content')
parser.add_argument('date')
parser.add_argument('user_id')

def abort_if_testimonial_doesnt_exist(testimonial_id):
    abort(404, message="Testimonial {} doesn't exist".format(testimonial_id))


class TestimonialAPI(Resource):
    def get(self, testimonial_id):
        testimonial = Testimonial.query.get(testimonial_id, None)
        if testimonial:
            abort_if_testimonial_doesnt_exist(testimonial_id)
        return testimonial.serialize
        

    def delete(self, testimonial_id):
        testimonial = Testimonial.query.get(testimonial_id, None)
        if testimonial:
            abort_if_testimonial_doesnt_exist(testimonial_id)
        db.session.delete(testimonial)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, testimonial_id):
        testimonial = Testimonial.query.get(testimonial_id, None)
        if testimonial:
            abort_if_testimonial_doesnt_exist(testimonial_id)
        args = parser.parse_args()
        testimonial.headline = args['headline']
        testimonial.content = args['content']
        testimonial.date = args['date']
        testimonial.user_id = args['user_id']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return testimonial.serialize, 201

class TestimonialListAPI(Resource):
    def get(self):
        return [testimonial.serialize for testimonial in Testimonial.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        headline = args['headline']
        content = args['content']
        user_id = args['user_id']
        date = datetime.now()
        new_testimonial =  Testimonial(headline=headline, content=content,
                               user_id=user_id, date=date)
        new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_testimonial)
        db.session.commit()
        return new_testimonial.serialize, 201

api.add_resource(TestimonialListAPI, '/testimonial_list')
api.add_resource(TestimonialAPI, '/testimonial/<testimonial_id>')