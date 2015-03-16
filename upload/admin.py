from django.contrib import admin
from upload.models import insertData, invitation, batchData

# Register your models here.

admin.site.register(insertData)
admin.site.register(invitation)
admin.site.register(batchData)

#admin.site.register(NameForm)