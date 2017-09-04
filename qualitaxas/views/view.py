from qualitaxas import app
from flask import request, make_response, render_template
from flask_oauthlib.client import OAuth
from qualitaxas import app




oauth = OAuth(app)

# google = oauth.remote_app(
#     'google',
#     consumer_key=app.config.get('GOOGLE_ID'),
#     consumer_secret=app.config.get('GOOGLE_SECRET'),
#     request_token_params={
#         'scope': 'email'
#     },
#     base_url='https://www.googleapis.com/oauth2/v1/',
#     request_token_url=None,
#     access_token_method='POST',
#     access_token_url='https://accounts.google.com/o/oauth2/token',
#     authorize_url='https://accounts.google.com/o/oauth2/auth',
# )

# linkedin = oauth.remote_app(
#     'linkedin',
#     consumer_key='k8fhkgkkqzub',
#     consumer_secret='ZZtLETQOQYNDjMrz',
#     request_token_params={
#         'scope': 'r_basicprofile',
#         'state': 'RandomString',
#     },
#     base_url='https://api.linkedin.com/v1/',
#     request_token_url=None,
#     access_token_method='POST',
#     access_token_url='https://www.linkedin.com/uas/oauth2/accessToken',
#     authorize_url='https://www.linkedin.com/uas/oauth2/authorization',
# )

# Front-End App
@app.route("/")
def home():
    """ Serves app view"""
    return make_response(render_template('index.html'), 200)

# @app.route('/login/google/')
# def g_login():
#     return google.authorize(callback=url_for('google_authorized', _external=True))

# @app.route('/login/linkedin/')
# def l_login():
#     return linkedin.authorize(callback=url_for('linkedin_authorized', _external=True))

# @app.route('/login/google/authorized')
# def google_authorized():
#     resp = google.authorized_response()
#     if resp is None:
#         return 'Access denied: reason=%s error=%s' % (
#             request.args['error_reason'],
#             request.args['error_description']
#         )
#     session['google_token'] = (resp['access_token'], '')
#     me = google.get('userinfo')
#     return jsonify({"data": me.data})

# @app.route('/login/linkedin/authorized')
# def linkedin_authorized():
#     resp = linkedin.authorized_response()
#     if resp is None:
#         return 'Access denied: reason=%s error=%s' % (
#             request.args['error_reason'],
#             request.args['error_description']
#         )
#     session['linkedin_token'] = (resp['access_token'], '')
#     me = linkedin.get('people/~')
#     return jsonify(me.data)

# @app.route('/logout/google')
# def g_logout():
#     session.pop('google_token', None)
#     return redirect(url_for('index'))

# @app.route('/logout/linkedin/')
# def l_logout():
#     session.pop('linkedin_token', None)
#     return redirect(url_for('index'))

# @linkedin.tokengetter
# def get_linkedin_oauth_token():
#     return session.get('linkedin_token')

# @google.tokengetter
# def get_google_oauth_token():
#     return session.get('google_token')

# def change_linkedin_query(uri, headers, body):
#     auth = headers.pop('Authorization')
#     headers['x-li-format'] = 'json'
#     if auth:
#         auth = auth.replace('Bearer', '').strip()
#         if '?' in uri:
#             uri += '&oauth2_access_token=' + auth
#         else:
#             uri += '?oauth2_access_token=' + auth
#     return uri, headers, body

# linkedin.pre_request = change_linkedin_query
