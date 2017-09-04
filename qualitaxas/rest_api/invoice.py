from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('amount')
parser.add_argument('creation_date')
parser.add_argument('due_date')
parser.add_argument('company_id')

def abort_if_invoice_doesnt_exist(invoice_id):
    abort(404, message="Invoice {} doesn't exist".format(invoice_id))

    
class InvoiceAPI(Resource):
    def get(self, invoice_id):
        invoice = Invoice.query.get(invoice_id, None)
        if invoice:
            abort_if_invoice_doesnt_exist(invoice_id)
        return invoice.serialize
        

    def delete(self, invoice_id):
        invoice = Invoice.query.get(invoice_id, None)
        if invoice:
            abort_if_invoice_doesnt_exist(invoice_id)
        db.session.delete(invoice)
        new_log = Log(activity="User {user} has deleted Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return '', 204


    def put(self, invoice_id):
        invoice = Invoice.query.get(invoice_id, None)
        if invoice:
            abort_if_invoice_doesnt_exist(invoice_id)
        args = parser.parse_args()
        invoice.amount = args['amount']
        invoice.company_id = args['company_id']
        invoice.due_date = args['due_date']
        new_log = Log(activity="User {user} has changed Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.commit()
        return invoice.serialize, 201

class InvoiceListAPI(Resource):
    def get(self):
        return [invoice.serialize for invoice in Invoice.query.all()] , 201

    def post(self):
        args = parser.parse_args()
        amount = args['amount']
        company_id = args['company_id']
        due_date = args['due_date']
        creation_date = datetime.now()
        new_invoice =  Invoice(amount=name, company_id=company_id, 
                               due_date=due_date, creation_date=creation_date)
        new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
                                new_correspondence = new_correspondence), 
                                user_id=user_id, timestamp=timestamp)
        db.session.add(new_log)
        db.session.add(new_invoice)
        db.session.commit()
        return new_invoice.serialize, 201

api.add_resource(InvoiceListAPI, '/invoice_list')
api.add_resource(InvoiceAPI, '/invoice/<invoice_id>')

