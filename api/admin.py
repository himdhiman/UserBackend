from django.contrib import admin
from api import models


admin.site.register([
    models.DateTime,
    models.UserModel,
    models.HistoryModel,
])
