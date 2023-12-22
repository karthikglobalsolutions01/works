


     
import pdfplumber
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Pdf_Info_Table
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.serializer import PDFFormSerializer
from rest_framework import status

# class ReadPDFView(APIView):
#     def post(self, request):
#         data = request.data.get('pdf_file')
        
#         with pdfplumber.open(data) as pdfs:
#             first_page_text = pdfs.pages[0].extract_text()

#         result_dict = self.extract_info(first_page_text)
#         return Response(result_dict)

#     def extract_info(self, first_page_text):
#         inv_number = self.extract_info_by_pattern("[0-9]+/[0-9]+/H/[0-9]+", first_page_text)
#         cstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]", first_page_text)
#         gstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}", first_page_text)
#         state_code = self.extract_info_by_pattern("State Code:.+", first_page_text)
#         invoice_amount = self.extract_info_by_pattern("Invoice Amount:.+", first_page_text)

#         # result_dict = {
#         #      "Invoice Number": inv_number[0] if inv_number else None,
#         #      "CSTIN": cstin[0] if cstin else None,
#         #      "GSTIN": gstin[0] if gstin else None,
#         #      "State Code": state_code[0] if state_code else None,
#         #      "Invoice Amount": invoice_amount[0] if invoice_amount else None
#         #  }

#         # return result_dict
#         pdf_info = Pdf_Info_Table(
#             Invoice_Number=inv_number,
#             CSTIN=cstin,
#             GSTIN=gstin,
#             State_Code=state_code,
#             Invoice_Amount=invoice_amount[1] if invoice_amount else None
#         )
#         pdf_info.save()

#     def extract_info_by_pattern(self, pattern, first_page_text):
#         matches = re.findall(pattern, first_page_text)
#         return matches

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
        # Assuming you want to update an existing PDF record
#         pdf_id = id
#         if not pdf_id:
#             return Response({"error": "Please provide the 'id' of the PDF record to update."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             pdf_info = Pdf_Info_Table.objects.get(id=pdf_id)
#         except Pdf_Info_Table.DoesNotExist:
#             return Response({"error": f"PDF record with id {pdf_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)

#         # Update the existing PDF record
#         data = request.data.get('pdf_file')
#         with pdfplumber.open(data) as pdfs:
#             first_page_text = pdfs.pages[0].extract_text()
       
#         inv_number = self.extract_info_by_pattern("[0-9]{2}-[0-9]{2}/\)H/[0-9]{2}+", first_page_text)
#         print(inv_number)
#         cstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]", first_page_text)
#         gstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}", first_page_text)
#         state_code = self.extract_info_by_pattern("State Code: \w{2} \- \d{2}", first_page_text)
#         result_dict = {
#                "Invoice Number": inv_number[0] if inv_number else None,
#                "CSTIN": cstin[0] if cstin else None,
#                "GSTIN": gstin[0] if gstin else None,
#                "State Code": l,
            
                
#            }
#             # Update the fields you want to change
#         pdf_info.Invoice_Number = result_dict['Invoice Number'] if result_dict['Invoice Number'] else pdf_info.Invoice_Number
#         pdf_info.CSTIN = result_dict['CSTIN'] if result_dict['CSTIN'] else pdf_info.CSTIN
#         pdf_info.GSTIN = result_dict['GSTIN'] if result_dict['GSTIN'] else pdf_info.GSTIN
#         pdf_info.State_Code = result_dict['State Code'] if result_dict['State Code'] else pdf_info.State_Code

#             # Save the updated record
#         pdf_info.save()

#         return Response({"status": "ok"})
#     def extract_info_by_pattern(self, pattern, first_page_text):
#          matches = re.findall(pattern, first_page_text)
#          return matches

# # ... (rest of the code)
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
     
            
        
        