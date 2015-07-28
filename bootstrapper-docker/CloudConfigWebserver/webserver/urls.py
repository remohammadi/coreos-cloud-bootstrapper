from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'webserver.views.home', name='home'),
    url(r'^pxe-cloud-config.yml$', 'webserver.views.pxe_cloud_config', name='pxe_cloud_config'),
]
