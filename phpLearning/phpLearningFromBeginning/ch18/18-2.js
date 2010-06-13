function sendRequest()
{
    //获取页面表单的文本框name的值
    var user_name = document.getElementById("name").value;

    if((user_name == null) || (user_name == ""))
        return;
    
    xmlHttp = GetXmlHttpRequest();
    if(xmlHttp == null)
    {
        alert("浏览器不支持XmlHttpRequest！");
        return;
    } 

    var url = "getUserName.php";               //构建请求的URL地址
    url = url + "?name=" + user_name;
    
    xmlHttp.open("GET", url, true);            //使用GET方法打开一个到url的连接，为发出请求做准备
    
    //设置一个函数，当服务器处理完请求后调用，该函数名为updatePage
    xmlHttp.onreadystatechange = updatePage;
    xmlHttp.send(null);                        //发送请求
}
