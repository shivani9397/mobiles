from rest_framework.routers import SimpleRouter
from .views import SamsungOperations

simpleRouter = SimpleRouter()

simpleRouter.register('Samsung',SamsungOperations)

urlpatterns = simpleRouter.urls