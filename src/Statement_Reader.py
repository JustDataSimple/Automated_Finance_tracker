def statement_reader(file_path):
    import pypdf

    '''
    Func: 

    '''


    # open PDF from file path to make it accessible as binary arg: (read binary(rb))
    # stores/assigns binary format file (return value) to variable 'file'
    with open(file_path, 'rb') as file:

        # when called, parses the binary code (from variable 'file') into .pdf format
        # stores/assigns .pdf object (return value) to variable 'reader'
        reader = pypdf.PdfReader(file)

        # accesses pages in the length of the .pdf
        # stores/assigns the total number of pages ((int) return value) to variable 'num_pages'
        #num_pages = lereader.pages

        #outputs the total number of pages to the console
        #print(f"Number of pages: {num_pages}")

        # for loop that iterates over each page, starting at '0'
        for p in range(len(reader.pages)):

            # contains appended text
            # this allows for a custom output
            #out = []

            #sores/assigns the current index "p" ((pdf page) return value) to variable 'page'
            page = reader.pages[p]

            # extracts the text from current index ((variable 'page') 'p')
            # stores/assigns extracted text (return value) to variable 'text'
            text = page.extract_text()

            # outputs: The text on page (page number) is: (extracted text)
            #out.append

    return f"Below is the text from PAGE {p+1}: \n{text}\n "
#"\n".join((out))
pdf = statement_reader('C:\\users\\antuj\\onedrive\\documents\\finance\\statements\\chime\\Tamara_Russell_Checking_eStatement-1.pdf')
print(pdf)