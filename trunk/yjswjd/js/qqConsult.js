var base_url = "/";
var img_src = "images/qqbox.gif";
var w_body = 95;
var h_body = 100;
var w_cursor = 20;
var h_cursor = 20;
var l_cursor = 160;
var t_cursor = 0;

document.writeln("  <div id=\"ShowQQ\" style=\"position:absolute; z-index: 100; font-size:12px;\"> ");
document.writeln("    <div id=\"ImgLayer\" style=\"position:absolute; z-index:1; left: 0px;\"> ");
document.writeln("<table width='95' height='100' background='images/qqbox.gif' border='0' cellspacing='0' cellpadding='0'>");
document.writeln("<tr><td height='20'></td></tr>");
document.writeln("<tr><td height='10' id='qqlist' style='align=\"center\"'>")
document.writeln("<a href='tencent://message/?uin=361660207&Menu=no' title='点击咨询'><img src='http://wpa.qq.com/pa?p=1:361660207:4' align='absmiddle'/>361660207</a></td></tr>")
document.writeln("<tr><td><a href='tencent://message/?uin=26510132&Menu=no'><img src='http://wpa.qq.com/pa?p=1:26510132:4' align='absmiddle'/>26510132&nbsp;&nbsp;</a></td></tr>")
document.writeln("</table>");
document.writeln("</div>");
document.writeln("</div>");

var QQfrm = ( document.compatMode.toLowerCase()=="css1compat" ) ? document.documentElement : document.body;
var QQst = document.getElementById("ShowQQ").style;
QQst.top = ( QQfrm.clientHeight - h_body -150 ) + "px";
QQst.left = ( QQfrm.clientWidth - w_body -12 ) + "px";
function moveR() {
    QQst.top = ( QQfrm.scrollTop + QQfrm.clientHeight - h_body - 150 ) + "px";
    QQst.left = ( QQfrm.scrollLeft + QQfrm.clientWidth - w_body -12 ) + "px";
}
setInterval("moveR();", 80);
function CloseIt(){
    QQst.display='none';
}
