from flask_restful import reqparse, abort, Api, Resource
from qualitaxas import app, db, mail
from qualitaxas.model import Correspondence, Log
from datetime import datetime
from flask_mail import Message
from flask import render_template

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('phone')
parser.add_argument('subject')
parser.add_argument('message')
parser.add_argument('inboxSent')

default_sender = app.config.get('MAIL_DEFAULT_SENDER')

def sort_email_by_date(emails):
  results = sorted(emails, key=lambda k: k['date'])
  return results

def get_unique_email(emails):
  contacts = []
  results = []
  for email in emails:
    if email['email'] not in contacts and email['inboxSent'] == 'inbox':
      contacts.append(email['email'])
      results.append(email)
  print results
  return results

def make_message(recipients, subject, body, html, cc = None, bcc = None, 
                 attachments = None, reply_to = default_sender, 
                 date = datetime.now()):
    msg = Message()
    msg.subject = subject
    msg.recipients = recipients
    msg.body = body
    msg.html = html
    msg.cc = cc
    msg.bcc = bcc
    msg.attachments = attachments
    msg.reply_to = reply_to
    msg.date = date
    return msg

def send_message(message):  
    mail.send(message)

def abort_if_correspondence_doesnt_exist(email_id):
    abort(404, message="Correspondence for {} doesn't exist".format(email_id))

class CorrespondenceAPI(Resource):
    def get(self, email_id):
        correspondences = Correspondence.query.filter_by(email = email_id).all()
        if not correspondences:
            abort_if_correspondence_doesnt_exist(email_id)
        return sort_email_by_date([correspondence.serialize for correspondence in correspondences]), 201

class CorrespondenceListAPI(Resource):
    def get(self):
        return get_unique_email(sorted([correspondence.serialize for correspondence in Correspondence.query.all()], reverse=True)) , 201

    def post(self):
        args = parser.parse_args()
        name = args['name']
        email = args['email']
        phone = args['phone']
        subject = args['subject']
        message = args['message']
        inbox_sent = args['inboxSent']
        date = datetime.now()
        new_correspondence =  Correspondence(name=name, email=email, 
                                             phone=phone, subject=subject,
                                             message=message, 
                                             inbox_sent = inbox_sent, date=date)

        print "0"

        email_data = {'name': name,
                      'email':email,
                      'phone': phone,
                      'subject': subject,
                      'message': message,
                      'date': date
                      }
        
        if inbox_sent == 'inbox':
            print "inbox"
            body = render_template('email/received_correspondence.txt',
                                    email_data = email_data)
            html = render_template('email/received_correspondence.html', 
                                    email_data = email_data) 
            message = make_message(recipients = [default_sender], 
                                   subject = "Qualitaxas.com: {}".format(subject), 
                                   body = body, html = html, 
                                   cc = [email],
                                   bcc = [default_sender])
        if inbox_sent == 'sent':
            print "sent"
            body = render_template('email/sent_correspondence.txt',
                                    email_data = email_data)
            html = render_template('email/sent_correspondence.html', 
                                    email_data = email_data) 
            message = make_message(recipients = [email], 
                                   subject = "Qualitaxas.com: {}".format(subject), 
                                   body = body, html = html, 
                                   bcc = [default_sender])
        
        # new_log = Log(activity="User {user} has created Correspondence {new_correspondence}".format(user = 0, 
        #                         new_correspondence = new_correspondence), 
        #                         user_id=user_id, timestamp=timestamp)
        # db.session.add(new_log)
        db.session.add(new_correspondence)
        db.session.commit()
        # send_message(message)
        return new_correspondence.serialize, 201

api.add_resource(CorrespondenceListAPI, '/correspondence_list')
api.add_resource(CorrespondenceAPI, '/correspondence/<email_id>')

