from documents.utils import extract_text_from_file


if __name__ == "__main__":
    print(extract_text_from_file
          ("/home/marcus/dev/homero_ocr/homero_ocr/test.pdf")
          )
    print(extract_text_from_file("test.jpg"))
