from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import PostForm
from .models import Post


class PostList(generic.ListView):
    template_name = "blog/home.html"
    context_object_name = "posts_list"
    def get_queryset(self):
        return Post.objects.filter(status='Pub').order_by('-datetime_modified')
# def posts_list(request):
#     posts_list = Post.objects.filter(status='Pub').order_by('-datetime_modified')
#     return render(request,"blog/home.html",{'posts_list': posts_list})


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
# def post_detail(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request,'blog/post_detail.html',{'post': post})


class PostCreate(generic.CreateView):
    form_class = PostForm
    template_name ='blog/create_new_post.html'
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = PostForm()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request , 'blog/create_new_post.html',context={'form':form})


class PostUpdate(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name ='blog/create_new_post.html'
# def update_post(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('post_detail',pk)
#     return render(request,'blog/create_new_post.html',context={'form':form})


class PostDelete(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')  #or    get_success_url(self)
                                                   # return reverse('post_list')

# def delete_post(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     if request.method =='POST':
#         post.delete()
#         return redirect('post_list')
#     return render(request,'blog/delete_post.html',context={'post':post})
