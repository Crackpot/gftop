DROP TABLE IF EXISTS users;
create table users(
user_id int(10) unsigned NOT NULL auto_increment,
user_name varchar(20) NOT NULL default '',
passwd varchar(32) NOT NULL default '',
email varchar(80) NOT NULL default '',
reg_ip varchar(16) NOT NULL default '',
reg_time datetime NOT NULL default '0000-00-00 00:00:00',
login_ip varchar(16) NOT NULL default '',
login_time datetime NOT NULL default '0000-00-00 00:00:00',
come_from varchar(12) NOT NULL default '',
PRIMARY KEY user_id(user_id)
);

DROP TABLE IF EXISTS boards;
create table boards(
id tinyint(2) unsigned NOT NULL auto_increment,
board_name varchar(50) NOT NULL default '',
board_desc varchar(100) NOT NULL default '',
build_time datetime NOT NULL default '0000-00-00 00:00:00',
PRIMARY KEY id(id)
);

DROP TABLE IF EXISTS topics;
create table topics(
id int(6) unsigned NOT NULL auto_increment,
bid tinyint(2) unsigned NOT NULL default '0',
fid int(6) unsigned NOT NULL default '0',
user_id int(5) unsigned NOT NULL default '0',
title varchar(50) NOT NULL default '',
content text NOT NULL default '',
post_time datetime NOT NULL default '0000-00-00 00:00:00',
edit_time datetime NOT NULL default '0000-00-00 00:00:00',
reply_time datetime NOT NULL default '0000-00-00 00:00:00',
PRIMARY KEY id(id),
KEY bid(bid),
KEY fid(fid),
KEY user_id(user_id),
KEY post_time(post_time)
);

DROP TABLE IF EXISTS admins;
create table admins(
id int(2) unsigned NOT NULL auto_increment,
name varchar(50) NOT NULL default '',
passwd varchar(32) NOT NULL default '',
email varchar(50) NOT NULL default '',
login_time datetime NOT NULL default '0000-00-00 00:00:00',
PRIMARY KEY id(id)
);