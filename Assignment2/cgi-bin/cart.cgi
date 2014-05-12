#!/usr/bin/env python  

# Import modules for CGI handling 
import cgi 

#import the xml library
import xml.dom.minidom

# Open XML document 
XMLDoc = xml.dom.minidom.parse('products.xml')
collection = XMLDoc.documentElement

# Get all the products 
products = collection.getElementsByTagName("product")

# Create instance of FieldStorage 
form = cgi.FieldStorage()

itemQty = 0
tableString = ""

# Check for each product: ----------------------------------------
# This first iteration is just to determine if we have items
for product in products:

  try: 
    itemQty = itemQty + int(form[product.getAttribute("stockid")].value)
  except:
    itemQty = itemQty + 0
#----------------------------------------------------------------

if itemQty < 1:
  tableString = "<p>Nothing has been ordered yet<p/>"
else:
  #insert a gap between the items ordered and the total.
  tableString = tableString + "<br />"
  # build a table of items
  #set up the table headings
  tableString = tableString + '<table class="center" summary="ItemsForSale">'
  tableString = tableString + '<tr>'
  tableString = tableString + '<th>Product Type</th>'
  tableString = tableString + '<th>Stock Id</th>'
  tableString = tableString + '<th>Colour</th>'
  tableString = tableString + '<th>Length</th>'
  tableString = tableString + '<th>Diameter</th>'
  tableString = tableString + '<th>Unit Price</th>'
  tableString = tableString + '<th>Quantity</th>'
  tableString = tableString + '<th>Sub Total</th>'
  tableString = tableString + '</tr>'

  # Check for each product: ----------------------------------------
  # Build the table
  for product in products:

    try: 
      itemNumber = int(form[product.getAttribute("stockid")].value)
    except:
      itemNumber = 0

    if itemNumber > 0:
      #we need to add this item to our table to display
      #start the table row
      tableString = tableString + "<tr>"
      tableString = tableString + "<td>%s</td>" % product.getAttribute("productType")
      tableString = tableString + "<td>%s" % product.getAttribute("stockid")

      colour = product.getElementsByTagName('colour')[0]
      tableString = tableString + "<td>" + colour.childNodes[0].data + "</td>"  
      
      length = product.getElementsByTagName('length')[0]
      tableString = tableString + "<td>" + length.childNodes[0].data + "</td>"  
      
      diameter = product.getElementsByTagName('diameter')[0]
      tableString = tableString + "<td>" + diameter.childNodes[0].data + "</td>" 
      
      price = product.getElementsByTagName('price')[0]
      tableString = tableString + "<td>" + price.childNodes[0].data + "</td>"

      tableString = tableString + "<td>" + str(itemNumber) + "</td>"

      #work out the subtotal for the item and display it
      itemSubTotal = itemNumber 
      tableString = tableString + "<td>" + str(itemSubTotal) + "</td>"

      tableString = tableString + '</tr>'
  #----------------------------------------------------------------    

print "Content-type:text/html\r\n\r\n"
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
print '<html xmlns="http://www.w3.org/1999/xhtml" lang="en">'
print '<head>'
print '<meta http-equiv="Content-Type" content="text/html" />'
print '<script type="text/javascript" src="http://csusap.csu.edu.au/~cduffe02/cart.js"></script>'
print '<link rel="stylesheet" type="text/css" href="http://csusap.csu.edu.au/~cduffe02/theme.css" />'
print '<title>Nuts R Us</title>'
print '</head>'
print '<body>'
print '<div id="whole_page">'
print '<div id="header">Nuts R Us</div>'
print '<div id="nav">'
print '<a href="http://csusap.csu.edu.au/~cduffe02/index.html">   Home | </a>'
print '<a href="http://csusap.csu.edu.au/cgi-pub/cduffe02/products.cgi">  Our Products | </a>'
print '<a href="http://csusap.csu.edu.au/cgi-pub/cduffe02/cart.cgi"> Shopping Cart </a>'
print '</div>'
print '<div id="content">'
print '<div id="logo">'
print '<img src="http://csusap.csu.edu.au/~cduffe02/img/logo.png" alt="MainLogo" width="142" height="142" />'
print '</div>'
print "<h1>Settle your account</h1>"
print '<h2>...And get your nuts in the post</h2>' 
print tableString
print '<form action="" onsubmit="return validateForm()" >'
print '<table class="center" summary="CheckOut">'
print '<tr>'
print '</tr>'
print '<tr>'
print '<th>Name</th>'
print '<td><input type = "text" name="fullname" id="fullname" size="20" /></td>'
print '</tr>'
print '<tr>'
print '<th>Email</th>'
print '<td><input type = "text" name="email" id ="email" size="20" /></td>'
print '</tr>'
print '<tr>'
print '<th>Phone</th>'
print '<td><input type = "text" id ="phone" name="phone" size="20" /></td>'
print '</tr>'
print '<tr>'
print '<th>Address</th>'
print '<td><input type = "text" id ="address" name = "address" size="20" /></td>'
print '</tr>'
print '</table>'
print '<p>'
print '<input type = "submit" value = "Process Order"/>'
print '<input type = "reset" value = "Clear Form"/>'
print '</p>'
print '</form>'
print '</div>'
print '</div>'
print '</body>'
print '</html>'