import pypdf

"""PDF Statement Reader Module.

This module provides functionality to read and extract text from PDF files.
It allows users to select specific pages to view from a PDF document.
"""


def statement_reader(file_path):


    """Extract text from a PDF file and allow user to select a specific page.

    This function opens a PDF file, extracts text from all pages, and
    prompts the user to select a specific page to view. It returns
    the text content of the selected page.

    Args:
        file_path (str): Path to the PDF file to be read.

    Returns:
        str: A formatted string containing the selected page number and its text content.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the user enters an invalid page number.
    """


    # open PDF from file path to make it accessible as binary arg: (read binary(rb))
    # stores/assigns binary format file (return value) to variable 'file'
    try:
        with open(file_path, 'rb') as file:

            # dictionary to store page numbers and their text content
            texts = {}

            # when called, parses the binary code (from variable 'file') into .pdf format
            # stores/assigns .pdf object (return value) to variable 'reader'
            # stores/assigns the length (number of pages) of the pdf in variable
            reader = pypdf.PdfReader(file)
            total_pages = len(reader.pages)

            # iterates over each page
            # stores/assigns the current index "p" ((pdf page) return value) to variable 'page'
            # extracts the text from current index ((variable 'page') 'p')
            # stores/assigns extracted text ('page' (return value)) to dictionary 'texts'
            # uses p (current page number), plus one (for base-10 indexing); as a key for indexing to the desired page
            for p in range(total_pages):
                page = reader.pages[p]
                texts[p + 1] = page.extract_text()
                print(texts)
            
                for i in texts:
                    words = []
                    while i < len(texts):
                        txtWords = texts[i].split()
                        words.append(txtWords)
                    for j in words:
                        return j

            # keep asking until a valid integer is returned
            while True:
                try:
                    # prompt user for page selection
                    user_input = int(input(f"Total number of pages: {total_pages} \nEnter the page number of the text you would like to convert (1-{total_pages}): \n"))

                    # validate user input
                    if 1 <= user_input <= total_pages:
                        break
                    else:
                        print(f"Invalid page number: {user_input}")
                except ValueError:
                    print("Please enter a number, not text.")

            # when while loop runs false, returns: The text on page (page number) is: (extracted text)
            return f"Below is the table from PAGE {user_input}:\n {texts[user_input]}"

    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found. Please check the path and try again."
    # catch all for any stray errors
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    

# Execute only when run directly
if __name__ == "__main__":
    # Code to run when you run THIS file directly
    file_path = input("Enter path to PDF file: ")
    pdf_text = statement_reader(file_path)
    print(pdf_text)