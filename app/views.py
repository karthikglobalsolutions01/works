


     
import pdfplumber
import re
from rest_framework.views import APIView
from rest_framework.response import Response

class ReadPDFView(APIView):
    def post(self, request):
        data = request.data.get('pdf_file')
        
        with pdfplumber.open(data) as pdfs:
            first_page_text = pdfs.pages[0].extract_text()

        result_dict = self.extract_info(first_page_text)
        return Response(result_dict)

    def extract_info(self, first_page_text):
        inv_number = self.extract_info_by_pattern("[0-9]+/[0-9]+/H/[0-9]+", first_page_text)
        cstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]", first_page_text)
        gstin = self.extract_info_by_pattern("[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{2}Z[A-Z]{1}", first_page_text)
        state_code = self.extract_info_by_pattern("State Code:.+", first_page_text)
        invoice_amount = self.extract_info_by_pattern("Invoice Amount:.+", first_page_text)

        result_dict = {
            "Invoice Number": inv_number[0] if inv_number else None,
            "CSTIN": cstin[0] if cstin else None,
            "GSTIN": gstin[0] if gstin else None,
            "State Code": state_code[0] if state_code else None,
            "Invoice Amount": invoice_amount[0] if invoice_amount else None
        }

        return result_dict

    def extract_info_by_pattern(self, pattern, first_page_text):
        matches = re.findall(pattern, first_page_text)
        return matches
     
