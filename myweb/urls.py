from django.conf.urls import url,include
from myweb.views import index,user,goods,cart

urlpatterns = [
    #index
    url(r'^$',index.web_index,name='web_index'),
    url(r'^web_login$',index.web_login,name='web_login'),
    url(r'^web_dologin$',index.web_dologin,name='web_dologin'),
    url(r'^web_loginout$',index.web_loginout,name='web_loginout'),

    #user
    url(r'^web_personal$',user.web_personal,name='web_personal'),
    url(r'^web_register$',user.web_register,name='web_register'),
    url(r'^web_insertuser$',user.web_insertuser,name='web_insertuser'),
    url(r'^web_updatepassword$',user.web_updatepassword,name='web_updatepassword'),
    url(r'^web_editpassword$',user.web_editpassword,name='web_editpassword'),
    url(r'^web_editpassword2$',user.web_editpassword2,name='web_editpassword2'),
    url(r'^web_update$',user.web_update,name='web_update'),
    url(r'^web_edit$',user.web_edit,name='web_edit'),

    #good
    url(r'^web_goodlist$',goods.web_goodlist,name='web_goodlist'),
    url(r'^web_good_details/(?P<uid>[0-9]+)$',goods.web_good_details,name='web_good_details'),

    #cart
    url(r'^web_cart/(?P<uid>[0-9]+)$',cart.web_cart,name='web_cart'),
    url(r'^web_insertcart/(?P<uid>[0-9]+)$',cart.web_insertcart,name='web_insertcart'),
    url(r'^web_insertcart2/(?P<uid>[0-9]+)$',cart.web_insertcart2,name='web_insertcart2'),
]
