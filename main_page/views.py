from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , response 
from api.models import MenuModel
from django.http import JsonResponse
from . import models
from . import forms
from django.shortcuts import *
def index(request):
    meals = MenuModel.objects.all()
    if request.user.is_authenticated:
        try :
            sabat = models.BasketModel.objects.filter(user=request.user)
            backet_length = sabat
        except models.BasketModel.DoesNotExist:
            backet_length = 0
        return render(request , 'main_page/index.html', {
                'meals'  : meals , 
                'basket' : backet_length ,
            })
    else:
        backet_length = []
        return render(request , 'main_page/index.html', {
            'meals'  : meals , 
            'basket' : backet_length ,
        })


def rules(request):
    return render(request , 'main_page/rules.html')

def backet(request):
    try :
        sabat = models.BasketModel.objects.filter(user=request.user)
        return render(request , 'main_page/basket.html' , {
            'basket' : sabat
            })
    except models.BasketModel.DoesNotExist:
        return render(request , 'main_page/basket.html' , {
            'message' : 'You don\'t have any order !'
        })

def delete_order(request, order_id):
    # Ищем заказ в базе данных
    order = get_object_or_404(models.BasketModel, id=order_id)

    # Убеждаемся, что пользователь, пытающийся удалить заказ, имеет на это право (например, проверьте, что это его заказ)
    if order.user == request.user.username:
        # Удаляем заказ
        order.delete()
        return JsonResponse({'message': 'Order deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Permission denied'}, status=403)

def create_order(request):
    if request.method == 'POST':
        form = forms.Orderform(request.POST)
        if True:
            # Извлекаем данные из формы
            user_id = request.POST['user_id']
            price = str(request.POST['narhi'])
            # price = '12.00'
            meal_name = request.POST['meal_name']
            quantity = 1
            print(user_id , '---->' , price , meal_name , quantity)

            # Создаем объект BasketModel
            order = models.BasketModel(
                user=user_id,
                price=price,
                meal_name=meal_name,
                quantity=quantity
            )

            # Устанавливаем пользователя
            order.user = request.user

            # Сохраняем объект
            order.save()

            print('SAVED !!!!')

            # Возвращаем JSON-ответ об успешном сохранении
            return redirect('main')
        else:
            # Возвращаем JSON-ответ с ошибкой валидации формы
            return JsonResponse({'error': form.errors}, status=400)

    # Если запрос не является POST-запросом, возвращаем ошибку
    return JsonResponse({'error': 'Invalid request method'}, status=405)