from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Category, Post


def index(request):
    """Главная страница, Лента записей"""
    post_list = Post.objects.select_related(
        "category",
        "location",
        "author",
    ).only(
        "title",
        "text",
        "pub_date",
        "author__username",
        "category__title",
        "category__slug",
        "location__name",
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ).order_by("-pub_date")[:5]
    context = {"post_list": post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Подробное описание выбранной записи"""
    post = get_object_or_404(Post.objects.select_related(
        "category",
        "location",
        "author",
    ).only(
        "title",
        "text",
        "pub_date",
        "author__username",
        "category__title",
        "category__slug",
        "location__name",
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ), pk=post_id,)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображение публикации по категории"""
    category = get_object_or_404(Category.objects.values(
        "title", "description")
        .filter(
        is_published=True,
    ), slug=category_slug,
    )
    post_list = Post.objects.select_related(
        "category",
        "location",
        "author",
    ).only(
        "title",
        "text",
        "pub_date",
        "author__username",
        "category__title",
        "category__slug",
        "location__name",
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    ).filter(category__slug=category_slug).order_by("-pub_date")[:10]
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
