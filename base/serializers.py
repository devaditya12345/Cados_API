from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *

#3
class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only = True)
    class Meta:
        model = Company
        fields = "__all__"

    def get_employee_count(self,obj):
        count = obj.advocate_set.count()
        return count

# output of #3 @ http://127.0.0.1:8000/companies
# [
#     {
#         "id": 1,
#         "employee_count": 1,
#         "name": "Bhash Software Labs",
#         "bio": "BHASH empowers its customers to communicate between varied IT back-end systems and mobile phones using SMS Services. BHASH provides a unique, end-to-end, global carrier-grade mobile data service. Its mobile data service offering includes \"plug and play\" application licensing and hosting. Employing a partnership with Mobile operators and a clear focus on SMS mobile messaging."
#     },
#     {
#         "id": 2,
#         "employee_count": 2,
#         "name": "DigiFast Technologies",
#         "bio": "We offer the following services....\r\nTransactional SMS\r\nPromotional SMS\r\nOTP Services"
#     },
#     {
#         "id": 3,
#         "employee_count": 1,
#         "name": "ROUNDSMS MARKETING SOLUTIONS",
#         "bio": "Mobile phones have evolved into a very important part of our live and there is no question about it. With the popularity of its usage it has connected the whole world at just one click. With time, marketing and sales had grown itself into it very successfully ‘Bulk SMS’ being at the centre of all.\r\n\r\nROUNDSMS MARKETING SOLUTIONS, being one of the best companies into Bulk SMS service, we understand it very well. We are expertise in providing service and guidance to our customers for using bulk SMS in the best way . With team powered with best trained professional experts in ROUNDSMS MARKETING SOLUTIONS we believe in providing best quality of service that sets a bench mark."
#     }
# ]

# #2
# class CompanySerializer(ModelSerializer):
#     class Meta:
#         model = Company
#         fields = "__all__"

#1
class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields = ['username','bio','company']
        
        # http://127.0.0.1:8000/advocates
        # otput for #2 with #1 & #3 with #1 also: {
        # "username": "Tadas",
        # "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut a",
        # "company": {
        #     "id": 2,
        #     "name": "DigiFast Technologies",
        #     "bio": "We offer the following services....\r\nTransactional SMS\r\nPromotional SMS\r\nOTP Services"
        # }



