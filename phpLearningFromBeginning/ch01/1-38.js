function checkForm()
{   
    if(document.fdata.num.value==""
    || document.fdata.al.value==""
    || document.fdata.lan.value=="0"
    )
    {
        alert("表单中的每一项都必须填写！");
        return false;
    }

    if(document.fdata.num.value!="")
    {
        var s = document.fdata.num.value;
        if(s.length > 9)
        {
            alert("第1个文本框字符串长度要小于10！");
            return false;
        }
        for(var loc=0; loc<s.length; loc++)
        {
            if((s.charAt(loc) < '0') || (s.charAt(loc) > '9'))
            {
                alert("第1个文本框只能输入数字！");
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
                alert("第2个文本框只能输入英文字母！");
                return false;
            }
        }
    }
    
    var v = document.fdata.lan.value; 
    
    var str = "您的填写和选择为：\r\n" + s + "\r\n" + t + "\r\n" + v;
    alert (str);
}
