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

