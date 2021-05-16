from flask_restful import Api

from App.apis.my_apis.users_apis import UsersApi

api1 = Api(prefix='/prefix/')

api1.add_resource(UsersApi,'user')