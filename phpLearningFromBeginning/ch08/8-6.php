<?php
//告诉浏览器此页面的过期时间(用国际标准时间表示)，只要是已经过去的日期即可。
header("Expires: Mon, 26 Jul 1970 05:00:00 GMT");
//告诉浏览器此页面的最后更新日期(用国际标准时间表示)也就是当天，目的就是强迫浏览器获取最新内容
header("Last-Modified: ".gmdate("D,d M Y  H:i:s")."GMT"); 
header("Cache-Control: no-cache,must-revalidate");               //告诉浏览器不使用缓存
//与以前的服务器兼容,即兼容HTTP1.0协议
header("Pragma: no-cache"); 
header("Content-type: application/file");                        //输出MIME类型
header("Content-Length: 2850");                                  //文件长度
header("Accept-Ranges: bytes");                                  //接受的范围单位
header("Content-Disposition: attachment;filename=afilename");    //缺省时文件保存对话框中的文件名称
?>
