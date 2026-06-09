from reciclagem.models import Material, PontoDeColeta

# 1. Limpa dados anteriores
PontoDeColeta.objects.all().delete()
Material.objects.all().delete()

# 2. Cria materiais
plastico = Material.objects.create(
    nome="Plástico", 
    slug="plastico", 
    instrucoes_preparo="Lave e seque as embalagens plásticas. Retire as tampas, se possível.", 
    icone="bi-droplet"
)
vidro = Material.objects.create(
    nome="Vidro", 
    slug="vidro", 
    instrucoes_preparo="Lave garrafas e potes. Em caso de vidro quebrado, embale em jornal ou caixa de papelão para evitar acidentes.", 
    icone="bi-cup"
)
papelao = Material.objects.create(
    nome="Papelão e Papel", 
    slug="papelao", 
    instrucoes_preparo="Amasse as caixas de papelão. Não misture papel sujo, como guardanapos ou fitas adesivas.", 
    icone="bi-box-seam"
)
metais = Material.objects.create(
    nome="Metais", 
    slug="metais", 
    instrucoes_preparo="Lave as latas de alumínio e amasse-as para reduzir o volume.", 
    icone="bi-nut"
)
eletronicos = Material.objects.create(
    nome="Eletrônicos", 
    slug="eletronicos", 
    instrucoes_preparo="Não descarte pilhas ou eletrônicos no lixo comum. Mantenha os conectores protegidos.", 
    icone="bi-cpu"
)
organicos = Material.objects.create(
    nome="Orgânico (Compostagem)", 
    slug="organicos", 
    instrucoes_preparo="Separe cascas de alimentos, legumes e folhas. Não inclua carnes ou restos temperados.", 
    icone="bi-flower1"
)

# 3. Cria pontos de coleta (coordenadas reais aproximadas de Campinas)
eco_centro = PontoDeColeta.objects.create(
    nome="Ecoponto Centro",
    endereco="Av. Francisco Glicério, 1000 - Centro, Campinas - SP",
    latitude=-22.9064,
    longitude=-47.0612,
    ativo=True
)
eco_centro.materiais_aceitos.add(plastico, vidro, papelao, metais)

eco_taquaral = PontoDeColeta.objects.create(
    nome="Ecoponto Parque Taquaral",
    endereco="Av. Dr. Heitor Penteado, 1600 - Taquaral, Campinas - SP",
    latitude=-22.8732,
    longitude=-47.0498,
    ativo=True
)
eco_taquaral.materiais_aceitos.add(plastico, vidro, papelao, metais, eletronicos)

eco_ouro_verde = PontoDeColeta.objects.create(
    nome="Ecoponto Ouro Verde",
    endereco="Rua Plínio Aguinaldo Di Nardo, 200 - Ouro Verde, Campinas - SP",
    latitude=-22.9567,
    longitude=-47.1354,
    ativo=True
)
eco_ouro_verde.materiais_aceitos.add(plastico, papelao, metais, organicos)

print("Banco de dados populado com sucesso!")
