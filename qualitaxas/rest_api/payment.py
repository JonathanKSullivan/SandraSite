from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('amount')
parser.add_argument('company_id')

def abort_if_payment_doesnt_exist(payment_id):
    abort(404, message="Payment {} doesn't exist".format(payment_id))


class PaymentAPI(Resource):
    def get(self, payment_id):
        payment = Payment.query.get(payment_id, None)
        if payment:
            abort_if_payment_doesnt_exist(payment_id)
        return payment.serialize
        

    def delete(self, payment_id):
        payment = Payment.query.get(payment_id, None)
        if payment:
            abort_if_payment_doesnt_exist(payment_id)
        db.session.delete(payment)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, payment_id):
        payment = Payment.query.get(payment_id, None)
        if payment:
            abort_if_payment_doesnt_exist(payment_id)
        args = parser.parse_args()
        payment.amount = args['amount']
        payment.company_id = args['company_id']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return payment.serialize, 201

class PaymentListAPI(Resource):
    def get(self):
        return [payment.serialize for payment in Payment.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        amount = args['amount']
        company_id = args['company_id']
        creation_date = datetime.now()
        new_payment =  Payment(amount=amount, company_id=company_id,
                               creation_date=creation_date)
        new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_payment)
        db.session.commit()
        return new_payment.serialize, 201

api.add_resource(PaymentListAPI, '/payment_list')
api.add_resource(PaymentAPI, '/payment/<payment_id>')