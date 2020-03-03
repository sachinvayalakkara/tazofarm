from django.urls import path
from . import views
urlpatterns = [
    path('home',views.fn_home),
    path('login',views.fn_login),
    path('register',views.fn_register),
    path('menu',views.fn_menu),
    path('tower/',views.fn_showtower), #for admin
    path('addtower/',views.fn_addtower),
    path('viewtower',views.fn_viewtower), #for user
    path('showrack/',views.fn_showrack), 
    path('addrack/',views.fn_addrack),
    path('showbay/',views.fn_showbay),
    path('addbay/',views.fn_addbay),
    path('addvendor/',views.fn_addvendor),
    path('showvendor/',views.fn_showvendor),
   
    # path('logout',views.fn_logout),

    path('viewtower',views.fn_viewtower),
    path('deleterack',views.fn_deleterack),
    path('deletevendor',views.fn_deletevendor),
    path('updaterack/',views.fn_update_rack),
    path('deletebay/',views.fn_deletebay),
    path('updatebay/',views.fn_update_bay),
    path('deletevendor/',views.fn_deletevendor),
    path('updatevendor/',views.fn_update_vendor),
    path('deletetower/',views.fn_deletetower),
    path('updatetower/',views.fn_update_tower),
    path('showcrop/',views.fn_showcrop),
    path('addcrop/',views.fn_addcrop),
    path('editcrop/',views.fn_editcrop),
    path('deletecrop/',views.fn_deletecrop),
    path('showpackingtype/',views.fn_showpackingtype),
    path('addpackingtype/',views.fn_addpackingtype),
    path('deletepackingtype/',views.fn_delete_packingtype),
    path('showstages/',views.fn_showstages),
    path('addstages/',views.fn_addstages),
    path('deletestages/',views.fn_deletestages),
    path('showcroptype/',views.fn_showcroptype),
    path('addcroptype/',views.fn_addcroptype),
    path('deletecroptype/',views.fn_deletecroptype),
    path('updatecrop/',views.fn_updatecrop),
    
]

