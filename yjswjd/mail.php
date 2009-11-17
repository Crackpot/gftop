<?php
//发件人
$from = "发件人 ";
//收件人
$email= "xxx@xxx.com";
//邮件主题
$subject= "邮件主题";
//HTML格式页面
$attachment= "email.htm";
$boundary= uniqid("");
$headers= "From: $from
  Mime-Version: 1.0
  Content-Type: multipart/mixed;
boundary=".$boundary."
  ";
//打开HTML文件
$fp = fopen($attachment, "r");
//把整个文件读入一个变量
$read= fread($fp, filesize($attachment));
//收件人名称替换，一般用于群发
//$read= str_replace("***", $value[username], $read);
//好，现在变量$read中保存的是包含整个文件内容的文本块。
//现在我们要把这个文本块转换成邮件程序可以读懂的格式
//我们用base64方法把它编码
$read= base64_encode($read);
//现在我们有一个用base64方法编码的长字符串。
//下一件事是要把这个长字符串切成由每行76个字符组成的小块
$read= chunk_split($read);
$body= "--$boundary
  Content-Type: text/html; charset=GB2312
  Content-Transfer-Encoding: base64
  $read
  --$boundary";
//发送MAIL
mail($email, $subject, $body, $headers);
?>
