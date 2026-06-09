document.addEventListener("DOMContentLoaded", function () {
    const feedbackForm = document.getElementById("feedback-form");
    const responseMessage = document.getElementById("feedback-response-message");

    if (feedbackForm) {
        feedbackForm.addEventListener("submit", function (e) {
            e.preventDefault();

            // Desativa botão
            const submitBtn = feedbackForm.querySelector("button[type='submit']");
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Enviando...`;

            // Oculta mensagem anterior
            responseMessage.classList.add("d-none");
            responseMessage.classList.remove("alert-success-custom", "alert-danger", "d-block");

            // Obtém dados do form
            const formData = new FormData(feedbackForm);
            const csrfToken = formData.get("csrfmiddlewaretoken");

            fetch("/enviar-feedback/", {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": csrfToken
                }
            })
            .then(response => response.json().then(data => ({ status: response.status, body: data })))
            .then(res => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;

                responseMessage.classList.remove("d-none");
                responseMessage.classList.add("d-block");

                if (res.status >= 200 && res.status < 300 && res.body.success) {
                    feedbackForm.reset();
                    responseMessage.className = "alert alert-success-custom rounded-card d-block mb-4";
                    responseMessage.innerHTML = `
                        <div class="d-flex align-items-center gap-2">
                            <i class="bi bi-check-circle-fill"></i>
                            <div>${res.body.message}</div>
                        </div>
                    `;
                } else {
                    responseMessage.className = "alert alert-danger rounded-card d-block mb-4";
                    responseMessage.innerHTML = `
                        <div class="d-flex align-items-center gap-2">
                            <i class="bi bi-exclamation-triangle-fill"></i>
                            <div>${res.body.message || 'Erro ao processar formulário.'}</div>
                        </div>
                    `;
                }
            })
            .catch(error => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;

                responseMessage.className = "alert alert-danger rounded-card d-block mb-4";
                responseMessage.innerHTML = `
                    <div class="d-flex align-items-center gap-2">
                        <i class="bi bi-exclamation-triangle-fill"></i>
                        <div>Ocorreu um erro ao enviar seu feedback. Por favor, tente novamente.</div>
                    </div>
                `;
                console.error("Erro no feedback:", error);
            });
        });
    }
});
