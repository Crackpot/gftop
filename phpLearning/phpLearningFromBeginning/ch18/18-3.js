function updatePage()
{
    if(xmlHttp.readyState == 4)
    {
        var response = xmlHttp.responseText;
        document.getElementById("userInfo").value = response;
    }
}
