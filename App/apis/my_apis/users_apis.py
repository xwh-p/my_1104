from flask_restful import Resource


class UsersApi(Resource):

    def get(self):
        return {'code':200}