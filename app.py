import gzip
import json

from chalice import Chalice, Response

app = Chalice(app_name='ChaliceLearning')

app.debug=True

@app.route('/')
def index():
    return {'hello': 'world'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:

@app.route('/hello/{name}')
def hello_name(name):
   # '/hello/james' -> {"hello": "james"}
   return {'hello': name}

@app.route('/eco', methods=['POST'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return {'users': user_as_json}

# See the README documentation for more examples.
#


users={
    "1" : "pranavi",
    "2" : "raju",
    "3" : "lakshmi"
}
@app.route('/users/{id}')
def get_user(id):
    try :
        return {'name': users[id]}
    except KeyError:
        return {'error': 'user %s not found'.format(id) }


@app.route('/users')
def get_user():
    return users

@app.route('/introspect')
def get_request_info():
    return app.current_request.to_dict()

@app.route('/getMethod')
def get_Method():
    return app.current_request.method


#will give error as chalice serialise response to json by it is of diff class
@app.route('/getHeaders')
def get_Headers():
    return app.current_request.headers


@app.route('/RequestHeaders')
def get_requestHeaders():

    return Response(body="text response with text contentType",
                    status_code=200,
                    headers={"requestId": "kgjfghfxrytu6ygjh",
                             "Content-Type": "text/plain"})