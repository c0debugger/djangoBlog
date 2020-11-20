from django.db.models import Count ,Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.shortcuts import render, get_object_or_404
from .models import Post
from marketing.models import Signup



def search(request):

    query = request.GET.get('q')

    if query:
        queryset = Post.objects.filter(

            Q(title__icontains = query)|
            Q(overview__icontains = query)
            
        ).distinct()

    context = {
        
        'queryset' : queryset

    }

    return render(request,'search_results.html',context)


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


    context = {
        'object_list': featured,
        'latest':latest
    }

    return render(request,'index.html',context)


def blog(request):
    category_count = get_category_count()
    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'

    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    latest = Post.objects.order_by('-timestamp')[0:3]


    context = {
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
        'latest' : latest,
        'category_count' : category_count

    }

    return render(request,'blog.html', context)


def post(request, id):

    post = get_object_or_404(Post, id=id)
    context = {

        'post' : post
    }

    return render(request,'post.html', context)
