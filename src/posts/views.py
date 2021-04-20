from django.db.models import Count ,Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post,Category
from .forms import CommentForm
from marketing.models import Signup
import datetime
from django.utils import timezone



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
    else:
        context = {}

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
    todays_date = datetime.datetime.now().date()
  
    context = {
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
        'latest' : latest,
        'category_count' : category_count,
        'todays_date' : todays_date,
        

    }

    return render(request,'blog.html', context)


def post(request, id):

    category_count = get_category_count()
    latest = Post.objects.order_by('-timestamp')[0:3]
    todays_date = datetime.datetime.now().date()

    post = get_object_or_404(Post, id=id)
    post.view_count += 1
    post.save()
    form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            form = CommentForm()
            redirect(post)
    
    
    context = {
        'form' : form,
        'post' : post,
        'latest' : latest,
        'category_count' : category_count,
        'todays_date' :todays_date
    }

    return render(request,'post.html', context)
 


def category(request, title):

    category_count = get_category_count()
    latest = Post.objects.order_by('-timestamp')[0:3]

    category_object =get_object_or_404(Category,title=title)
    if category_object:
        post_list = Post.objects.filter(categories__title=title).order_by('-timestamp')
    
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
    

    context={

        "queryset":paginated_queryset,
        "category" :category_object,
        "latest" : latest,
        'category_count' : category_count

    }
    return render(request,"category.html",context)