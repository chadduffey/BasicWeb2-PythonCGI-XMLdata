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

print "Content-type:text/html\r\n\r\n"
print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
print '<html xmlns="http://www.w3.org/1999/xhtml" lang="en">'
print '<head>'
print '<meta http-equiv="Content-Type" content="text/html" />'
print '<script type="text/javascript" src="http://csusap.csu.edu.au/~cduffe02/products.js"></script>'
print '<link rel="stylesheet" type="text/css" href="http://csusap.csu.edu.au/~cduffe02/theme.css" />'
print '<title>Nuts R Us</title>'
print '</head>'
print '<body>'
print '<div id="whole_page">'
print '<div id="header">Nuts R Us</div>'
print '<div id="nav">'
print '<a href="http://csusap.csu.edu.au/~cduffe02/index.html">   Home | </a>'
print '<a href="hhttp://csusap.csu.edu.au/cgi-pub/cduffe02/products.cgi">  Our Products | </a>'
print '<a href="http://csusap.csu.edu.au/cgi-pub/cduffe02/cart.cgi"> Shopping Cart </a>'
print '</div>'
print '<div id="content">'
print '<div id="logo">'
print '<img src="http://csusap.csu.edu.au/~cduffe02/img/logo.png" alt="MainLogo" width="142" height="142" />'
print '</div>'
print "<h1>Products Page</h1>"
print '<h2>What can we do for you today?</h2>' 
#main part - need to get the action in here:

print '<form action = "/cgi-pub/cduffe02/cart.cgi" onsubmit="return validateForm()" method="post">'
print '<table class="center" summary="ItemsForSale">'

#set up the table headings
print '<tr>'
print '<th>Product Type</th>'
print '<th>Stock Id</th>'
print '<th>Colour</th>'
print '<th>Length</th>'
print '<th>Diameter</th>'
print '<th>Unit Price</th>'
print '<th>Quantity</th>'
print '<th>Sub Total</th>'
print '</tr>'

# Print each product:
for product in products:

	#start the table row
	print "<tr>"
	if product.hasAttribute("productType"):
	    print "<td>%s</td>" % product.getAttribute("productType")
	if product.hasAttribute("stockid"):
		print "<td>%s" % product.getAttribute("stockid")

	colour = product.getElementsByTagName('colour')[0]
	print "<td>%s</td>" % colour.childNodes[0].data
	length = product.getElementsByTagName('length')[0]
	print "<td>%s</td>" % length.childNodes[0].data
	diameter = product.getElementsByTagName('diameter')[0]
	print "<td>%s</td>" % diameter.childNodes[0].data
	price = product.getElementsByTagName('price')[0]
	print "<td>%s</td>" % price.childNodes[0].data

	print '<td><input type = "text" name = "%s" id = "%s" size="2" /></td>' % (product.getAttribute("stockid"), product.getAttribute("stockid"))
	print '<td><input type = "text" name = "%s" id = "%s" size="4" disabled="disabled"/></td>' % (product.getAttribute("productType"), product.getAttribute("stockid"))

	#close the table row
	print "<tr>"
	################

print '</table>'
print '<p>'
print '<input type = "submit" value = "Submit Order" />'
print '<input type = "reset" value = "Clear Order Form"/>'
print '</p>'
print '</form>'

#closing tags
print '</div>'
print '</div>'
print '</body>'    
print '</html>'