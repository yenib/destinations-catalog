from itemCatalog import app
import os

currentModulePath = os.path.dirname(os.path.abspath(__file__))

try:
    with open(currentModulePath + '/../client_secret.json', 'r') as f:
        app.config['GOOGLE_CLIENT_SECRET'] = f.read()

    with open(currentModulePath + '/../fb_client_secret.json', 'r') as f:
        app.config['FACEBOOK_CLIENT_SECRET'] = f.read()
        
except IOError:
    print (("I/O error: Could not read files with client secrets "
           "for authentication with Google and Facebook."))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
