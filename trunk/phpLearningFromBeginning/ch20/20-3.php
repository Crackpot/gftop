<?php
include("./Smarty/libs/Smarty.class.php");  //包含smarty类文件 

$smarty = new Smarty();                          //建立smarty实例对象$smarty 
$smarty->template_dir = "./templates";           //设置模板目录 
$smarty->compile_dir = "./templates_c";          //设置编译目录 

$smarty->left_delimiter = "{";                   //设定左右边界符为{}，Smarty推荐使用的是<{}>
$smarty->right_delimiter = "}"; 

$smarty->assign("name", "Smarty");                //进行模板变量替换
$smarty->assign("page_title", "Smarty的使用");    //进行模板变量替换 

$smarty->display("20-2.tpl");                     //编译并显示位于./templates下的20-2.tpl模板 
?>