from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
import logging
from django.conf import settings
from django.core.files.storage import default_storage
import numpy as np
import cv2
import string
from keras.models import load_model
from .forms import *

# from pybo.model import Result
from .models import Result

logger = logging.getLogger('mylogger')

def index(request):
    AiModelform = AiModelForm()
    return render(request, 'language/index.html', {'AiModelform' : AiModelform})

def upload(request):
    result_list = []
    if request.method == 'POST' and request.FILES.getlist('files'):
        # class names 준비
        class_names = list(string.ascii_lowercase)
        class_names = np.array(class_names)

        # 딥러닝 모델 로딩
        ai_model = request.POST['is_selected']
        model_path = AiModel.objects.get(is_selected=ai_model).ai_file.path
        dl_model = load_model(model_path)


        # history 저장을 위해 객체에 담아서 DB에 저장한다.
        # 이때 파일시스템에 저장도 된다.
        model = AiModel.objects.get(is_selected = ai_model)
        file_list = request.FILES.getlist('files')
        answer_list = request.POST.getlist('answer')
        for i, file in enumerate(file_list):
            result = Result()
            result.answer = answer_list[i].lower()
            result.image = file
            result.pub_date = timezone.datetime.now()
            result.model = AiModel.objects.get(is_selected=ai_model)
            result.save()
            
            # 흑백으로 읽기
            img = cv2.imread(result.image.path, cv2.IMREAD_GRAYSCALE)

            # 크기 조정
            img = cv2.resize(img, (28, 28))

            # input shape 맞추기
            dl_test_sign = img.reshape(1, 28, 28, 1)
            
            # 스케일링
            dl_test_sign = dl_test_sign / 255.

            # 예측 : 결국 이 결과를 얻기 위해 모든 것을 했다.
            dl_pred = dl_model.predict(dl_test_sign) 
            
            pred = dl_pred.argmax(axis=1)
            

            #결과를 DB에 저장한다.
            result.result = class_names[pred][0]
            if result.answer == result.result:
                result.correct = 'correct'
            result.save()
            
            result_list.append(result)
        
        result = Result.objects.filter(model=model)
        model.accuracy = result.filter(correct='correct').count() / result.count()
        model.save()
        
        context = {
            'result': result_list,
        }


    # http method의 GET은 처리하지 않는다. 사이트 테스트용으로 남겨둠
    else:
        # test = request.GET['test']
        # logger.error(('Something went wrong!!', test))
        logger.error(('Something went wrong!!'))
        
    return render(request, 'language/result.html', context)


def update_model(request):
    if request.method == 'POST' and request.FILES['ai_file']:
        form = AiModelForm2(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            model = form.save(commit=False)
            model.ai_file = request.FILES['ai_file']
            model.ip = request.META['REMOTE_ADDR']
            model.save()
            return redirect(model)
    else:
        form = AiModelForm2()
        ai_models = AiModel.objects.all()
        return render(request, 'language/manage.html', {'form':form, 'ai_models':ai_models})

