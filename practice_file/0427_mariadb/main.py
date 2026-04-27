import os

# import easyocr
# from pdf2image import convert_from_path

# def main():
#     print("start ocr")
#     reader = easyocr.Reader(['ko', 'en'])
#     result = reader.readtext('da7ca0606f54d903.jpg')
#     texts = [item[1] for item in result]
#     clean_text = ''.join(texts)
#     print(clean_text)


import fitz  # PyMuPDF
import pdfplumber
import pandas as pd

def extract_text_from_pdf(pdf_path, numbers):
    doc = fitz.open(pdf_path)
    all_text = []
    
    for page_num in numbers:
        page = doc[page_num]
        text = page.get_text()
        all_text.append(text)
    return all_text

def save(pdf_path, page_nums):
    file_path = r"C:\Users\hi\Desktop\Sooah\fullstack-journey\practice_file\0427_mariadb\save_file"
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_name = "중대성평가.csv"
        save_path = os.path.join(file_path, file_name)
        final_rows = []
        with pdfplumber.open(pdf_path) as pdf:
            for pg_num in page_nums:
                page = pdf.pages[pg_num]

                table = page.extract_table()
                # table_obj=[t.bbox for t in table]

                extracted_table = page.extract_table()
                page_text = page.extract_text()
                if page_text:
                    for line in page_text.split('\n'):
                        final_rows.append([line])
                
                for table in extracted_table:
                    final_rows.append("-----------[표]-----------")
                    for row in table:
                        clean_row = [str(cell).replace('\n', ' ') if cell else "" for cell in row]
                        formatted_row = ",".join(clean_row)
                        final_rows.append([formatted_row])
                    final_rows.append("-----------[표]-----------")
        df = pd.DataFrame(final_rows)
        df.to_csv(save_path, index=False, header=False, encoding="utf-8")
        print(f"성공: {save_path}에 저장되었습니다.")
    except Exception as e:
        print(f"저장 중 오류 발생: {e}")

# 사용 예시
def main():
    pdf_path = '현대모비스_SR 2025_K_1027.pdf'
    # texts = extract_text_from_pdf(pdf_path, [30,31,32,33])
    save(pdf_path, [30,31,32,33])


if __name__ == "__main__":
    main()
