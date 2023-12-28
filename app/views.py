import pdfplumber
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Pdf_Info_Table
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from app.serializer import PDFFormSerializer
from rest_framework import status



class ReadPDFView(APIView):
    def post(self, request):
        data = request.data.get('pdf_file')
        
        with pdfplumber.open(data) as pdfs:
            first_page_text = pdfs.pages[0].extract_text()
            result_dict = self.extract_info(first_page_text)
            return Response({"status":"ok"})


        # Save data to the database
        


    def extract_info(self, first_page_text):
         inv_number = self.extract_info_by_pattern("[0-9]{2}-[0-9]{2}/\)H/[0-9]{2}+", first_page_text)
         print(inv_number)
         cstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]", first_page_text)
         gstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}", first_page_text)
         state_code = self.extract_info_by_pattern("State Code: \w{2} \- \d{2}", first_page_text)
         print(state_code)
         k=(state_code[1].split(":"))
         datatypetype=type(k)
         print(datatypetype)
         l=k[1]
         print(l)
         print(k)
         print(state_code)
        

         result_dict = {
               "Invoice Number": inv_number[0] if inv_number else None,
               "CSTIN": cstin[0] if cstin else None,
               "GSTIN": gstin[0] if gstin else None,
               "State Code": l,
            
                
           }
         print(result_dict["State Code"])

         pdf_info = Pdf_Info_Table(
            Invoice_Number=result_dict['Invoice Number'],
            CSTIN=result_dict['CSTIN'],
            GSTIN=result_dict['GSTIN'],
            State_Code=result_dict['State Code'],
        )
         pdf_info.save()
         return Response(result_dict)
    
    def extract_info_by_pattern(self, pattern, first_page_text):
         matches = re.findall(pattern, first_page_text)
         return matches
    def get(self, request):

        pdf_info_records = Pdf_Info_Table.objects.all()

        # Example: Return data as a JSON response
        response_data = [{"id":record.id,"Invoice_Number": record.Invoice_Number, "CSTIN": record.CSTIN, "GSTIN": record.GSTIN, "State_Code": record.State_Code} for record in pdf_info_records]
        return Response(response_data)
class DeletePut(APIView):
    def put(self, request,id):
         pdf_info = Pdf_Info_Table.objects.get(id=id)
         data = request.data
         data=data.dict()

         with pdfplumber.open(data.get("pdf_file")) as pdfs:
            first_page_text = pdfs.pages[0].extract_text()

         inv_number = re.findall("[0-9]{2}-[0-9]{2}/\)H/[0-9]{2}+", first_page_text)
         cstin = re.findall("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]", first_page_text)
         gstin = re.findall("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}", first_page_text)
         state_code = re.findall("State Code: \w{2} \- \d{2}", first_page_text)
         k = state_code[1].split(":")
         l = k[1]
         result_dict = {
            "Invoice Number": inv_number[0] if inv_number else None,
            "CSTIN": cstin[0] if cstin else None,
            "GSTIN": gstin[0] if gstin else None,
            "State Code": l,
         }

        # Check if the provided invoice number matches the existing one
         if pdf_info.Invoice_Number == result_dict["Invoice Number"]:
             Pdf_Info_Table.objects.filter(Invoice_Number=result_dict["Invoice Number"]).update(CSTIN=result_dict['CSTIN'],GSTIN=result_dict['GSTIN'],State_Code=result_dict['State Code'])
             #     serializer = PDFFormSerializer(pdf_info, result_dict)
        #   Pdf_Info_Table.objects.filter(id=id).update({'Invoice Number':'result_dict[Invoice Number]','CSTIN':'result_dict[CSTIN]','GSTIN':'result_dict[GSTIN]',"State Code": 'result_dict[l]'})
         #    if serializer.is_valid(raise_exception=True):
         #        updated_instance = serializer.save()
         #        return Response({"status": "ok", "data": updated_instance.data})
         # return Response({"status": "error", "message": "Invoice number does not match."})

            
        # elif pdf_info.Invoice_Number != inv_number :
        #     def post(self, request):
        #         data = request.data.get('pdf_file')
        
        #     with pdfplumber.open(data) as pdfs:
        #      first_page_text = pdfs.pages[0].extract_text()
        #      result_dict = self.extract_info(first_page_text)
        #      return Response({"status":"ok"})


        # # Save data to the database
        


        #     def extract_info(self, first_page_text):
        #       inv_number = self.extract_info_by_pattern("[0-9]{2}-[0-9]{2}/\)H/[0-9]{2}+", first_page_text)
        #     print(inv_number)
        #         cstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]", first_page_text)
        #         gstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}", first_page_text)
        #         state_code = self.extract_info_by_pattern("State Code: \w{2} \- \d{2}", first_page_text)
        #         print(state_code)
        #         k=(state_code[1].split(":"))
        #         datatypetype=type(k)
        #         print(datatypetype)
        #         l=k[1]
         
        #       result_dict = {
        #        "Invoice Number": inv_number[0] if inv_number else None,
        #        "CSTIN": cstin[0] if cstin else None,
        #        "GSTIN": gstin[0] if gstin else None,
        #        "State Code": l,
            
                
        #    }

        
        #      print(result_dict["State Code"])

        #  pdf_info = Pdf_Info_Table(
        #     Invoice_Number=result_dict['Invoice Number'],
        #     CSTIN=result_dict['CSTIN'],
        #     GSTIN=result_dict['GSTIN'],
        #     State_Code=result_dict['State Code'],
        # )
        #  pdf_info.save()
        #  return Response(result_dict)
    
        # def extract_info_by_pattern(self, pattern, first_page_text):
        #    matches = re.findall(pattern, first_page_text)
        # return matches
        # else:
        #     r eturn Response({"error": "Invoice number mismatch"}, status=400)

def delete(self, request, id):
    pdf_info =Pdf_Info_Table.objects.get(id=id)
    pdf_info.delete()

       
        #function based api views 
        # @api_view(['GET','POST','PUT','DELETE'])
        # def file_list(request):
        #  try:
        #   snippet = Pdf_Info_Table.objects.get(id=id)
        #  except Pdf_Info_Table.DoesNotExist:
        #    return Response(status=status.HTTP_404_NOT_FOUND)
        #  if request.method == 'GET':
        #     lol= Pdf_Info_Table.objects.all()
        #     serializers=PDFFormSerializer(lol,many=True)
        #     return Response(serializers.data)
        #  elif request.method == 'POST':
        #      serializers=PDFFormSerializer(data=request.data)
        #      if serializers.is_valid():
        #           serializers.save()
        #           return Response(serializers.data)
        #  elif request.method =='PUT':
        #      serializers=PDFFormSerializer(snippet,data=request.data)
        #      if serializers.is_valid():
        #          serializers.save()
        #          return Response(serializers.data)
            #mixin classes listmodel mixin will be used to get the data createmodelmixin will be used as post 
#             #update model mixin used to update the data destroymodelmixin for destroying 
# class mixins(mixins.RetrieveModelMixin,
#              mixins.UpdateModelMixin,
#              mixins.DestroyModelMixin,
#              mixins.ListModelMixin,
#              generics.GenericAPIView):
#     queryset=Pdf_Info_Table.objects.all()
#     serializer_class=PDFFormSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
#     def get(self,request,**kwargs):#to get a particular element using a id 
#         return self.retrieve(request,**kwargs)
#     def put(self,request,**kwargs):
#         return self.update(request,**kwargs)
# this is a authentication process a basic authentication which is doen locally if we  ta ke that and place in settings it will be globally applied 
# class viewset(viewsets.ModelViewSet):
#     queryset=Pdf_Info_Table.objects.all()
#     serializers=PDFFormSerializer
#     authentication_class=[SessionAuthentication,TokenAuthentication]
#     permission_classes=[IsAuthenticated]
#     permission_classes=[IsAdminUser]
    
    #authentication and permission 
    #types of authentication 
    #basic authentication,token authentication ,session authentication remote user authentications
    
            
            
            
             
            
            
    # def put(self,request):
    #  username = request.data('result_dict')
    #  user = Pdf_Info_Table.objects.get(CSTIN)
    #  serialized = PDFFormSerializer(data = request.data)
    #  if serialized.is_valid():
    #     serialized.update(user,serialized.valsidated_data)
    #session authentication done on backside unauthorized http 403 forbidden it  will show 

