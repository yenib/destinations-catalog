from itemCatalog import app
from itemCatalog.utils import getAntiForgeryToken, createOrSignInUser

from flask import make_response, session, request, jsonify

import httplib2
import json
from googleapiclient.discovery import build
from oauth2client.client import (credentials_from_clientsecrets_and_code,
                                FlowExchangeError)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # If this request does not have `X-Requested-With` header or the
    # anti-forgery state token is not the expected one this could be a CSRF
    if not request.is_xhr or request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid request.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    authCode = request.data
    
    try:        
        # Exchange auth code for access token, refresh token, and ID token
        credentials = credentials_from_clientsecrets_and_code(
            filename = app.config['GOOGLE_CLIENT_SECRET_FILE'],
            scope = ['profile', 'email'],
            code = authCode)
        
    except FlowExchangeError as e:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    del session['state']
    session['credentials'] = credentials.to_json()

    # Call Google+ API to get user's profile info
    httpAuth = credentials.authorize(httplib2.Http())
    gplusService = build('plus', 'v1', http=httpAuth)
    userInfo = gplusService.people().get(userId='me').execute()

    user = createOrSignInUser(email = credentials.id_token["email"],
                              name = userInfo["name"]["givenName"],
                              lastName = userInfo["name"]["familyName"],
                              picture = userInfo["image"]["url"])

    resp = {'status': 'success',
            'userName': "{} {}".format(user.name, user.last_name),
            'userPicture': user.picture
            }
                          
    return jsonify(resp)



@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    # If this request does not have `X-Requested-With` header or the
    # anti-forgery state token is not the expected one this could be a CSRF.
    if not request.is_xhr or request.args.get('state') != session['state']:
        response = make_response(json.dumps('Invalid request.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    accessToken = request.data

    appInfo = json.loads(open(app.config['FACEBOOK_CLIENT_SECRET_FILE'],
                             'r').read())

    # Exchange the short-lived token for a long-lived token.    
    url = ("https://graph.facebook.com/v2.9/oauth/access_token?"
           "grant_type=fb_exchange_token"
           "&client_id=%s"
           "&client_secret=%s"
           "&fb_exchange_token=%s") % (appInfo['web']['app_id'],
                                      appInfo['web']['app_secret'],
                                      accessToken)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error').get("message")),
                                 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Use long-lived token to get user info from API
    url = ("https://graph.facebook.com/v2.9/me?fields=id,first_name,"
           "last_name,email&access_token=%s") % result["access_token"]
    h = httplib2.Http()
    userInfo = json.loads(h.request(url, 'GET')[1])
    
    # Get user picture
    url = ("https://graph.facebook.com/v2.9/me/picture?height=200&width=200"
           "&redirect=0&access_token=%s") % result["access_token"]
    h = httplib2.Http()
    userPicture = json.loads(h.request(url, 'GET')[1])
    
    session['fb_credentials'] = {}
    session['fb_credentials']['access_token'] = result["access_token"]
    session['fb_credentials']['user_id'] = userInfo['id']

    del session['state']

    user = createOrSignInUser(email = userInfo["email"],
                              name = userInfo["first_name"],
                              lastName = userInfo["last_name"],
                              picture = userPicture["data"]["url"])

    resp = {'status': 'success',
            'userName': "{} {}".format(user.name, user.last_name),
            'userPicture': user.picture
            }
                          
    return jsonify(resp)
