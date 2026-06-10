from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Material, PontoDeColeta, Feedback
import json

def home(request):
    materiais = Material.objects.all()
    pontos = PontoDeColeta.objects.filter(ativo=True)
    context = {
        'materiais': materiais,
        'pontos': pontos,
    }
    return render(request, 'reciclagem/home.html', context)

def api_pontos_coleta(request):
    material_slug = request.GET.get('material', '').strip()
    pontos = PontoDeColeta.objects.filter(ativo=True).distinct()
    
    if material_slug:
        pontos = pontos.filter(materiais_aceitos__slug=material_slug)
        
    pontos_list = []
    for p in pontos:
        locais = []
        for local in p.locais_descarte.filter(ativo=True):
            locais.append({
                'id': local.id,
                'nome': local.nome,
                'descricao': local.descricao,
                'material': local.material.nome
            })
        pontos_list.append({
            'id': p.id,
            'nome': p.nome,
            'endereco': p.endereco,
            'latitude': float(p.latitude),
            'longitude': float(p.longitude),
            'materiais': [m.nome for m in p.materiais_aceitos.all()],
            'icones_materiais': [m.icone for m in p.materiais_aceitos.all()],
            'locais_descarte':locais,
        })
        
    return JsonResponse(pontos_list, safe=False)

@require_POST
def enviar_feedback(request):
    try:
        # Se for enviado como JSON (AJAX)
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST

        nome = data.get('nome', '').strip()
        email = data.get('email', '').strip()
        tipo_feedback = data.get('tipo_feedback', 'sugestao').strip()
        ponto_coleta_id = data.get('ponto_coleta', None)
        mensagem = data.get('mensagem', '').strip()

        if not mensagem:
            return JsonResponse({'success': False, 'message': 'O campo mensagem é obrigatório.'}, status=400)

        ponto_coleta = None
        if ponto_coleta_id:
            try:
                ponto_coleta = PontoDeColeta.objects.get(id=int(ponto_coleta_id))
            except (PontoDeColeta.DoesNotExist, ValueError):
                pass

        Feedback.objects.create(
            nome=nome,
            email=email,
            tipo_feedback=tipo_feedback,
            ponto_coleta=ponto_coleta,
            mensagem=mensagem
        )

        return JsonResponse({
            'success': True, 
            'message': 'Muito obrigado! Seu feedback foi enviado com sucesso e será analisado por nossa equipe.'
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Erro ao processar feedback: {str(e)}'}, status=500)
