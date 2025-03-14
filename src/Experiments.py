def statement_reader(file_path):
    import pypdf

    file = open(file_path, 'rb')

    for f in file:
        reader = pypdf.PdfReader(file_path)
        for num_page in reader:
            num_pgs = len(reader.pages)