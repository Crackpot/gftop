function GetXmlHttpRequest()
{
    var xmlHttp=null;
    try
    {
        xmlHttp = new XMLHttpRequest();                      //����Firefox�������
    }
    catch(e)
    {
        try
        {
            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");   //����IE�����
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