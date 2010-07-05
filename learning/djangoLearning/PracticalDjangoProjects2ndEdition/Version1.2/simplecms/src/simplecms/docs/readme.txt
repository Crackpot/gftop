141页
准备完成weblog

crackpot@linux-Crackpot:/home/workspace/gftop/learning/djangoLearning/PracticalDjangoProjects2ndEdition/Version1.2/simplecms/src/simplecms> python manage.py test                   
Creating test database 'default'...                                                       
Creating table auth_permission                                                            
Creating table auth_group_permissions                                                     
Creating table auth_group                                                                 
Creating table auth_user_user_permissions                                                 
Creating table auth_user_groups                                                           
Creating table auth_user                                                                  
Creating table auth_message                                                               
Creating table django_content_type                                                        
Creating table django_session                                                             
Creating table django_site                                                                
Creating table django_flatpage_sites                                                      
Creating table django_flatpage                                                            
Creating table django_admin_log                                                           
Creating table cab_language                                                               
Creating table cab_snippet                                                                
Creating table cab_bookmark                                                               
Creating table search_searchkeyword                                                       
Creating table coltrane_category                                                          
Creating table coltrane_entry_categories                                                  
Creating table coltrane_entry                                                             
Creating table coltrane_link                                                              
Creating table tagging_tag                                                                
Creating table tagging_taggeditem                                                         
Creating table django_comments                                                            
Creating table django_comment_flags                                                       
Installing index for auth.Permission model                                                
Installing index for auth.Group_permissions model                                         
Installing index for auth.User_user_permissions model                                     
Installing index for auth.User_groups model                                               
Installing index for auth.Message model                                                   
Installing index for flatpages.FlatPage_sites model                                       
Installing index for flatpages.FlatPage model                                             
Installing index for admin.LogEntry model                                                 
Installing index for cab.Snippet model                                                    
Installing index for cab.Bookmark model                                                   
Installing index for search.SearchKeyword model                                           
Installing index for coltrane.Entry_categories model                                      
Installing index for coltrane.Entry model                                                 
Installing index for coltrane.Link model                                                  
Installing index for tagging.TaggedItem model                                             
Installing index for comments.Comment model                                               
Installing index for comments.CommentFlag model                                           
No fixtures found.                                                                        
...........................................................E.......................E............................E......................E..............................              
======================================================================                    
ERROR: test_middleware_disabled_anon_user (django.contrib.messages.tests.cookie.CookieTest)                                                                                         
----------------------------------------------------------------------                    
Traceback (most recent call last):                                                        
  File "/usr/lib/python2.6/site-packages/django/contrib/messages/tests/base.py", line 257, in test_middleware_disabled_anon_user                                                    
    data, follow=True)                                                                    
  File "/usr/lib/python2.6/unittest.py", line 336, in failUnlessRaises                    
    callableObj(*args, **kwargs)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 322, in post        
    response = self.request(**r)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 230, in request     
    response = self.handler(environ)                                                      
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 74, in __call__     
    response = self.get_response(request)                                                 
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 142, in get_response                                                                                   
    return self.handle_uncaught_exception(request, resolver, exc_info)                    
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 181, in handle_uncaught_exception                                                                      
    return callback(request, **param_dict)                                                
  File "/usr/lib/python2.6/site-packages/django/views/defaults.py", line 24, in server_error                                                                                        
    return http.HttpResponseServerError(t.render(Context({})))                            
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 173, in render
    return self._render(context)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)                                                  
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))                                          
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node                                                                                         
    result = node.render(context)                                                         
  File "/usr/lib/python2.6/site-packages/django/template/loader_tags.py", line 125, in render                                                                                       
    return compiled_parent._render(context)                                               
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)                                                  
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))                                          
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node                                                                                         
    result = node.render(context)                                                         
  File "/usr/lib/python2.6/site-packages/django/template/defaulttags.py", line 378, in render                                                                                       
    raise e                                                                               
TemplateSyntaxError: Caught NoReverseMatch while rendering: Reverse for 'cab_snippet_list' with arguments '()' and keyword arguments '{}' not found.                                

======================================================================
ERROR: test_middleware_disabled_anon_user (django.contrib.messages.tests.fallback.FallbackTest)                                                                                     
----------------------------------------------------------------------                    
Traceback (most recent call last):                                                        
  File "/usr/lib/python2.6/site-packages/django/contrib/messages/tests/base.py", line 257, in test_middleware_disabled_anon_user                                                    
    data, follow=True)                                                                    
  File "/usr/lib/python2.6/unittest.py", line 336, in failUnlessRaises                    
    callableObj(*args, **kwargs)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 322, in post        
    response = self.request(**r)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 230, in request     
    response = self.handler(environ)                                                      
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 74, in __call__     
    response = self.get_response(request)                                                 
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 142, in get_response                                                                                   
    return self.handle_uncaught_exception(request, resolver, exc_info)                    
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 181, in handle_uncaught_exception                                                                      
    return callback(request, **param_dict)                                                
  File "/usr/lib/python2.6/site-packages/django/views/defaults.py", line 24, in server_error                                                                                        
    return http.HttpResponseServerError(t.render(Context({})))                            
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 173, in render
    return self._render(context)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)                                                  
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))                                          
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node                                                                                         
    result = node.render(context)                                                         
  File "/usr/lib/python2.6/site-packages/django/template/loader_tags.py", line 125, in render                                                                                       
    return compiled_parent._render(context)                                               
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)                                                  
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))                                          
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node                                                                                         
    result = node.render(context)                                                         
  File "/usr/lib/python2.6/site-packages/django/template/defaulttags.py", line 378, in render                                                                                       
    raise e                                                                               
TemplateSyntaxError: Caught NoReverseMatch while rendering: Reverse for 'cab_snippet_list' with arguments '()' and keyword arguments '{}' not found.                                

======================================================================
ERROR: test_middleware_disabled_anon_user (django.contrib.messages.tests.user_messages.LegacyFallbackTest)                                                                          
----------------------------------------------------------------------                    
Traceback (most recent call last):                                                        
  File "/usr/lib/python2.6/site-packages/django/contrib/messages/tests/base.py", line 257, in test_middleware_disabled_anon_user                                                    
    data, follow=True)                                                                    
  File "/usr/lib/python2.6/unittest.py", line 336, in failUnlessRaises                    
    callableObj(*args, **kwargs)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 322, in post        
    response = self.request(**r)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 230, in request     
    response = self.handler(environ)                                                      
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 74, in __call__     
    response = self.get_response(request)                                                 
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 142, in get_response                                                                                   
    return self.handle_uncaught_exception(request, resolver, exc_info)                    
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 181, in handle_uncaught_exception                                                                      
    return callback(request, **param_dict)                                                
  File "/usr/lib/python2.6/site-packages/django/views/defaults.py", line 24, in server_error                                                                                        
    return http.HttpResponseServerError(t.render(Context({})))                            
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 173, in render
    return self._render(context)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)                                                  
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))                                          
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node                                                                                         
    result = node.render(context)                                                         
  File "/usr/lib/python2.6/site-packages/django/template/loader_tags.py", line 125, in render                                                                                       
    return compiled_parent._render(context)                                               
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)                                                  
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))                                          
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node                                                                                         
    result = node.render(context)                                                         
  File "/usr/lib/python2.6/site-packages/django/template/defaulttags.py", line 378, in render                                                                                       
    raise e                                                                               
TemplateSyntaxError: Caught NoReverseMatch while rendering: Reverse for 'cab_snippet_list' with arguments '()' and keyword arguments '{}' not found.                                

======================================================================
ERROR: test_middleware_disabled_anon_user (django.contrib.messages.tests.session.SessionTest)                                                                                       
----------------------------------------------------------------------                    
Traceback (most recent call last):                                                        
  File "/usr/lib/python2.6/site-packages/django/contrib/messages/tests/base.py", line 257, in test_middleware_disabled_anon_user                                                    
    data, follow=True)                                                                    
  File "/usr/lib/python2.6/unittest.py", line 336, in failUnlessRaises                    
    callableObj(*args, **kwargs)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 322, in post        
    response = self.request(**r)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 230, in request     
    response = self.handler(environ)                                                      
  File "/usr/lib/python2.6/site-packages/django/test/client.py", line 74, in __call__     
    response = self.get_response(request)                                                 
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 142, in get_response                                                                                   
    return self.handle_uncaught_exception(request, resolver, exc_info)                    
  File "/usr/lib/python2.6/site-packages/django/core/handlers/base.py", line 181, in handle_uncaught_exception                                                                      
    return callback(request, **param_dict)                                                
  File "/usr/lib/python2.6/site-packages/django/views/defaults.py", line 24, in server_error                                                                                        
    return http.HttpResponseServerError(t.render(Context({})))                            
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 173, in render
    return self._render(context)                                                          
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render                                                                                
    return self.nodelist.render(context)
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node
    result = node.render(context)
  File "/usr/lib/python2.6/site-packages/django/template/loader_tags.py", line 125, in render
    return compiled_parent._render(context)
  File "/usr/lib/python2.6/site-packages/django/test/utils.py", line 29, in instrumented_test_render
    return self.nodelist.render(context)
  File "/usr/lib/python2.6/site-packages/django/template/__init__.py", line 796, in render
    bits.append(self.render_node(node, context))
  File "/usr/lib/python2.6/site-packages/django/template/debug.py", line 72, in render_node
    result = node.render(context)
  File "/usr/lib/python2.6/site-packages/django/template/defaulttags.py", line 378, in render
    raise e
TemplateSyntaxError: Caught NoReverseMatch while rendering: Reverse for 'cab_snippet_list' with arguments '()' and keyword arguments '{}' not found.

----------------------------------------------------------------------
Ran 166 tests in 236.682s

FAILED (errors=4)
Destroying test database 'default'...
crackpot@linux-Crackpot:/home/workspace/gftop/learning/djangoLearning/PracticalDjangoProjects2ndEdition/Version1.2/simplecms/src/simplecms>
