"""
URL configuration for Geobag_Counting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.urls import path,include
from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Geobag/', views.Geobag, name = 'Geobag'),
    path('geobagdatatable/', views.Geobagdatatable, name = 'Geobagdatatable'),
    
    path('geobagriverbank/', views.geobagriverbank, name = 'geobagriverbank'),
    path('geobagriverbank_input/', views.geobagriverbank_input, name = 'geobagriverbank_input'),
    path('geobagriverbank_edit/<int:id>', views.geobagriverbank_edit, name = 'geobagriverbank_edit'),
    path('geobagriverbank_update/', views.geobagriverbank_update, name = 'geobagriverbank_update'),
    path('geobagriverbank_delete/<int:id>', views.geobagriverbank_delete, name = 'geobagriverbank_delete'),
    
    path('filledriverbank/', views.filledriverbank, name = 'filledriverbank'),
    path('filledriverbank_input/', views.filledriverbank_input, name = 'filledriverbank_input'),
    path('filledriverbank_edit/<int:id>', views.filledriverbank_edit, name = 'filledriverbank_edit'),
    path('filledriverbank_update/', views.filledriverbank_update, name = 'filledriverbank_update'),
    path('filledriverbank_delete/<int:id>', views.filledriverbank_delete, name = 'filledriverbank_delete'),
    
    path('prototypeproposed/', views.prototypeproposed, name = 'prototypeproposed'),
    path('prototypeproposed_input/', views.prototypeproposed_input, name = 'prototypeproposed_input'),
    path('prototypeproposed_edit/<int:id>', views.prototypeproposed_edit, name = 'prototypeproposed_edit'),
    path('prototypeproposed_update/', views.prototypeproposed_update, name = 'prototypeproposed_update'),
    path('prototypeproposed_delete/<int:id>', views.prototypeproposed_delete, name = 'prototypeproposed_delete'),
    
    path('preparingdataset/', views.preparingdataset, name = 'preparingdataset'),
    path('preparingdataset_input/', views.preparingdataset_input, name = 'preparingdataset_input'),
    path('preparingdataset_edit/<int:id>', views.preparingdataset_edit, name = 'preparingdataset_edit'),
    path('preparingdataset_update/', views.preparingdataset_update, name = 'preparingdataset_update'),
    path('preparingdataset_delete/<int:id>', views.preparingdataset_delete, name = 'preparingdataset_delete'),
    
    path('testingprocedures/', views.testingprocedures, name = 'testingprocedures'),
    path('testingprocedures_input/', views.testingprocedures_input, name = 'testingprocedures_input'),
    path('testingprocedures_edit/<int:id>', views.testingprocedures_edit, name = 'testingprocedures_edit'),
    path('testingprocedures_update/', views.testingprocedures_update, name = 'testingprocedures_update'),
    path('testingprocedures_delete/<int:id>', views.testingprocedures_delete, name = 'testingprocedures_delete'),
    
    
    path('toonificationheadingpage/', views.toonificationheadingpage, name='toonificationheadingpage'),
    path('toonificationheadinginsert/', views.toonificationheadinginsert, name='toonificationheadinginsert'),
    path('Toonificationdatatable/', views.Toonificationdatatable, name='Toonificationdatatable'),
    path('ToonificationHeadingpageedit/<int:id>', views.ToonificationHeadingpageedit, name='ToonificationHeadingpageedit'),
    path('ToonificationHeadingupdate/', views.ToonificationHeadingupdate, name='ToonificationHeadingupdate'),
    path('deleteToonificationHeading/<int:id>', views.deleteToonificationHeading, name='deleteToonificationHeading'),
    
    
    path('toonificationimagepage/', views.toonificationimagepage, name='toonificationimagepage'),
    path('toonificationimageinsert/', views.toonificationimageinsert, name='toonificationimageinsert'),
    path('toonificationimagedatatable/', views.toonificationimagedatatable, name='toonificationimagedatatable'),
    path('toonificationimagepageedit/<int:id>', views.toonificationimagepageedit, name='toonificationimagepageedit'),
    path('toonificationimageupdate/', views.toonificationimageupdate, name='toonificationimageupdate'),
    path('deletetoonificationimage/<int:id>', views.deletetoonificationimage, name='deletetoonificationimage'),
     
     
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
