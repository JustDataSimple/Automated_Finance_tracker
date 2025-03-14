def statement_reader(file_path):
    import pypdf

    '''
    Func: Makes pdf accessible for parsing with using 'open'
    Parses, reads, and extracts text from .pdf formatted statements 
    using the pypdf library and the pdfreader class.

    '''


    # open PDF from file path to make it accessible as binary arg: (read binary(rb))
    # stores/assigns binary format file (return value) to variable 'file'
    with open(file_path, 'rb') as file:

        # when called, parses the binary code (from variable 'file') into .pdf format
        # stores/assigns .pdf format (return value) to variable 'reader'
        reader = pypdf.PdfReader(file)

        # reads the all ages in the length of the .pdf
        # extracts the text
        # stores/assigns the extracted text (return value) to variable 'text'
        text = reader.pages[len(reader.pages)].extract_text()
        print(text)

    return text



