import subprocess

from .celery import app

import datetime

@app.task
def convert_to_pdf(docx_file_content):

    create_the_docx_locally(docx_file_content)

    convert_docx_to_pdf()

    delete_the_previously_created_docx()

    pdf_file_content = get_pdf_file_content()

    return pdf_file_content

def create_the_docx_locally(docx_file_content):

    fd = open("temp.docx","wb")

    fd.write(docx_file_content)

    fd.close()

def convert_docx_to_pdf():
    try:
        # Call unoconv to convert the input file to PDF
        subprocess.run(['unoconv', '--output', 'Format3Flex_'++'.pdf', input_file])
        print(f'Successfully converted {input_file} to PDF.')
    except subprocess.CalledProcessError:
        print(f'Error converting {input_file} to PDF.')

def delete_the_previously_created_docx():
    pass


