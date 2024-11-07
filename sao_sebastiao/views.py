from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from blog.models import Post, ImagemNoticia
from .models import Documento
from collections import OrderedDict
from django.views.decorators.http import require_GET
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def index(request):
    noticias = Post.objects.all().order_by('-criado_em')
    noticias_list = list()
    for n in noticias:
        noticias_list.append(n)

    ultimo_index = len(noticias_list)
    penultimo_index = ultimo_index - 1

    return render(request, 'index.html', {'noticias': noticias_list, 'ultimo_index': ultimo_index, 'penultimo_index': penultimo_index})

def sobreNos(request):
    return render(request, 'about.html')
        
def servicos(request):
    return render(request, 'services.html')

def transparencia(request):
     # Cria um OrderedDict para garantir a ordem dos dropdowns
    ordered_documents = OrderedDict([
        ("Alvará de Funcionamento", []),
        ("Atestados de Capacidade Técnica", []),
        ("Regularidade Fiscal Matriz", []),
        # Adicione mais tipos de documentos conforme necessário
    ])
    
    documentos = Documento.objects.all()
    
    # Organiza os documentos de acordo com o tipo esperado
    for document in documentos:
        tipo_documento = document.tipo
        # Verifica se o tipo de documento está nos tipos ordenados
        if tipo_documento in ordered_documents:
            ordered_documents[tipo_documento].append(document)
        else:
            # Se o tipo de documento não estiver na lista ordenada, adiciona no final
            ordered_documents[tipo_documento] = [document]

    return render(request, 'transparencia.html', {'documentos': ordered_documents.items()})

def noticias(request):
    posts = Post.objects.all().order_by('-criado_em')
    destaques = posts[:3]
    outros = posts[3:]
    return render(request, 'noticias.html',{'noticias': posts, 'destaques': destaques, 'outros': outros})

def contato(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        send_mail(
            'Mensagem de {}: {}'.format(name, assunto),
            'Nome: {} \nEmail: {} \nTelefone: {} \nAssunto: {} \nMensagem: {}'.format(name, email, telefone, assunto, mensagem),
            "ti@rockefellerambiental.com.br",
            ["administrativo@rockefellerambiental.com.br"],
            fail_silently=False,
        )
        messages.success(request, 'Formulário enviado com sucesso!')
        return redirect('contato')
    else:
        return render(request, 'contato.html')
    
def noticia(request, id):
    post = Post.objects.get(id=id)
    posts = Post.objects.filter(~Q(id=post.id)).order_by('-criado_em')
    sugestoes = posts[:3]
    current_url = request.build_absolute_uri()
    fotos = ImagemNoticia.objects.filter(noticia=post)
    return render(request, 'noticia.html',{'post': post, 'sugestoes': sugestoes, 'current_url': current_url, 'fotos': fotos})

class NoticiaList(APIView):
    def get(self, request):
        noticias = Post.objects.all()
        data = [{"titulo": noticia.titulo, "conteudo": noticia.conteudo, "data_publicacao": noticia.criado_em} for noticia in noticias]
        return Response(data)