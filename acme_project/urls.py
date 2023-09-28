from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy 
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import CreateView 

from birthday import views

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('birthday/', include('birthday.urls')),
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
