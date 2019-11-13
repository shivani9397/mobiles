from rest_framework.routers import SimpleRouter
from .views import NokiaOperations

simpleRouter = SimpleRouter()

simpleRouter.register('nokia',NokiaOperations)
urlpatterns = simpleRouter.urls