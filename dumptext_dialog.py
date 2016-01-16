import textract
from Tkinter import Tk
import tkFileDialog
import string
def getFilenames():
    """Returns list of files for use"""
    root = Tk().withdraw()
    list_of_filenames = tkFileDialog.askopenfilenames()
    return list_of_filenames

def get_text_from_files(files_to_process):
    """Extracts text from each file given a list of file_names"""
    file_text_dict = {}
    for file_name in iter(files_to_process):
        extracted_text = textract.process(file_name)
        file_text_dict[file_name] = extracted_text
    return file_text_dict


if __name__ == '__main__':
    files_to_process = getFilenames()
    fnameTextDict = get_text_from_files(files_to_process)
    for key, item in fnameTextDict.items():
        newfname = tkFileDialog.asksaveasfilename()
        with open(newfname,'w') as f:
            f.write(filter(lambda x: x in string.printable, item))
        
