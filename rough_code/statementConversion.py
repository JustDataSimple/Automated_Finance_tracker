 # Import Module 
import pdftables_api 

def create_csv(pdf_text):

 # API KEY VERIFICATION 
 conversion = pdftables_api.Client("u75vy1661luj") 

 KEYWORD = {
    'Bank_Institution': {
        'Chime': ['CHIME', 'Chime', 'chime'],
        'CashApp': ['CASH APP', 'CASHAPP', 'CashApp', 'Cash App', 'cashapp', 'cash app'],
        'Paypal': ['PAYPAL', 'PAY PAL', 'paypal', 'pay pal']
    },
    'Account_Type': {
        'Savings': ['SAVINGS', 'SAVING', 'Savings', 'Saving', 'savings', 'saving'],
        'Checking': ['CHECKING', 'CHECK', 'Checking', 'Check', 'checking', 'check'],
        'Debit': ['DEBIT', 'Debit', 'debit'],
        'Credit': ['CREDIT', 'Credit', 'credit']
    }
}

# new file name
newFileName = ()

for match in pdf_text:
 if match == KEYWORD:




# (Hello.pdf, Hello) 
conversion.csv(pdf_file_path, output_file_path)
