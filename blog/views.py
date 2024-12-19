from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from .models import Post, Blog, Mensagem
from .forms import MensagemForm

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first(),
    }

    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": get_object_or_404(Post, pk=post_id),
        "blog": Blog.objects.first(),
    }

    return render(request, "post.html", context)

def sobre(request):
    context = {
        "blog": Blog.objects.first(),
    }

    return render(request, "about.html", context)

def contato(request):
    context = {
        "blog": Blog.objects.first(),
    }

    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensagens')
        else:
            context["form"] = form
    else:
        context["form"] = MensagemForm()
    
    return render(request, "contact.html", context)
    
def mensagem(request):
    context = {
        "mensagens": Mensagem.objects.all(),
        "blog": Blog.objects.first(),       
    }

    return render(request, "mensagem.html", context)

def editar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    context = {
        "blog": Blog.objects.first(),
        "form": MensagemForm(initial=model_to_dict(mensagem))
    }

    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mensagem')

    return render(request, "contact.html", context)

def deletar_mensagem(request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem": get_object_or_404(Mensagem, pk=mensagem_id),
    }

    if request.method == "POST":
        context["mensagem"].delete()
        return redirect('mensagem')
    else:
        return render(request, "delete_contact.html", context)

def cadastro(request):
    context = {
        "blog": Blog.objects.first(),
    }

    return render(request, "cadastro.html", context)