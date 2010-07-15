# -*- coding: utf-8 -*-
"""
Created on 2010-6-13

@author: fangshi
"""

from __future__ import division
import time
        
def read_cpu_usage(): 
    """解析 /proc/stat文件
    
    """ 
    lines = open("/proc/stat").readlines() 
    for line in lines: 
        #print "l = %s" % line 
        l = line.split() 
        if len(l) < 5: 
            continue 
        if l[0].startswith('cpu'): 
            return l;
    return {} 

def getCup_info():
    """解析cpu数据信息，返回cpu 用户占用比例
    
    """
    cpustr = read_cpu_usage()
    #cpu usage=[(user_2 +sys_2+nice_2) - (user_1 + sys_1+nice_1)]/(total_2 - total_1)*100 
    usni1 = long(cpustr[1]) + long(cpustr[2]) + long(cpustr[3]) + long(cpustr[5]) + long(cpustr[6]) + long(cpustr[7]) + long(cpustr[4])
    usn1 = long(cpustr[1]) + long(cpustr[2]) + long(cpustr[3])
    
    time.sleep(2)
    cpustr = read_cpu_usage()
    usni2 = long(cpustr[1]) + long(cpustr[2]) + float(cpustr[3]) + long(cpustr[5]) + long(cpustr[6]) + long(cpustr[7]) + long(cpustr[4])
    usn2 = long(cpustr[1]) + long(cpustr[2]) + long(cpustr[3])
    #usni2=long(cpustr[1])+long(cpustr[2])+float(cpustr[3])+long(cpustr[4])
    
    cpuper = (usn2 - usn1) / (usni2 - usni1)
    #s = "CPUTotal used percent =%.4f \r\n" % (cpuper * 100)
    return cpuper        
        
def getMem_info():
    """解析proc/meminfo文件，返回内存总量和内存空闲量
    
    """
    filename = '/proc/meminfo'
    files = open(filename, 'r')
    try:
        info_list = []
        for line in files.readlines():
            s = line.lstrip()
            info_list.append(s)
        mtotal_info_list = info_list[0].split(' ')
        mtotal = filter(lambda x:x != '', mtotal_info_list)[1]   
        mfree_info_list = info_list[1].split(' ')
        mfree = filter(lambda x:x != '', mfree_info_list)[1]   
        return mtotal,mfree
    except:
        return 0, 0
    finally:
        files.close()
        
def getNet_info(dev):
    """解析/proc/net/dev，获取网络分析数据
    @param dev:
    @type dev:
    """
    filename = '/proc/net/dev'
    files = open(filename, 'r')
    try:
        info_list = []
        for line in files.readlines():
            s = line.lstrip()
            if s.startswith(dev):
                info_list.append(s)
                
        if info_list != []:
            for eth_item in info_list:
                date = eth_item.split(' ')
                temp = filter(lambda x:x != '', date)
                getdate = temp[0].split(':')[-1]
                putdate = temp[8]
                return int(getdate), int(putdate)
    except:
        return 0, 0
    finally:
        files.close()
        
def save_monitor_data(mtotal, mfree, getdate, putdate, cpu_use_rate, mem_use_rate, net_post_rate,net_rec_rate):
    """保存分析数据到数据库
    
    """
    try:
        import MySQLdb  
        conn = MySQLdb.connect(host="xxx", user="xxx", passwd="xxx", db="xxx")  
        cursor = conn.cursor()  
        cursor.execute("SET NAMES utf8")  
        sql = 'insert into srt_server_info (mtotal, mfree, recivedata, postdata, cpu_user_rate, mem_user_rate, net_post_rate,net_rec_rate) values(%s,%s,%s,%s,%s,%s,%s,%s)' % \
        (mtotal, mfree, getdate, putdate, cpu_use_rate, mem_use_rate, net_post_rate,net_rec_rate)
        cursor.execute(sql)  
        cursor.close()
        print 'succress'
    except:
        raise

getdate_1 = 0
putdate_1 = 0

if __name__ == '__main__':
    time_difine = 1 * 60
    while True:
        dev = 'eth0'
        getdate, putdate = getNet_info(dev)
        cpu_use_rate = getCup_info()
        mtotal, mfree = getMem_info()        
        mem_use_rate = (int(mtotal) - int(mfree)) / int(mtotal)
        
        if getdate_1 == 0 or putdate_1 == 0 :
            getdate_1 = getdate
            putdate_1 = putdate  
            continue
        else:
            net_rec_rate = (int(getdate) - int(getdate_1)) / (time_difine) 
            net_post_rate = (int(putdate) - int(putdate_1)) / (time_difine) 
                  
        getdate_1 = getdate
        putdate_1 = putdate   
                                
        print '%-5s get : %-10s ' % (dev, getdate) 
        print '%-5s post: %-10s ' % (dev, putdate) 
        print 'mtotal :%s' % mtotal
        print 'mfree  :%s' % mfree
        print 'cpu_use_rate :', cpu_use_rate
        print 'mem_use_rate :', mem_use_rate
        print 'net_rec_rate :', net_rec_rate
        print 'net_post_rate:', net_post_rate
        print '*' * 40
       
        #save_monitor_data(mtotal, mfree, getdate, putdate, cpu_use_rate, mem_use_rate, net_post_rate,net_rec_rate)
        time.sleep(time_difine)
    
    
"""
CREATE TABLE  `opensips`.`srt_server_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ctime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mfree` int(11) NOT NULL,
  `recivedata` bigint(20) NOT NULL,
  `postdata` bigint(20) NOT NULL,
  `cpu_user_rate` float DEFAULT 0,
  `mem_user_rate` float DEFAULT 0,
  `net_rec_rate` float DEFAULT 0,
  `net_post_rate` float DEFAULT 0,
  `mtotal` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=56 DEFAULT CHARSET=latin1
   
""" 