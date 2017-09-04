import json, unittest,  random, string
from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from flask import request
from qualitaxas import app, db, s3
from qualitaxas.model import Company, Log
from datetime import datetime




api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('website')
parser.add_argument('email')
parser.add_argument('phone')
parser.add_argument('address1')
parser.add_argument('address2')
parser.add_argument('city')
parser.add_argument('state')
parser.add_argument('zip_code')
parser.add_argument('img_url')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 
    file = request.files['file']
    # if user does not select file, browser also
    # submit a empty part without filename
    if file.filename == '':
        return 
    if file and allowed_file(file.filename):
        bucket = 'mybucket'
        salt = ''.join([random.choice(string.letters) for i in range(50)])
        filename = secure_filename(file.filename)
        salted_filename = salt + filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], salted_filename))
        s3.Object(bucket, salted_filename).put(Body=open(app.config['UPLOAD_FOLDER'] + salted_filename, 'rb'))
        url = s3Client.generate_presigned_url('get_object', Params = {'Bucket': bucket, 'Key': salted_filename}, ExpiresIn = 100)
        return url

def abort_if_company_doesnt_exist(company_id):
    abort(404, message="Company {} doesn't exist".format(company_id))


class ActivateCompanyAPI(Resource):
    def post(self, company_id):
        company = Company.query.get(company_id)
        print company
        if not company:
            abort_if_company_doesnt_exist(company_id)
        company.active = not company.active
        db.session.commit()
        creation_date = datetime.now()
        # new_log = Log(activity="User {user} has deleted Company {company}".format(user = 0, 
        #                         company = company.name), user_id=None, timestamp=creation_date)
        # db.session.add(new_log)
        db.session.commit()
        return company.serialize, 201

class CompanyAPI(Resource):
    def get(self, company_id):
        company = Company.query.get(company_id)
        if not company:
            abort_if_company_doesnt_exist(company_id)
        return company.serialize

    def post(self, company_id):
        company = Company.query.get(company_id)
        if not company:
            abort_if_company_doesnt_exist(company_id)
        args = parser.parse_args()
        company.name = args['name']
        company.website = args['website']
        company.email = args['email']
        company.phone = args['phone']
        company.address = "{}|{}".format(args['address1'], args['address2'])
        company.city = args['city']
        company.state = args['state']
        company.img_url = args['img_url']
        if not company.img_url:
            img_file = args['logo_file']
            img_url = upload_file(img_file)
        company.zip_code = args['zip_code']
        company.active = True
        creation_date = datetime.now()
        # new_log = Log(activity="User {user} has changed Company {company}".format(user = 0, 
        #                         company = company.name), user_id=user_id, timestamp=creation_date)
        # db.session.add(new_log)
        db.session.commit()
        return company.serialize, 201


class CompanyListAPI(Resource):
    def get(self):
        data = [company.serialize for company in Company.query.all()]
        return data, 201

    def post(self):
        args = parser.parse_args()
        name = args['name']
        website = args['website']
        email = args['email']
        phone = args['phone']
        address1 = args['address1']
        address2 = args['address2']
        city = args['city']
        state = args['state']
        zip_code = args['zip_code']
        img_url = args['img_url']
        address = address1 + "|" + address2 if address2 else address1
        if not img_url:
            img_file = args['logo_file']
            img_url = upload_file(img_file)
        active = True
        creation_date = datetime.now()
        print args
        new_company =  Company(name=name, website=website, email=email, 
                               phone=phone, address=address, 
                               city=city, state=state, zip_code=zip_code,
                               active=active, img_url=img_url, 
                               creation_date=creation_date)
        # new_log = Log(activity="User {user} has created Company {company}".format(user = 0, 
        #                         company = new_company.name), user_id='0', timestamp=creation_date)
        db.session.add(new_company)
        # db.session.add(new_log)
        db.session.commit()
        return new_company.serialize, 201

api.add_resource(ActivateCompanyAPI, '/activate/company/<company_id>')
api.add_resource(CompanyAPI, '/company/<company_id>')
api.add_resource(CompanyListAPI, '/companyList')

class CompanyTestCase(unittest.TestCase):
    """Test for Company.py"""
        

if __name__ == '__main__':
    unittest.main()


    