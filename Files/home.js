function loadUrl(){
	var searchValue = document.getElementsByTagName('input')[0].value;
	if (searchValue == ""){
		document.getElementsByTagName("a")[0].setAttribute("href","#");
	}else{
		var url = "http://www.google.com/search?q=" + searchValue;
		document.getElementsByTagName("a")[0].setAttribute("href",url);
	}
}