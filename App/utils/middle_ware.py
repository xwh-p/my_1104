from flask import request, session, jsonify, g


def load_middleware(app):

    @app.before_request
    def before_request():
        path = request.full_path
        method= request.method
        print(path,'中间件')
        token = request.cookies.get('token')

        check_path = request.path
        path_list = ['/aaa/']
        for p in path_list:
            if p == check_path:
                break

        else:
            if token not in session:
                return jsonify({"code":400})

            # u = Users.query.get(session.get(token))
            # g.user = u