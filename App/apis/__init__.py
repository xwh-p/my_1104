from App.apis.my_apis import api1


def init(app):
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))


def init_api(app):

    api1.init_app(app)