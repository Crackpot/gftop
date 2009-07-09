<?php
require_once("xajax/xajax.inc.php");

$xajax = new xajax();       //ʵ����xajax����

//$xajax->debugOn();        //��ajax���Թ���

//ע��һ��xajax���õ�php����������javascript�еĺ�����xajax_showOutput���Ӧ��
$xajax->registerFunction("showOutput");

//��д�����Ѿ�ע���php�������ڴ˺�������xajaxResponse����������XMLָ�
function showOutput()
{
    $testResponse = new xajaxResponse();
    $testResponse->addAlert("Hello");
    
    $testResponse2 = new xajaxResponse();
    $testResponse2->loadXML($testResponse->getXML());
    $testResponse2->addReplace("this", "is", "a", "replacement");
    $testResponseOutput = htmlspecialchars($testResponse2->getXML());    
    
    $objResponse = new xajaxResponse();
    
    //ʹ��xajaxResponse�����addAssign�������XMLָ�
    //��ָ�idΪsubmittedDiv��Ԫ�ص�innerHTML���Ը���Ϊ$testResponseOutput
    $objResponse->addAssign("submittedDiv", "innerHTML", $testResponseOutput);
    return $objResponse;
}

$xajax->processRequests();  //�ڽű����ͳ��κζ���ǰ��xajax��Ҫ������������
?>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>18-6.php - xajaxResponse Test</title>
<?php

//�����ʹxajax������������������JavaScript
$xajax->printJavascript("xajax/")
?>
</head>
<body>

<!-- ��������� -->
<p><div onclick="xajax_showOutput();"> ���������ʾ��ӦXML </div></p>
<div id="submittedDiv">���ｫ����Ӧ��XMLָ�����滻</div>

</body>
</html>