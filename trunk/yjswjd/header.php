<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
 "http://www.w3.org/TR/html4/loose.dtd">
<HTML xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
 <HEAD>
   <LINK REL="stylesheet" TYPE="text/css" HREF="css/qqList.css">
   <SCRIPT TYPE="text/javascript" SRC="js/qqConsult.js"></SCRIPT>
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<?php
if (!isset($page_title)) {
  $page_title = 'Header';
}
echo '<TITLE>冶金商务酒店※冶金宾馆连锁 - ' . $page_title . '</TITLE>';
?>
   <LINK REL="stylesheet" TYPE="text/css" HREF="css/style.css">
 </HEAD>
 <BODY BGCOLOR="#FFFFFF">
   <TABLE WIDTH="789" ALIGN="center" BORDER="0">
     <TR>
       <TD WIDTH="255" ALIGN="left" CELLPADDING="0" BGCOLOR="#FFFFFF">
         <A HREF="./"><IMG SRC="images/logo.gif" WIDTH="230" HEIGHT="91" ALT="冶金商务酒店(冶金宾馆)logo"></A>
       </TD>
       <TD WIDTH="528" VALIGN="bottom">
         <TABLE WIDTH="100%" HEIGHT="85" BORDER="0" CELLPADDING="0">
           <TR>
             <TD>
               <TABLE WIDTH="100%" HEIGHT="20" BORDER="0" CELLPADDING="0">
                 <TR>
                   <TD HEIGHT="20" ALIGN="right" VALIGN="middle" BACKGROUND="images/to.gif">
                     <A CLASS="navigation" HREF="CheckOrder.php" TARGET="_blank">订单查询</A>&nbsp;
                     <A CLASS="navigation" id="AddToMyFav" TITLE="添加到您的收藏夹，以便下次访问！" HREF="javascript:void(0)" ONCLICK="window.external.addFavorite(location.href,document.title)">加为收藏</A>&nbsp;
                     <A CLASS="navigation" TITLE="设为首页，下次打开时自动打开！" HREF="javascript:void(0)" ONCLICK="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.yj-hotel.com/');">设为首页</A>
                   </TD>
                 </TR>
               </TABLE>
             </TD>
           </TR>
           <TR>
             <TD HEIGHT="63" ALIGN="left" VALIGN="bottom">
               <IMG WIDTH="287" HEIGHT="33" SRC="images/adfont.gif" ALT="自然时尚，用心服务">
                 <TABLE WIDTH="100%" HEIGHT="30" BORDER="0" ALIGN="center" CELLPADDING="0">
                   <TR>
                     <TD BACKGROUND="images/navigation.gif" STYLE="color:#FFFFFF">
                       <TABLE WIDTH="100%" HEIGHT="27" BORDER="0" ALIGN="center" CELLPADDING="0">
                         <TR>
                           <TD>
                             &nbsp;&nbsp;
                             <A CLASS="navigation" HREF="index.php">首&nbsp;&nbsp;页</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="order.php">酒店预订</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="user.php">会员中心</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="leaveMessage.php">在线留言</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="job.php">工作机会</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="customerService.php">客服中心</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="about.php">关于我们</A>&nbsp;|&nbsp;
                             <A CLASS="navigation" HREF="bbs">冶金论坛</A>
                           </TD>
                         </TR>
                       </TABLE>
                     </TD>
                   </TR>
                 </TABLE>
             </TD>
           </TR>
         </TABLE>
       </TD>
     </TR>
   </TABLE>
