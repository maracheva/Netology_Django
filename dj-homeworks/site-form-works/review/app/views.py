from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import HttpResponseRedirect


from .models import Product, Review
from .forms import ReviewForm

# список товаров
class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


# карточка товара
class ProductView(DetailView):
    model = Product
    template_name = 'app/product_detail.html' # добавили html шаблон

    def get_success_url(self):
        product_id = self.request.session.get('current_product')
        if product_id:
            return reverse('product_detail', kwargs={'pk': product_id})

        return reverse('main_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_product = self.get_object()
        context['reviews'] = Review.objects.filter(product=current_product)
        context['form'] = ReviewForm

        #  проверка на наличие комментария:
        # если has_commented variable = False, то можно добавить комментарий, после чего has_commented станет True
        if self.request.session.get('has_commented', False):
            context['has_commented'] = self.request.session.get('has_commented')
            context['is_review_exist'] = True

        return context


    # Добавление и сохранение информации на сервер осуществляется через POST запрос.
    def post(self, request, *args, **kwargs):
        has_commented = self.request.session.get('has_commented', [])  # запрос о наличии коммента в сессии
        form = ReviewForm(self.request.POST) # считываем данные формы

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        current_product = Product.objects.get(id=pk)

        if form.is_valid() and pk not in has_commented:
            text_review = request.POST['text']
            Review.objects.create(text=text_review, product=current_product)
            has_commented.append(pk)
            self.request.session['has_commented'] = has_commented

            # return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': pk}))

        return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': pk}))

