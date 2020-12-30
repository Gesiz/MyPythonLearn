from django.utils.deprecation import MiddlewareMixin


# MiddlewareMixin

class BookMiddlewareMixin(MiddlewareMixin):
    # 每次请求前都会调用
    def process_request(self, request):
        print('request')
        pass

    # 在每次响应前 都会调用
    def process_response(self, request, response):
        print('response')
        return response


class BookMiddlewareMixin2(MiddlewareMixin):
    # 每次请求前都会调用
    def process_request(self, request):
        print('request2')
        pass

    # 在每次响应前 都会调用
    def process_response(self, request, response):
        print('response2')
        return response
