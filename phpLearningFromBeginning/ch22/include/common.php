<?php
require_once("setting.php");
require_once("forum.func.php");
function showerrpage($info_str)     //������ʾ��Ϣ����
{
	$html = "<html>";
	$html .= "<head><title>��ʾ��Ϣ</title></head>";
	$html .= "<body>";

	$html .= "<center>";

	$html .= "<div style=\"border:1px solid #000;background:#F2F3F4;width:500px;font:13px;height:180px;line-height:100px;\">";

	$html .= "<div style=\"border-bottom:1px solid #000;background:#434A56;width:500px;text-align:left;height:28px;line-height:28px;padding:0 0 0 8px;color:#D8DBFE\"><b>��ʾ��Ϣ</b></div>";
	$html .= $info_str."<br/>";
	$html .= "<input type=\"button\" onclick=\"javascript:window.history.go(-1);\" value=\"����\" /><br/>";
	$html .= "</div>";

	$html .= "<center>";

	$html .= "</body>";
	$html .= "<html>";
	
	echo $html;
}

function delete_htm($scr)           //ɾ��html���
{
	$str="";
	for($i=0;$i<strlen($scr);$i++)
	{
		if(substr($scr,$i,1)=="<") 
		{
			while(substr($scr,$i,1)!=">") $i++;
			continue;
		}
		$str .= substr($scr,$i,1);
	}
return $str; 
}

function dhtmlspecialchars($string) //html��Ǵ���
{
	if(is_array($string))
	{
		foreach($string as $key => $val)
		{
			$string[$key] = dhtmlspecialchars($val);
		}
	}
	else
	{
		$string = preg_replace('/&amp;((#(\d{3,5}|x[a-fA-F0-9]{4})|[a-zA-Z][a-z0-9]{2,5});)/', '&\\1',
		str_replace(array('&', '"', '<', '>'), array('&amp;', '&quot;', '&lt;', '&gt;'), $string));
	}
	return $string;
}
?>