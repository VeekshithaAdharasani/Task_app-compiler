from fastapi import FastAPI

app = FastAPI()

@app.get('/api/user')
def get_users():
    return {'message': 'generated'}

@app.post('/api/user')
def create_user():
    return {'message': 'generated'}

@app.put('/api/user/{id}')
def update_user():
    return {'message': 'generated'}

@app.delete('/api/user/{id}')
def delete_user():
    return {'message': 'generated'}

@app.get('/api/contact')
def get_api_contact():
    return {'message': 'generated'}

@app.post('/api/contact')
def post_api_contact():
    return {'message': 'generated'}

@app.put('/api/contact/{id}')
def put_api_contact_id():
    return {'message': 'generated'}

@app.delete('/api/contact/{id}')
def delete_api_contact_id():
    return {'message': 'generated'}

@app.get('/api/subscription')
def get_api_subscription():
    return {'message': 'generated'}

@app.post('/api/subscription')
def post_api_subscription():
    return {'message': 'generated'}

@app.put('/api/subscription/{id}')
def put_api_subscription_id():
    return {'message': 'generated'}

@app.delete('/api/subscription/{id}')
def delete_api_subscription_id():
    return {'message': 'generated'}
