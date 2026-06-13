from Tracker.models import RequestLogs


class RequestLogin:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        
        request_info = (request)
        print(request_info.path , request_info.method)
        RequestLogs.objects.create(   
            request_info= vars(request_info),
            request_type= request_info.path,
            method= request_info.method,
            ip_address = request_info.META.get('REMOTE_ADDR'),
        )
       
        return self.get_response(request)
        