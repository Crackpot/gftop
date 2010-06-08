python manage.py debugsqlshell

/usr/lib/python2.6/site-packages/registration/models.py:4: DeprecationWarning: the sha module is deprecated; use the hashlib module instead           
  import sha                                                               
Python 2.6.2 (r262:71600, Mar 29 2010, 15:30:23)
Type "copyright", "credits" or "license" for more information.

IPython 0.10 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object'. ?object also works, ?? prints more.

In [1]: from polls.models import Poll, Choice

In [2]: Poll.objects.all()
Out[2]: SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll` LIMIT 21

[]

In [3]: import datetime

In [4]: p = Poll(question="What's up?", pub_date=datetime.datetime.now())

In [5]: p.save()
INSERT INTO `polls_poll` (`question`,
                          `pub_date`)
VALUES (What's up?, 2010-06-06 12:48:37)

In [6]: p.id
Out[6]: 1L

In [7]: p.question
Out[7]: "What's up?"

In [8]: p.pub_date
Out[8]: datetime.datetime(2010, 6, 6, 12, 48, 37, 401058)

In [9]: p.pub_date = datetime.datetime(2007, 4, 1, 0, 0)

In [11]: p.save()
SELECT (1) AS `a`
FROM `polls_poll`
WHERE `polls_poll`.`id` = 1LIMIT 1

UPDATE `polls_poll`
SET `question` = What's up?, `pub_date` = 2007-04-01 00:00:00
WHERE `polls_poll`.`id` = 1

In [12]: Poll.objects.all()
Out[12]: SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll` LIMIT 21

[<Poll: Poll object>]

退出debugsqlshell重新进入

In [1]: from polls.models import Poll, Choice

In [2]: Poll.objects.all()
Out[2]: SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll` LIMIT 21

[<Poll: What's up?>]

In [3]: Poll.objects.filter(id=1)
Out[3]: SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`id` = 1LIMIT 21

[<Poll: What's up?>]

In [4]: Poll.objects.filter(id=1)[0]
SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`id` = 1LIMIT 1

Out[4]: <Poll: What's up?>

In [5]: Poll.objects.get(id=1)
SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`id` = 1

Out[5]: <Poll: What's up?>

In [6]: Poll.objects.filter(question__startswith='What')
Out[6]: SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`question` LIKE BINARY What%LIMIT 21

[<Poll: What's up?>]

In [7]: Poll.objects.get(pub_date__year=2007)
SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`pub_date` BETWEEN 2007-01-01 00:00:00
  and 2007-12-31 23:59:59.99

Out[7]: <Poll: What's up?>

In [8]: Poll.objects.get(pk=1)
SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`id` = 1

Out[8]: <Poll: What's up?>

In [9]: p = Poll.objects.get(pk=1)
SELECT `polls_poll`.`id`,
       `polls_poll`.`question`,
       `polls_poll`.`pub_date`
FROM `polls_poll`
WHERE `polls_poll`.`id` = 1


In [10]: p.was_published_today()
Out[10]: False

In [11]: p = Poll.objects.get(pk=1)
SELECT `polls_poll`.`id`,          
       `polls_poll`.`question`,    
       `polls_poll`.`pub_date`     
FROM `polls_poll`                  
WHERE `polls_poll`.`id` = 1        


In [12]: p.choice_set.all()
Out[12]: SELECT `polls_choice`.`id`,
       `polls_choice`.`poll_id`,    
       `polls_choice`.`choice`,     
       `polls_choice`.`votes`       
FROM `polls_choice`                 
WHERE `polls_choice`.`poll_id` = 1LIMIT 21

[]

In [13]: p.choice_set.create(choice='Not much', votes = 0)
INSERT INTO `polls_choice` (`poll_id`,
                            `choice`,
                            `votes`)
VALUES (1, Not much,
               0)

Out[13]: <Choice: Not much>


In [14]: p.choice_set.create(choice='The sky', votes = 0)
INSERT INTO `polls_choice` (`poll_id`,
                            `choice`,
                            `votes`)
VALUES (1,
        The sky,
        0)

Out[14]: <Choice: The sky>

In [15]: c = p.choice_set.create(choice='Just hacking again', votes = 0)
INSERT INTO `polls_choice` (`poll_id`,
                            `choice`,
                            `votes`)
VALUES (1,
        Just hacking again,
                     0)

In [16]: c.poll
Out[16]: <Poll: What's up?>

In [17]: p.choice_set.count()
SELECT COUNT(*)
FROM `polls_choice`
WHERE `polls_choice`.`poll_id` = 1

Out[17]: 3

In [18]: Choice.objects.filter(poll__pub_date__year = 2007)
Out[18]: SELECT `polls_choice`.`id`,
       `polls_choice`.`poll_id`,
       `polls_choice`.`choice`,
       `polls_choice`.`votes`
FROM `polls_choice`
INNER JOIN `polls_poll` ON (`polls_choice`.`poll_id` = `polls_poll`.`id`)
WHERE `polls_poll`.`pub_date` BETWEEN 2007-01-01 00:00:00
  and 2007-12-31 23:59:59.99LIMIT 21

[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

>>> c = p.choice_set.filter(choice__startswith='Just hacking')
>>> c.delete()
