document.addEventListener("DOMContentLoaded", function () {
    // Coordenadas padrão
    const defaultLat = -22.9068;
    const defaultLng = -47.0616;

    // Inicialização do Mapa Leaflet
    const map = L.map('map').setView([defaultLat, defaultLng], 13);

    // Carregamento de tiles do OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    let markers = [];
    const materialSelect = document.getElementById("material-select");
    const searchBtn = document.getElementById("btn-buscar");
    const badgeCounter = document.getElementById("ponto-counter");

    // Função para carregar e atualizar pontos
    function carregarPontos(materialSlug = "") {
        let url = "/api/pontos/";
        if (materialSlug) {
            url += `?material=${encodeURIComponent(materialSlug)}`;
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                // Limpa marcadores existentes
                markers.forEach(marker => map.removeLayer(marker));
                markers = [];

                // Atualiza o contador visual
                if (badgeCounter) {
                    badgeCounter.textContent = `${data.length} local(is) encontrado(s)`;
                }

                // Ajusta limites do mapa se houver pontos
                const bounds = [];

                data.forEach(ponto => {
                    const marker = L.marker([ponto.latitude, ponto.longitude]).addTo(map);

                    // Renderiza popup customizado
                    let materiaisBadges = ponto.materiais.map(mat => `<span class="badge-material">${mat}</span>`).join("");

                    // Lista de locais de descarte
                    let locaisListHtml = "";
                    if (ponto.locais_descarte && ponto.locais_descarte.length > 0) {
                        locaisListHtml = ponto.locais_descarte.map(local => `
                            <div class="mb-1">
                                <span class="badge-material">${local.material}</span>
                                <strong>${local.nome}</strong><br>
                                <span class="text-secondary">${local.descricao || "Sem descrição"}</span>
                            </div>
                        `).join("");
                    } else {
                        locaisListHtml = "<small class='text-muted'>Nenhum local de descarte específico encontrado para este ponto.</small>";
                    }

                    // Definir classe e ícone conforme status
                    let statusClass = "status-ativo";
                    let statusIcon = "🟢";
                    if (ponto.status === "Indisponível") {
                        statusClass = "status-indisponivel";
                        statusIcon = "🔴";
                    } else if (ponto.status === "Em manutenção") {
                        statusClass = "status-manutencao";
                        statusIcon = "🟡";
                    }

                    // Montar popup
                    let popupContent = `
                        <div class="p-1">
                            <h6 class="mb-1 text-success fw-bold">${ponto.nome}</h6>
                            <p class="text-secondary small mb-2">
                                <i class="bi bi-geo-alt-fill text-danger"></i> ${ponto.endereco}
                            </p>
                            <p class="small mb-1">
                                <strong>Status:</strong> <span class="${statusClass}">${statusIcon} ${ponto.status}</span>
                            </p>
                            <p class="small mb-2">
                                <strong>Horário:</strong> ${ponto.horario_funcionamento || "Não informado"}
                            </p>
                            <div class="mb-1"><strong>Aceita:</strong></div>
                            <div class="d-flex flex-wrap">${materiaisBadges}</div>
                            <div class="mt-2">
                                <h6 class="text-primary small mb-1"><strong>Locais de descarte:</strong></h6>
                                ${locaisListHtml}
                            </div>
                        </div>
                    `;

                    marker.bindPopup(popupContent);
                    markers.push(marker);
                    bounds.push([ponto.latitude, ponto.longitude]);
                });

                // Foca nos marcadores existentes
                if (bounds.length > 0) {
                    map.fitBounds(bounds, { padding: [50, 50], maxZoom: 15 });
                } else if (!materialSlug) {
                    // Centraliza de volta no default
                    map.setView([defaultLat, defaultLng], 13);
                }
            })
            .catch(error => {
                console.error("Erro ao buscar pontos de coleta:", error);
            });
    }

    // Carregar inicialmente todos os pontos
    carregarPontos();

    // Event Listeners para Filtros
    if (materialSelect) {
        materialSelect.addEventListener("change", function () {
            carregarPontos(this.value);
        });
    }

    if (searchBtn) {
        searchBtn.addEventListener("click", function () {
            const val = materialSelect ? materialSelect.value : "";
            carregarPontos(val);
        });
    }
});
