from django.http import JsonResponse
class ResponseTool():
    def success_json_res(data):
        response_data = {
            "code": "SUCCESS",
            "message": "成功",
            "data": data
        }
        return JsonResponse(response_data, safe=False)
    
    def exception_json_res(Exception):
        response_data = {
            "code": "SOME_EXCEPTION",
            "message": str(Exception),
            "data": {}
        }
        return JsonResponse(response_data, safe=False)
    
    