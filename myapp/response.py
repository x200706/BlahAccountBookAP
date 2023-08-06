from django.http import JsonResponse
class ResponseTool():
    def jsob_res(data):
        try:
            response_data = {
                "message": "成功",
                "code": "SUCCESS",
                "data": data
            }
        except Exception as e:
            response_data = {
                "message": "Something throw a exception.",
                "code": "SOME_EXCEPTION",
                "error": str(e)
            }
        return JsonResponse(response_data, safe=False)
    