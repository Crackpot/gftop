<?php
include("./Smarty/libs/Smarty.class.php");  //����smarty���ļ� 

$smarty = new Smarty();                          //����smartyʵ������$smarty 
$smarty->template_dir = "./templates";           //����ģ��Ŀ¼ 
$smarty->compile_dir = "./templates_c";          //���ñ���Ŀ¼ 

$smarty->left_delimiter = "{";                   //�趨���ұ߽��Ϊ{}��Smarty�Ƽ�ʹ�õ���<{}>
$smarty->right_delimiter = "}"; 

$smarty->assign("name", "Smarty");                //����ģ������滻
$smarty->assign("page_title", "Smarty��ʹ��");    //����ģ������滻 

$smarty->display("20-2.tpl");                     //���벢��ʾλ��./templates�µ�20-2.tplģ�� 
?>