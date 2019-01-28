from django.conf.urls import url
from myadmin.views import index,user,type,goods

urlpatterns = [
    #index
    url(r'^$',index.myadmin_index,name='myadmin_index'),
    url(r'^myadmin_login$',index.myadmin_login,name='myadmin_login'),
    url(r'^myadmin_dologin$',index.myadmin_dologin,name='myadmin_dologin'),
    url(r'^myadmin_loginout$',index.myadmin_loginout,name='myadmin_loginout'),

    #user
    url(r'^myadmin_userlist$',user.myadmin_userlist,name='myadmin_userlist'),
    url(r'^myadmin_adduser$',user.myadmin_adduser,name='myadmin_adduser'),
    url(r'^myadmin_insertuser$',user.myadmin_insertuser,name='myadmin_insertuser'),
    url(r'^myadmin_updateuser/(?P<uid>[0-9]+)$',user.myadmin_updateuser,name='myadmin_updateuser'),
    url(r'^myadmin_edituser/(?P<uid>[0-9]+)$',user.myadmin_edituser,name='myadmin_edituser'),
    url(r'^myadmin_deleteuser/(?P<uid>[0-9]+)$',user.myadmin_deleteuser,name='myadmin_deleteuser'),

    #type
    url(r'^myadmin_typelist$',type.myadmin_typelist,name='myadmin_typelist'),
    url(r'^myadmin_addtype$', type.myadmin_addtype, name='myadmin_addtype'),
    url(r'^myadmin_inserttype$', type.myadmin_inserttype, name='myadmin_inserttype'),
    url(r'^myadmin_updatetype/(?P<uid>[0-9]+)$', type.myadmin_updatetype, name='myadmin_updatetype'),
    url(r'^myadmin_edittype/(?P<uid>[0-9]+)$', type.myadmin_edittype, name='myadmin_edittype'),
    url(r'^myadmin_deletetype/(?P<uid>[0-9]+)$', type.myadmin_deletetype, name='myadmin_deletetype'),

    #goods
    url(r'^myadmin_goodlist$',goods.myadmin_goodlist,name='myadmin_goodlist'),
    url(r'^myadmin_addgood$',goods.myadmin_addgood,name='myadmin_addgood'),
    url(r'^myadmin_insertgood$',goods.myadmin_insertgood,name='myadmin_insertgood'),
    url(r'^myadmin_updategood/(?P<uid>[0-9]+)$',goods.myadmin_updategood,name='myadmin_updategood'),
    url(r'^myadmin_editgood/(?P<uid>[0-9]+)$',goods.myadmin_editgood,name='myadmin_editgood'),
    url(r'^myadmin_deletegood/(?P<uid>[0-9]+)$',goods.myadmin_deletegood,name='myadmin_deletegood'),

]