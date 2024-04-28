from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    #cuando escribamos "nosotros en el url, vamos a acceder a la vista "nosotros. es el html
    path('nosotros', views.nosotros, name='nosotros'),
    path('perfumes', views.Perfumes, name="perfumes"),
    path('perfumes/crear', views.crear_perfume, name="crear_perfume"),
    path('maquillaje', views.maquillaje, name="maquillaje"),
    path('perfumes/crear_maq', views.crear_maq, name="crear_maq"),
    path('Capilares', views.Capilares, name="Capilares"),
    path('perfumes/crear_capilares', views.crear_capilares, name="crear_capilares"),
    path('skin_care', views.skin_care, name="skin_care"),
    path('perfumes/crear_skinCare', views.crear_skinCare, name="crear_skinCare"),
    path('accesorios', views.accesorios, name="accesorios"),
    path('perfumes/crear_accesorios', views.crear_accesorios, name="crear_accesorios"),

]
