from django.shortcuts import render, get_object_or_404

from core.same_requests import get_posts, get_category


def index(request):
    """Главная страница, Лента записей"""
    max_res = 5
    post_list = get_posts().order_by("-pub_date")[:max_res]
    context = {"post_list": post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Подробное описание выбранной записи"""
    post = get_object_or_404(get_posts(), pk=post_id,)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображение публикации по категории"""
    max_res = 10
    category = get_object_or_404(get_category(), slug=category_slug, )
    post_list = get_posts().filter(category__slug=category_slug).order_by(
        "-pub_date")[:max_res]
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
