from django.contrib import admin
import json
from django.core.serializers.json import DjangoJSONEncoder

# Register your models here.
from .models import *

# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
# admin.site.register(Result)
# admin.site.register(AiModel)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_date', 'correct', 'model')
admin.site.register(Result, ResultAdmin)

class AiModelAdmin(admin.ModelAdmin):

    list_display = ('version', 'is_selected', 'pub_date', 'accuracy')

    def changelist_view(self, request, extra_context=None):
        
        model_obj = AiModel.objects.all()
        results = []
        for model in model_obj:
            result_obj = Result.objects.filter(model = model).count()
            results.append([model.is_selected, model.accuracy, result_obj])
        
        as_json = json.dumps(list(results), cls=DjangoJSONEncoder)
        context = extra_context or {"results" : as_json}
        
        return super().changelist_view(request, extra_context=context)
admin.site.register(AiModel, AiModelAdmin)