from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .forms import PessoaForm

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/criar_pessoa.html', {'form': form})

def listar_pessoas(request):
    ordem = request.GET.get('ordem', 'nome')
    pessoas = Pessoa.objects.all().order_by(ordem)
    return render(request, 'cadastro/listar_pessoas.html', {'pessoas': pessoas})

def detalhes_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    return render(request, 'cadastro/detalhes_pessoa.html', {'pessoa': pessoa})
