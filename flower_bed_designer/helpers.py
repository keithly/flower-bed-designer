from flask import json, Response


class ApiException(Exception):
    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_result(self):
        return Response(json.dumps({'message': self.message}),
                        status=self.status,
                        mimetype='application/json')


def validate_body(request_json):
    if not request_json:
        raise ApiException('expected json body', 400)


def register_api(bp, view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    bp.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', ])
    bp.add_url_rule(url, view_func=view_func, methods=['POST', ])
    bp.add_url_rule(f'{url}<{pk_type}:{pk}>', view_func=view_func, methods=['GET', 'PUT', 'DELETE'])
