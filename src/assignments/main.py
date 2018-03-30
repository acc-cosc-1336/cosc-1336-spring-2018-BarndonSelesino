#Write import statements for classes invoice and invoice_item
from src.assignments.invoice import Invoice
from src.assignments.invoice_item import InvoiceItem

'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
invoice_items = []
def Main():
    invoice = Invoice('blah', '14')
    hiya = 'y'
    while hiya == 'y' or hiya == "Y":
        description = input('enter description:   ')
        quantity = int(input('enter quantity:   '))
        cost = float(input('Enter cost:   '))

        invoice_item = InvoiceItem(description, quantity, cost)
        invoice.add_invoice_item(invoice_item)
        hiya = input('type y to continue...')
        if hiya != 'y':
            invoice.print_invoice()
Main()

    
    
