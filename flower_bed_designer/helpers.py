from flask import Flask, json, Response


class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResult):
            return rv.to_response()
        return Flask.make_response(self, rv)


class ApiResult:
    def __init__(self, value, status=200):
        self.value = value
        self.status = status

    def to_response(self):
        return Response(
            json.dumps(self.value),
            status=self.status,
            mimetype='application/json',
            headers={'Access-Control-Allow-Origin': '*'}
        )


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return ApiResult(
            {'message': self.message},
            status=self.status
        )


def register_api(bp, view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    bp.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', 'OPTIONS'])
    bp.add_url_rule(url, view_func=view_func, methods=['POST', 'OPTIONS'])
    bp.add_url_rule(f'{url}<{pk_type}:{pk}>', view_func=view_func, methods=['GET', 'PUT', 'DELETE', 'OPTIONS'])
