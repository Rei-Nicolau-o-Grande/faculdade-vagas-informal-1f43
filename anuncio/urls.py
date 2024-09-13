from django.urls import path
from . import views

app_name = 'anuncio'

urlpatterns = [
    path('', views.ListaAnuncio.as_view(), name='lista'),
    path('<slug>', views.DetalheAnuncio.as_view(), name='detalhe'),
    path('contratante/', views.Contratante.as_view(), name='contratante'),
    path('contratado/', views.Contratado.as_view(), name='contratado'),
    path('contratante/<slug>', views.DetalheAnuncio.as_view(), name='detalhe_contratante'),
    path('contratado/<slug>', views.DetalheAnuncio.as_view(), name='contratado_contratado'),
    path('categorias/', views.Categorias.as_view(), name='categorias'),
    path('categorias/<categorias>', views.FiltroCategorias.as_view(), name='filtro_categorias'),

]
