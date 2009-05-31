--
-- PostgreSQL database dump
--

-- Started on 2009-05-31 12:31:02 CST

SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- TOC entry 1752 (class 0 OID 0)
-- Dependencies: 1299
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- TOC entry 1753 (class 0 OID 0)
-- Dependencies: 1318
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 1754 (class 0 OID 0)
-- Dependencies: 1303
-- Name: auth_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_message_id_seq', 1, false);


--
-- TOC entry 1755 (class 0 OID 0)
-- Dependencies: 1297
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_permission_id_seq', 33, true);


--
-- TOC entry 1756 (class 0 OID 0)
-- Dependencies: 1320
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- TOC entry 1757 (class 0 OID 0)
-- Dependencies: 1301
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- TOC entry 1758 (class 0 OID 0)
-- Dependencies: 1322
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 1759 (class 0 OID 0)
-- Dependencies: 1314
-- Name: books_author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('books_author_id_seq', 1, false);


--
-- TOC entry 1760 (class 0 OID 0)
-- Dependencies: 1324
-- Name: books_book_authors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('books_book_authors_id_seq', 1, false);


--
-- TOC entry 1761 (class 0 OID 0)
-- Dependencies: 1316
-- Name: books_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('books_book_id_seq', 1, false);


--
-- TOC entry 1762 (class 0 OID 0)
-- Dependencies: 1312
-- Name: books_publisher_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('books_publisher_id_seq', 1, false);


--
-- TOC entry 1763 (class 0 OID 0)
-- Dependencies: 1310
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- TOC entry 1764 (class 0 OID 0)
-- Dependencies: 1305
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('django_content_type_id_seq', 11, true);


--
-- TOC entry 1765 (class 0 OID 0)
-- Dependencies: 1308
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: crackpot
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- TOC entry 1736 (class 0 OID 17969)
-- Dependencies: 1300
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- TOC entry 1746 (class 0 OID 18077)
-- Dependencies: 1319
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- TOC entry 1738 (class 0 OID 17987)
-- Dependencies: 1304
-- Data for Name: auth_message; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_message (id, user_id, message) FROM stdin;
\.


--
-- TOC entry 1735 (class 0 OID 17960)
-- Dependencies: 1298
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add message	4	add_message
11	Can change message	4	change_message
12	Can delete message	4	delete_message
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add log entry	8	add_logentry
23	Can change log entry	8	change_logentry
24	Can delete log entry	8	delete_logentry
25	Can add publisher	9	add_publisher
26	Can change publisher	9	change_publisher
27	Can delete publisher	9	delete_publisher
28	Can add author	10	add_author
29	Can change author	10	change_author
30	Can delete author	10	delete_author
31	Can add book	11	add_book
32	Can change book	11	change_book
33	Can delete book	11	delete_book
\.


--
-- TOC entry 1737 (class 0 OID 17978)
-- Dependencies: 1302
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_user (id, username, first_name, last_name, email, "password", is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
1	crackpot			gaofeitop@gmail.com	sha1$454ae$b2d81bc120a0d6197863525b504ee53662cc113b	t	t	t	2009-05-31 11:49:32.262354+08	2009-05-31 11:47:47.219147+08
\.


--
-- TOC entry 1747 (class 0 OID 18096)
-- Dependencies: 1321
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- TOC entry 1748 (class 0 OID 18115)
-- Dependencies: 1323
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 1744 (class 0 OID 18058)
-- Dependencies: 1315
-- Data for Name: books_author; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY books_author (id, salutation, first_name, last_name, email, headshot) FROM stdin;
2	crackpot	飞	高	gaofeitop@gmail.com	/home/workspace/gftop/mysite/books/headshots/1_.jpg
3	张三	三	张	zhangsan@gmail.com	/home/workspace/gftop/mysite/books/headshots/2.jpg
\.


--
-- TOC entry 1745 (class 0 OID 18065)
-- Dependencies: 1317
-- Data for Name: books_book; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY books_book (id, title, publisher_id, publication_date) FROM stdin;
1	俄语入门	4	2009-05-31
2	dddddddddddddddddddddddddddddddddddddddddddddddddddddd	1	2009-05-31
\.


--
-- TOC entry 1749 (class 0 OID 18134)
-- Dependencies: 1325
-- Data for Name: books_book_authors; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY books_book_authors (id, book_id, author_id) FROM stdin;
1	1	2
2	2	3
\.


--
-- TOC entry 1743 (class 0 OID 18051)
-- Dependencies: 1313
-- Data for Name: books_publisher; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY books_publisher (id, name, address, city, state_province, country, website) FROM stdin;
1	Addison-Wesley	75 Arlington Street	Boston	MA	U.S.A.	http://www.apress.com/
3	Apress Publishing	2855 Telegraph Ave.	Berkeley	CA	U.S.A.	http://www.apress.com/
2	O'Reilly	10 Fawcett St.	Cambridge	MA	U.S.A.	http://www.oreilly.com/
4	南昌出版社	江西南昌	南昌	江西	中国	http://www.tudou.com/
\.


--
-- TOC entry 1742 (class 0 OID 18030)
-- Dependencies: 1311
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2009-05-31 12:03:56.869764+08	1	9	1	Addison-Wesley	2	已修改 website 。
2	2009-05-31 12:04:02.538298+08	1	9	3	Apress Publishing	2	没有字段被修改。
3	2009-05-31 12:04:07.446647+08	1	9	3	Apress Publishing	2	没有字段被修改。
4	2009-05-31 12:04:12.976641+08	1	9	2	O'Reilly	2	没有字段被修改。
5	2009-05-31 12:04:17.772449+08	1	9	4	南昌出版社	2	没有字段被修改。
6	2009-05-31 12:27:11.332503+08	1	10	2	飞 高	1	
7	2009-05-31 12:27:45.537469+08	1	10	3	三 张	1	
8	2009-05-31 12:28:15.919924+08	1	11	1	俄语入门	1	
9	2009-05-31 12:28:33.964443+08	1	11	2	dddddddddddddddddddddddddddddddddddddddddddddddddddddd	1	
\.


--
-- TOC entry 1739 (class 0 OID 18002)
-- Dependencies: 1306
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	message	auth	message
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	log entry	admin	logentry
9	publisher	books	publisher
10	author	books	author
11	book	books	book
\.


--
-- TOC entry 1740 (class 0 OID 18014)
-- Dependencies: 1307
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
6b691451a159001d87897a2aad6abc2f	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwF1LjZiODA4Y2VmZGFhN2I5ZDEyYWM1\nOTRmZTlmMmYxMjYw\n	2009-06-14 11:49:32.288894+08
599d1648a41b167e9030497fba651bd4	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwF1LjZiODA4Y2VmZGFhN2I5ZDEyYWM1\nOTRmZTlmMmYxMjYw\n	2009-06-11 18:30:20.027514+08
\.


--
-- TOC entry 1741 (class 0 OID 18023)
-- Dependencies: 1309
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: crackpot
--

COPY django_site (id, "domain", name) FROM stdin;
1	example.com	example.com
\.


-- Completed on 2009-05-31 12:31:02 CST

--
-- PostgreSQL database dump complete
--

