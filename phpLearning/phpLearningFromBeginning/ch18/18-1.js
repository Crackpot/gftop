function GetXmlHttpRequest()
{
    var xmlHttp=null;
    try
    {
        xmlHttp = new XMLHttpRequest();                      //对于Firefox等浏览器
    }
    catch(e)
    {
        try
        {
            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");   //对于IE浏览器
        }
        catch (e)
        {
            try
            {
                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch(e)
            {
                xmlHttp = false;
            }            
        }
    }

return xmlHttp;
}