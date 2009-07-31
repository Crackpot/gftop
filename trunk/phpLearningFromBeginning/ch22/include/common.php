<?php
require_once("setting.php");
require_once("forum.func.php");
function showerrpage($info_str)     //错误提示信息函数
{
	$html = "<html>";
	$html .= "<head><title>提示信息</title></head>";
	$html .= "<body>";

	$html .= "<center>";

	$html .= "<div style=\"border:1px solid #000;background:#F2F3F4;width:500px;font:13px;height:180px;line-height:100px;\">";

	$html .= "<div style=\"border-bottom:1px solid #000;background:#434A56;width:500px;text-align:left;height:28px;line-height:28px;padding:0 0 0 8px;color:#D8DBFE\"><b>提示信息</b></div>";
	$html .= $info_str."<br/>";
	$html .= "<input type=\"button\" onclick=\"javascript:window.history.go(-1);\" value=\"返回\" /><br/>";
	$html .= "</div>";

	$html .= "<center>";

	$html .= "</body>";
	$html .= "<html>";
	
	echo $html;
}

function delete_htm($scr)           //删除html标记
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

function dhtmlspecialchars($string) //html标记处理
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