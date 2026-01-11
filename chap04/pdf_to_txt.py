import pymupdf
import os

pdf_file_path = "chap04/data/리눅스마스터2급20220903(학생용).pdf"
doc = pymupdf.open(pdf_file_path)

full_text = ''

for page in doc:
    text = page.get_text() # 페이지 텍스트 추출
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

txt_file_path = f"chap04/output/{pdf_file_name}.txt"
with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)