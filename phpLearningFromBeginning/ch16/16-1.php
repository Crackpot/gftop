<?php
class Exception
{
    protected $message = 'Unknown exception';   // �쳣��Ϣ
    protected $code = 0;                        // �û��Զ����쳣����
    protected $file;                            // �����쳣���ļ���
    protected $line;                            // �����쳣�Ĵ����к�

    function __construct($message = null, $code = 0);

    final function getMessage();                // �����쳣��Ϣ
    final function getCode();                   // �����쳣����
    final function getFile();                   // ���ط����쳣���ļ���
    final function getLine();                   // ���ط����쳣�Ĵ����к�
    final function getTrace();                  // backtrace() ����
    final function getTraceAsString();          // �Ѹ�ɻ����ַ����� getTrace() ��Ϣ

    function __toString();                      // ��������ַ���
}
?>