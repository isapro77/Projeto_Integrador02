from django.urls import path

from.views import index, agendamento, consulta, catalogo, galeria

urlpatterns = [
    path('', index),
    path('agendamento', agendamento),
    path('catalogo', catalogo),
    path('consulta', consulta),
    path('galeria', galeria),

]