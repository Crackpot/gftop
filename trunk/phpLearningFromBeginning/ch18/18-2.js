function sendRequest()
{
    //��ȡҳ������ı���name��ֵ
    var user_name = document.getElementById("name").value;

    if((user_name == null) || (user_name == ""))
        return;
    
    xmlHttp = GetXmlHttpRequest();
    if(xmlHttp == null)
    {
        alert("�������֧��XmlHttpRequest��");
        return;
    } 

    var url = "getUserName.php";               //���������URL��ַ
    url = url + "?name=" + user_name;
    
    xmlHttp.open("GET", url, true);            //ʹ��GET������һ����url�����ӣ�Ϊ����������׼��
    
    //����һ�����������������������������ã��ú�����ΪupdatePage
    xmlHttp.onreadystatechange = updatePage;
    xmlHttp.send(null);                        //��������
}
