<?php
/**
设置全局变量
*/

//错误信息
$ERR = array();
$ERR['NO_BOARD'] = "暂无论坛";
$ERR['NO_TOPIC'] = "该论坛暂无主题帖";
$ERR['BOARD_NOT_EXIST'] = "板块不存在";
$ERR['TOPIC_NOT_EXIST'] = "帖子不存在";
$ERR['NO_PARAM'] = "请求参数有误";
$ERR['INVALID_PAGE'] = "无效页数";
$ERR['USER_NOT_EXIT'] = "用户不存在";
$ERR['NOT_LOGIN'] = "请登录后执行此操作";
$ERR['INVALID_USER'] = "用户名或密码错误";
$ERR['NONE_CONTENT'] = "发贴内容不能为空";
$ERR['OP_ILLEGAL'] = "非法操作";

//页面标题
$HTML_TITLE = array();
$HTML_TITLE['board'] = "论坛列表";
$HTML_TITLE['list'] = "帖子列表";
$HTML_TITLE['view'] = "查看、回复帖子";
$HTML_TITLE['userinfo'] = "用户信息";
$HTML_TITLE['mod'] = "修改帖子";

//功能选项
$FUNC = array();
$FUNC['reply'] = "回复";
$FUNC['modify'] = "修改";
$FUNC['delete'] = "删除";
$FUNC['newpost'] = "<a href=\"#fatie\">发贴</a>";
$FUNC['refresh'] = "刷新";
$FUNC['notlogin'] = "请<a href=\"login.php\">登录</a>后发贴或回复&nbsp;&nbsp;&nbsp;<a href=\"reg.html\">注册</a>";
$FUNC['login1'] = "登录";
$FUNC['login2'] = "用户名：<input type=\"text\" name=\"username\" size=\"15\"> 密码：<input type=\"password\" name=\"passwd\" size=\"15\">";
$FUNC['register'] = "注册";
$FUNC['user_name'] = "用户名";
$FUNC['header_link'] = "MyBBS 简易论坛系统";
$FUNC['footer_link'] = "版权所有&nbsp;&copy;&nbsp;2007&nbsp;&nbsp;";
?>

