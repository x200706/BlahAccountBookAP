from django.http import JsonResponse
class ResponseTool():
    def jsob_res(data):
        try:
            response_data = {
                "message": "Success",
                "code": "SUCCESS",
                "data": data
            }
        except Exception as e:
            response_data = {
                "message": "Something throw a exception.",
                "code": "SOME_EXCEPTION",
                "error": str(e) # 不過比起這樣打印，我還想計入日誌
            }
        return JsonResponse(response_data, safe=False)
    