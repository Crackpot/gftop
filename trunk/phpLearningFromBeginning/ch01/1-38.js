function checkForm()
{   
    if(document.fdata.num.value==""
    || document.fdata.al.value==""
    || document.fdata.lan.value=="0"
    )
    {
        alert("���е�ÿһ�������д��");
        return false;
    }

    if(document.fdata.num.value!="")
    {
        var s = document.fdata.num.value;
        if(s.length > 9)
        {
            alert("��1���ı����ַ�������ҪС��10��");
            return false;
        }
        for(var loc=0; loc<s.length; loc++)
        {
            if((s.charAt(loc) < '0') || (s.charAt(loc) > '9'))
            {
                alert("��1���ı���ֻ���������֣�");
                return false;
            }
        }
    }
    
    if(document.fdata.al.value!="")
    {
        var t = document.fdata.al.value;
        for(var loc=0; loc<t.length; loc++)
        {
            if(((t.charAt(loc) < 'a') || (t.charAt(loc) > 'z')) && ((t.charAt(loc) < 'A') || (t.charAt(loc) > 'Z'))) 
            {
                alert("��2���ı���ֻ������Ӣ����ĸ��");
                return false;
            }
        }
    }
    
    var v = document.fdata.lan.value; 
    
    var str = "������д��ѡ��Ϊ��\r\n" + s + "\r\n" + t + "\r\n" + v;
    alert (str);
}