from job.models import joboffer
from rest_framework import status
from rest_framework.views import APIView
from .serializers import joboffer_serializer
from job.models import joboffer
from rest_framework.response import Response
import traceback
class ListJobOffer(APIView):
    def get(self,request):
        try:
            print('********************************************************',request)
            job_offer_instance =  joboffer.objects.all()
            job_offer_json =  joboffer_serializer(job_offer_instance,many=True).data
            return Response(job_offer_json)
        except Exception as e:
            return Response(f'Error :{e}')

    def post(self,request):
        print(f'request.data ***********************************: {request.data}')
        serialized_data =  joboffer_serializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        


class joboffer_detail(APIView):

    def get(self, request, pk):
        instance =  joboffer.objects.get(pk=pk)
        instance_serializer = joboffer_serializer(instance)
        return Response(instance_serializer.data)

    def put(self, request ,pk):
        instance = joboffer.objects.get(pk=pk)
        instance_serializer = joboffer_serializer(instance, data=request.data)
        if instance_serializer.is_valid():
            instance_serializer.save()
            return Response(instance_serializer)
        return Response(instance_serializer.errors ,  status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request, pk):
        job = joboffer.objects.get(pk=pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

