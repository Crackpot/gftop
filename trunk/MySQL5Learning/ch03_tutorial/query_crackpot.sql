create database if not exists `crackpot` default character set utf8 collate utf8_general_ci;/*不存在就建立*/
alter database `crackpot` default character set utf8 collate utf8_general_ci;
use crackpot;
drop table if exists `pet`;/*存在就删除*/
create table pet(
        name varchar(20),
        owner varchar(20),
        species varchar(20),
        sex char(1),
        birth date,
        death date);
insert into pet values ('Puffball','Diane','hamster','f','1999-03-30',NULL);
delete from pet;/*删除表中的所有数据*/
truncate pet;/*清空全表*/
insert into pet values
    ('Fluffy','Harold','cat','f','1993-02-04',NULL),
    ('Claws','Gwen','cat','m','1994-03-17',NULL),
    ('Buffy','Harold','dog','f','1989-05-13',NULL),
    ('Fang','Benny','dog','m','1990-08-27',NULL),
    ('Bowser','Diane','dog','m','1979-08-31','1995-07-29'),
    ('Chirpy','Gwen','bird','f','1998-09-11',NULL),
    ('Whistler','Gwen','bird',NULL,'1997-12-09',NULL),
    ('Slim','Benny','snake','m','1996-04-29',NULL);

update pet set birth = '1989-08-31' where name = 'Bowser';/*修改错误的生日项*/
insert into pet values ('Puffball','Diane','hamster','f','1999-03-30',NULL);

select * from pet where name = 'Bowser';/*宠物名字*/
select * from pet where birth > '1998-1-1';/*生日*/
select * from pet where species = 'dog' and sex = 'f';/*母狗*/
select * from pet where species = 'snake' or species = 'bird';/*蛇和鸟*/
select * from pet where (species = 'cat' and sex = 'm') or (species = 'dog' and sex = 'f');/*公猫和母狗*/
select name, birth from pet;/*名字，生日*/
select owner from pet;/*主人*/
select distinct owner from pet;/*不同的主人*/
select name,species,birth from pet where species = 'dog' or species = 'cat';/*狗和猫*/
select name,birth from pet order by birth;/*生日，顺序*/
select name,birth from pet order by birth desc;/*生日，逆序*/
select name,species,birth from pet order by species, birth desc;/*物种和生日，逆序*/
/*要想确定每个宠物有多大，可以计算当前日期的年和出生日期之间的差。如果当前日期的日历年比出生日期早，则减去一年。以下查询显示了每个宠物的出生日期、当前日期和年龄数值的年数字。
YEAR()提取日期的年部分，RIGHT()提取日期的MM-DD (日历年)部分的最右面5个字符。比较MM-DD值的表达式部分的值一般为1或0，如果CURDATE()的年比birth的年早，则年份应减去1。整个表达式有些难懂，使用alias (age)来使输出的列标记更有意义。*/
select name,birth,curdate(),(year(curdate()) - year(birth)) - (right(curdate(),5) < right(birth,5)) as age from pet;
select name,birth,curdate(),(year(curdate()) - year(birth)) - (right(curdate(),5) < right(birth,5)) as age from pet order by age desc;/*计算出宠物的年龄，逆序*/
select name,birth,curdate(),(year(curdate()) - year(birth)) - (right(curdate(),5) < right(birth,5)) as age from pet order by name;/*算出年龄按名字排序*/
select name,birth,death,(year(death) - year(birth)) - (right(death,5) < right(birth,5)) as age from pet where death is not Null order by age;/*查询使用death IS NOT NULL而非death != NULL，因为NULL是特殊的值，不能使用普通比较符来比较*/
/*如果你想要知道哪个动物下个月过生日，怎么办？对于这类计算，年和天是无关的，你只需要提取birth列的月份部分。MySQL提供几个日期部分的提取函数，例如YEAR( )、MONTH( )和DAYOFMONTH( )。在这里MONTH()是适合的函数。为了看它怎样工作，运行一个简单的查询，显示birth和MONTH(birth)的值：*/
select name,birth,month(birth) from pet;
/*找出下个月生日的动物也是容易的。假定当前月是4月，那么月值是4，你可以找在5月出生的动物 (5月)，方法是：*/
select name,birth from pet where month(birth)=5;/*如果当前月份是12月，就有点复杂了。你不能只把1加到月份数(12)上并寻找在13月出生的动物，因为没有这样的月份。相反，你应寻找在1月出生的动物(1月) 。*/
/*你甚至可以编写查询，不管当前月份是什么它都能工作。采用这种方法不必在查询中使用一个特定的月份，DATE_ADD( )允许在一个给定的日期上加上时间间隔。如果在NOW( )值上加上一个月，然后用MONTH()提取月份，结果产生生日所在月份：*/
insert into pet values ('Snooby','Crackpot','cat','m','2000-10-20',NULL);/*先添加一个10月生日的*/
select name,birth from pet where month(birth) = month(date_add(curdate(),interval 1 month));
/*完成该任务的另一个方法是加1以得出当前月份的下一个月(在使用取模函数(MOD)后，如果月份当前值是12，则“回滚”到值0)：*/
select name,birth from pet where month(birth)= mod(month(curdate()),12) + 1;

SELECT 1 = NULL, 1 <> NULL, 1 < NULL, 1 > NULL;/*NULL值很特殊*/
SELECT 1 IS NULL, 1 IS NOT NULL;/*使用IS NULL和IS NOT NULL操作符可以得到比较有意义的结果*/
SELECT 0 IS NULL, 0 IS NOT NULL, '' IS NULL, '' IS NOT NULL;


/*
	模式匹配
*/
select * from pet where name like 'b%';/*找出以"b"开头的名字*/
select * from pet where name like '%fy';/*找出以"fy"结尾的名字*/
select * from pet where name like '%w%';/*找出包含"w"的名字*/
select * from pet where name like '_____';/*找出正好包含5个字符的名字*/
/*由MySQL提供的模式匹配的其它类型是使用扩展正则表达式。当你对这类模式进行匹配测试时，使用REGEXP和NOT REGEXP操作符(或RLIKE和NOT RLIKE，它们是同义词)。 */
select * from pet where name regexp '^b';/*找出以" b"开头的名字*/
select * from pet where name regexp binary '^B';/*强制使regexp区分大小写，使用binary使其中一个字符串变成二进制字符串*/
select * from pet where name regexp 'fy$';/*找出以'fy'结尾的名字，使用'$'匹配名字的结尾*/
select * from pet where name regexp 'w';/*找出包含一个'w'的名字*/
select * from pet where name regexp '^.....$';/*找出正好包含5个字符的名字，使用'^'和'$'匹配名字的开始和结尾，和5个'.'实例在两者之间*/
select * from pet where name regexp '^.{5}';/*同样找出正好包含5个字符的名字，用'{n}'，'重复n次'来查询*/


/*
	计数行
*/
select count(*) from pet;/*计算表中的记录有多少行*/
select owner,count(*) from pet group by owner;/*检索每个主人拥有多少宠物，使用group by对每个owner的所有记录分组*/
select species,count(*) from pet group by species;/*检索每种动物的数量*/
select sex,count(*) from pet group by sex;/*每种性别的动物数量*/
select species,sex,count(*) from pet group by species,sex;/*种类和性别组合的动物数量*/
select species,sex,count(*) from pet where species = 'dog' or species = 'cat' group by species,sex;/*使用count()，不必检索整个表。如检索猫和狗雌雄各为多少*/
select species,sex,count(*) from pet where sex is not null group by species,sex;/*检索已知性别的按性别分类的动物数目*/


/*
继针对表pet操作的学习至此，需要用到一个以上的表。
pet表追踪你有哪个宠物。如果你想要记录其它相关信息，例如在他们一生中看兽医或何时后代出生，你需要另外的表。这张表应该像什么呢？需要：
它需要包含宠物名字以便你知道每个事件属于哪个动物。
需要一个日期以便你知道事件是什么时候发生的。
需要一个描述事件的字段。
如果你想要对事件进行分类，则需要一个事件类型字段。
 */
create table if not exists event(
    name varchar(20),
    date date,
    type varchar(15),
    remark varchar(255)
);
select pet.name,(year(date)-year(curdate()))-(right(date,5)<right(birth,5)) as age,remark from pet,event where pet.name = event.name and event.type = 'litter';/*当他们有了一窝小动物时，假定你想要找出每只宠物的年龄。我们前面看到了如何通过两个日期计算年龄。event表中有母亲的生产日期，但是为了计算母亲的年龄，你需要她的出生日期，存储在pet表中。说明查询需要两个表：*/
select p1.name,p1.sex,p2.name,p2.sex,p1.species from pet as p1,pet as p2 where p1.species = p2.species and p1.sex = 'f' and p2.sex = 'm';/*在宠物之中繁殖配偶，你可以用pet联结自身来进行相似种类的雄雌配对*/

/*
	3.6常用查询的例子
	用到表shop
*/

create table if not exists shop(
	article int(4) unsigned zerofill default '0000' not null,
	dealer	char(20)		 default ''	not null,
	price	double(16,2)		 default '0.00' not null,
	primary key(article,dealer));
truncate table shop;/*清空表*/
insert into shop values	(1,'A',3.45),(1,'B',3.99),(2,'A',10.99),(3,'B',1.45),(3,'C',1.69),(3,'D',1.25),(4,'D',19.95);
select * from shop;
select max(article) as article from shop;/*检索最大的物品号*/
select article,dealer,price from shop where price = (select max(price) from shop);/*检索最贵物品的编号、销售商和价格*/
select article,dealer,price from shop order by price desc limit 1;/*功能同上*/
select article,max(price) as price from shop group by article;/*检索每项物品的最高价格*/
select article,dealer,price from shop s1 where price=(select max(s2.price) from shop s2 where s1.article=s2.article);/*对每项物品，找出最贵价格的物品的经销商*/

