from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PDFFormSerializer
import PyPDF2

class UploadPDFView(APIView):
    def process_pdf(self, file_path):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            num_pages = pdf_reader.numPages
            # Perform processing or extract information as needed
            # Example: Extract text from the first page
            first_page_text = pdf_reader.getPage(0).extractText()
        return num_pages, first_page_text

    def post(self, request, *args, **kwargs):
        serializer = PDFFormSerializer(data=request.data)
        if serializer.is_valid():
            pdf_file = serializer.validated_data['pdf_file']
            # Save the file temporarily
            with open('temp.pdf', 'wb') as temp_file:
                for chunk in pdf_file.chunks():
                    temp_file.write(chunk)
            # Process the PDF
            num_pages, first_page_text = self.process_pdf('temp.pdf')
            # You can now use 'num_pages' and 'first_page_text' as needed
            return Response({'num_pages': num_pages, 'first_page_text': first_page_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
