# views.py
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Todo
from .serializers import TodoSerializer

class TodoView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        todos = Todo.objects.filter(user=user)
        serializer = TodoSerializer(todos, many=True)
        return Response({
            'status': True,
            'data': serializer.data,
            'message': 'Todo fetched successfully'
        })

    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.id  # Assuming user is a ForeignKey in Todo model
            serializer = TodoSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Todo is created',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Invalid Fields',
                    'data': serializer.errors
                })

        except Exception as e:
            return Response({
                'status': False,
                'message': f'Something Went Wrong: {str(e)}',
                'data': {}
            })
    def patch(self, request):
        try:
            data = request.data
            uid = data.get('uid')

            if not uid:
                return Response({
                    'status': False,
                    'message': 'uid is required',
                    'data': {}
                })

            obj = get_object_or_404(Todo, uid=uid, user=request.user)

            serializer = TodoSerializer(obj, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Todo is updated',
                    'data': serializer.data
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Invalid Fields',
                    'data': serializer.errors
                })

        except Todo.DoesNotExist:
            return Response({
                'status': False,
                'message': 'Invalid uid',
                'data': {}
            })

        except Exception as e:
            return Response({
                'status': False,
                'message': f'Something Went Wrong: {str(e)}',
                'data': {}
            })
