<?php
//�����������ҳ��Ĺ���ʱ��(�ù��ʱ�׼ʱ���ʾ)��ֻҪ���Ѿ���ȥ�����ڼ��ɡ�
header("Expires: Mon, 26 Jul 1970 05:00:00 GMT");
//�����������ҳ�������������(�ù��ʱ�׼ʱ���ʾ)Ҳ���ǵ��죬Ŀ�ľ���ǿ���������ȡ��������
header("Last-Modified: ".gmdate("D,d M Y  H:i:s")."GMT"); 
header("Cache-Control: no-cache,must-revalidate");               //�����������ʹ�û���
//����ǰ�ķ���������,������HTTP1.0Э��
header("Pragma: no-cache"); 
header("Content-type: application/file");                        //���MIME����
header("Content-Length: 2850");                                  //�ļ�����
header("Accept-Ranges: bytes");                                  //���ܵķ�Χ��λ
header("Content-Disposition: attachment;filename=afilename");    //ȱʡʱ�ļ�����Ի����е��ļ�����
?>
