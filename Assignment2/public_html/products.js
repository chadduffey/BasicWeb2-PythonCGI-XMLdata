/**
 * @author Chad Duffey
 * student 11372834B
 */

function init () 
{
	//not required any more
	//enter any set up code here.
}

function calcTotal()
{
	xmlDoc=loadXMLDoc("http://csusap.csu.edu.au/~cduffe02/products.xml") // Path to the XML file;
 	
 	//use N to count the number of items to deal with
 	var N = xmlDoc.getElementsByTagName("product");
 	
 	totalValue = 0;

 	for (i = 0; i < N.length; i++) {
        //syntax for accessing the attributes is:
        //alert(xmlDoc.getElementsByTagName("product")[i].getAttribute('stockid'))
        
        //tidy any NaNs
		if (isNaN(document.getElementById(xmlDoc.getElementsByTagName("product")[i].getAttribute('stockid')).value)) 
			document.getElementById(xmlDoc.getElementsByTagName("product")[i].getAttribute('stockid')).value = 0;

		//sub totals
		var cost = xmlDoc.getElementsByTagName("price")[i].childNodes[0].nodeValue;
		var number = document.getElementById(xmlDoc.getElementsByTagName("product")[i].getAttribute('stockid')).value;
		var subTotal = cost * number;
		document.getElementById(xmlDoc.getElementsByTagName("product")[i].getAttribute('stockid')+'s').value = subTotal.toFixed(2);
		totalValue = totalValue + subTotal;
 	}

 	//update the total
	document.getElementById("total").value = totalValue.toFixed(2);
	
}

function validateForm()
{
  	xmlDoc=loadXMLDoc("http://csusap.csu.edu.au/~cduffe02/products.xml") // Path to the XML file;
 	
 	//use N to count the number of items to deal with
 	var N = xmlDoc.getElementsByTagName("product");
 	
 	for (i = 0; i < N.length; i++) {
        
        //tidy any NaNs
		if (isNaN(document.getElementById(xmlDoc.getElementsByTagName("product")[i].getAttribute('stockid')).value)) 
		{
			alert("Please only use numbers for quantities on the order form");
			return false;
		}
 	}
}

function loadXMLDoc(docname)
 {
	var xmlDocument;
	if (window.XMLHttpRequest)
	{
		xmlDocument=new window.XMLHttpRequest();
		xmlDocument.open("GET",docname,false);
		xmlDocument.send("");
		return xmlDocument.responseXML;
	}
	alert("Something has gone wrong!");
	return null;
 }

	