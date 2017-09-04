from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from qualitaxas import app

db = SQLAlchemy()

class Company(db.Model):

    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    website = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(85), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(9), nullable=False)
    img_url = db.Column(db.String(), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '''Company(name=%r, website=%r, email=%r, phone=%r, address=%r, 
                           city=%r, state=%r, zip_code=%r, img_url=%r, active=%r, 
                           creation_date=%r)''' % (self.name, self.website, 
                                                   self.email, self.phone, 
                                                   self.address, self.city, 
                                                   self.state, self.zip_code, 
                                                   self.img_url, self.active,
                                                   self.creation_date)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'website': self.website,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'active': self.active,
            'zip_code': self.zip_code,
            # 'admin_id': self.admin_id,
            'img_url': self.img_url,            
            'creation_date': self.creation_date.strftime("%A %B %e, %Y - %I:%M:%S%p"),
        }

class Correspondence(db.Model):

    __tablename__ = 'correspondence'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(20), nullable = True)
    subject = db.Column(db.String(1000), nullable = False)
    message = db.Column(db.String(1000), nullable = False)
    inbox_sent = db.Column(db.String(5), nullable = False)
    date = db.Column(db.DateTime, nullable = False)

    def __repr__(self):
        return '''Correspondence(name=%r, email=%r, phone=%r, message=%r, 
                                   date=%r)''' % (self.name, self.email, 
                                                   self.phone, self.subject, 
                                                   self.message, self.date)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'subject': self.subject,
            'message': self.message,
            'inboxSent' : self.inbox_sent,
            'date': self.date.strftime("%A %B %e, %Y - %I:%M:%S%p"),
        }

class Document(db.Model):

    __tablename__ = 'document'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),  nullable=True)
    description = db.Column(db.String(250),  nullable=True)

    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'), 
                                 nullable= False)
    cover_photo = db.Column(db.String(250),  nullable=True)
    location = db.Column(db.String(250),  nullable=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), 
                           nullable= False)
    company = db.relationship('Company', backref='documents')
    document_type = db.relationship('DocumentType', backref='document')

class DocumentType(db.Model):

    __tablename__ = 'document_type'

    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(25),  nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'typeName': self.type_name,
        }

class Invoice(db.Model):

    __tablename__ = 'invoice'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250),  nullable=True)
    amount = db.Column(db.Float(precision=2), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), 
                           nullable= False)
    company = db.relationship('Company', backref='invoices')


    def __repr__(self):
        return '''Invoice(amount = %r, creation_date = %r, due_date = %r, 
                          company_id = %r)''' % (self.amount, 
                          self.creation_date, self.company_id)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'company_id': self.company_id,
            'amount': self.amount,
            'creation_date': self.creation_date,
            'due_date': self.due_date
        }


class Log(db.Model):

    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(250),  nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref='logs')
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '''Log(user_id = %r, company_id = %r, activity = %r, 
                    timestamp = %r)''' % (self.user_id, self.activity, 
                    self.timestamp)
                    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'user_id': self.user_id,
            'activity': self.activity,
        }

class Payment(db.Model):

    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(precision=2), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    company_id = db.Column(db.String, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('Company', backref='payments')

    def __repr__(self):
        return 'Payment(amount = %r, creation_date = %r, company_id = %r>' % \
                (self.amount, self.creation_date, self.company_id)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'company_id': self.company_id,
            'amount': self.amount,
            'creation_date': self.creation_date
        }

class SoftwareAccess(db.Model):
    
    __tablename__ = 'software_access'

    id = db.Column(db.Integer, primary_key=True)
    api_token =  db.Column(db.String(50),  nullable=False)
    secret_token =  db.Column(db.String(50),  nullable=False)
    software_id =  db.Column(db.Integer, db.ForeignKey('software.id'), nullable=False)
    company_id =  db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    software = db.relationship('Software', backref='software_access')
    company = db.relationship('Company', backref='software_access')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'api_token': self.api_token,
            'secret_token': self.secret_token,
            'software': self.software
        }

class Software(db.Model):
    
    __tablename__ = 'software'    

    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(20),  nullable=False)
    url =  db.Column(db.String(50),  nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url
        }

class Testimonial(db.Model):

    __tablename__ = 'testimonial'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    headline = db.Column(db.String(20),  nullable=False)
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user = db.relationship('User', backref='testimonials')

    def __repr__(self):
        return '''Testimonial(user_id = %r, headline = %r, content = %r, 
                              date = %r)''' % (self.user_id, self.headline, 
                                               self.content, self.date)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'headline': self.headline,
            'content': self.content,
            'date': self.date
        }

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(120), nullable=False)
    picture = db.Column(db.String(200), nullable=True)
    role = db.Column(db.String(80), nullable= True)
    phone = db.Column(db.String(20), nullable=True)
    active = db.Column(db.Boolean, nullable=False)
    company_admin = db.Column(db.Boolean, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
    company = db.relationship('Company', backref='users')

    @staticmethod
    def hash_password(self, password):
        return pwd_context.encrypt(password)

    @staticmethod
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return '''User(name=%r, email=%r, email=%r, phone=%r, address=%r, 
                      city=%r, state=%r, zip_code=%r, active=%r, 
                      creation_date=%r)''' % (self.username, self.email, 
                      self.website, self.email, self.phone, self.address, 
                      self.city, self.state, self.zip_code, self.active, 
                      self.creation_date)
    
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'company_id': self.company_id,
            'role': self.role,
            'phone': self.phone,
            'creation_date': self.creation_date.strftime("%A %B %e, %Y - %I:%M:%S%p"),
            'active': self.active
        }

if __name__ == "__main__":
    app.config.from_object('qualitaxas.config.DevelopmentConfig')
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()