<?php
require_once("xajax/xajax.inc.php");

$xajax = new xajax();       //实例化xajax对象

//$xajax->debugOn();        //打开ajax调试功能

//注册一个xajax调用的php函数名（与javascript中的函数名xajax_showOutput相对应）
$xajax->registerFunction("showOutput");

//编写上面已经注册的php函数，在此函数中用xajaxResponse对象来返回XML指令集
function showOutput()
{
    $testResponse = new xajaxResponse();
    $testResponse->addAlert("Hello");
    
    $testResponse2 = new xajaxResponse();
    $testResponse2->loadXML($testResponse->getXML());
    $testResponse2->addReplace("this", "is", "a", "replacement");
    $testResponseOutput = htmlspecialchars($testResponse2->getXML());    
    
    $objResponse = new xajaxResponse();
    
    //使用xajaxResponse对象的addAssign方法添加XML指令，
    //该指令将id为submittedDiv的元素的innerHTML属性更新为$testResponseOutput
    $objResponse->addAssign("submittedDiv", "innerHTML", $testResponseOutput);
    return $objResponse;
}

$xajax->processRequests();  //在脚本传送出任何东西前，xajax都要处理所有请求
?>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>18-6.php - xajaxResponse Test</title>
<?php

//这代码使xajax对象可以生成所必需的JavaScript
$xajax->printJavascript("xajax/")
?>
</head>
<body>

<!-- 在这里调用 -->
<p><div onclick="xajax_showOutput();"> 点击这里显示响应XML </div></p>
<div id="submittedDiv">这里将被响应的XML指令所替换</div>

</body>
</html>