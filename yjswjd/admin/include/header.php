<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
 "http://www.w3.org/TR/html4/loose.dtd">
<HTML xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh" lang="zh">
 <HEAD>
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<script language="javascript">
function isCookie() {
  if(navigator.cookieEnabled) {
    //alert("浏览器开启了Cookie");
  } else {
    alert("请开启Cookie来访问本站!");
  }
}
isCookie();
</script>
<?php
if (!isset($page_title)) {
  $page_title = 'Header';
}
echo '<TITLE>冶金商务酒店(冶金宾馆)管理系统 - '. $page_title .'</TITLE>';
?>
   <LINK REL="stylesheet" TYPE="text/css" HREF="css/style.css">
 </HEAD>
 <BODY marginwidth="0" marginheight="0" BGCOLOR="#AAAAAA">
<?php
echo '<H2 CLASS="header">冶金商务酒店(冶金宾馆)管理系统 - ' . $page_title . '</H2>';
?>
