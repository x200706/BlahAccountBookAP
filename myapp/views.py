from django.http import JsonResponse
from django.db import transaction
from rest_framework.generics import GenericAPIView
from myapp.serializers import UserSerializer
from myapp.models import User


# class UsersView(GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         users = self.get_queryset()
#         serializer = self.serializer_class(users, many=True)
#         data = serializer.data
#         response_data = {
#             "message": "Success",
#             "code": "SUCCESS",
#             "data": data
#         }
#         return JsonResponse(response_data, safe=False)

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         try:
#             serializer = self.serializer_class(data=data)
#             serializer.is_valid(raise_exception=True)
#             with transaction.atomic():
#                 serializer.save()
#             data = serializer.data
#             response_data = {
#                 "message": "Success",
#                 "code": "SUCCESS",
#                 "data": data
#             }
#         except Exception as e:
#             response_data = {
#                 "message": "Something throw a exception.",
#                 "code": "SOME_EXCEPTION",
#                 "error": str(e) # 不過比起這樣打印，我比較想記入日誌就好
#             }
#         return JsonResponse(response_data)
