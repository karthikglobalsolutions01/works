


     
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
    def put(self, request, id):
        pdf_info = Pdf_Info_Table.objects.get(id=id)
        serializer = PDFFormSerializer(pdf_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        pdf_info =Pdf_Info_Table.objects.get(id=id)
        pdf_info.delete()