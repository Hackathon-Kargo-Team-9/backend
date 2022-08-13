from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DriverSerializers
from .models import Driver
# Create your views here.

class DriverAPIView(APIView):
    serializer_class = DriverSerializers
    def get_queryset(self):
        driver = Driver.objects.all()
        return driver

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                driver = Driver.objects.get(id=id)
                serializer = DriverSerializers(driver)
        except:
            drivers = self.get_queryset()
            serializer = DriverSerializers(drivers, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        driver_data = request.data

        new_driver = Driver.objects.create(name=driver_data["name"], status=driver_data[
            "status"], phone_number=driver_data["phone_number"], driver_license=driver_data["driver_license"])

        new_driver.save()

        serializer = DriverSerializers(new_driver)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        driver_object = Driver.objects.get(id=id)

        data = request.data

        driver_object.car_brand = data["car_brand"]
        driver_object.car_model = data["car_model"]
        driver_object.production_year = data["production_year"]
        driver_object.car_body = data["car_body"]
        driver_object.engine_type = data["engine_type"]

        driver_object.save()

        serializer = DriverSerializers(driver_object)
        return Response(serializer.data)