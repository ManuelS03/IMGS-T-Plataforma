const IMGS_Wizard = {
    currentStep: 0,
    totalSteps: 0,

    init: function(total) {
        this.totalSteps = total;
        this.showStep(0);
        this.updateProgress();
    },

    showStep: function(stepIndex) {
        document.querySelectorAll('.step').forEach(step => step.classList.remove('active'));
        const nextStep = document.getElementById(`step${stepIndex}`);
        if (nextStep) {
            nextStep.classList.add('active');
            this.currentStep = stepIndex;
            window.scrollTo(0, 0);
        }
    },

    goToStep: function(stepIndex) {
        
        if (stepIndex > this.currentStep) {
            if (this.currentStep === 0) {
                const nombre = document.querySelector('input[name="nombre_empresa"]').value;
                if (!nombre.trim()) {
                    alert("Por favor, ingresa el nombre de la organización.");
                    return;
                }
            } else {

                const currentStepDiv = document.getElementById(`step${this.currentStep}`);
                const radios = currentStepDiv.querySelectorAll('input[type="radio"]');
                const names = new Set();
                radios.forEach(r => names.add(r.name));
                
                for (let name of names) {
                    if (!currentStepDiv.querySelector(`input[name="${name}"]:checked`)) {
                        alert("Por favor, responda todas las preguntas antes de continuar.");
                        return;
                    }
                }
            }
        }
        this.showStep(stepIndex);
        this.updateProgress();
    },

    updateProgress: function() {
        const bar = document.getElementById('progressBar');
        if (bar) {
            const percent = (this.currentStep / this.totalSteps) * 100;
            bar.style.width = percent + '%';
        }
    }
};

function renderResultChart(labels, scores) {
    const ctx = document.getElementById('radarChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Nivel de Madurez',
                data: scores,
                fill: true,
                backgroundColor: 'rgba(13, 110, 253, 0.2)',
                borderColor: 'rgb(13, 110, 253)',
                pointBackgroundColor: 'rgb(13, 110, 253)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(13, 110, 253)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    angleLines: { display: true },
                    suggestedMin: 0,
                    suggestedMax: 5,
                    ticks: { 
                        stepSize: 1,
                        backdropColor: 'transparent'
                    },
                    
                    pointLabels: {
                        font: {
                            size: 11
                        },
                        callback: function(label) {
                            if (label.length > 10) {
                                return label.split(' '); 
                            }
                            return label;
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function enviarComentario(empresaId) {
    const textarea = document.getElementById('comentario_general');
    const comentario = textarea.value.trim();
    const btn = event.target.closest('button');

    if (!comentario) {
        alert("Por favor, escribe un comentario antes de enviar.");
        return;
    }

    btn.disabled = true;
    btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Enviando...';

    fetch('/guardar_comentario', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ empresa_id: empresaId, comentario: comentario })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert("¡Muchas gracias! Tu comentario ha sido guardado.");
            textarea.disabled = true;
            btn.innerHTML = '¡Enviado!';
            btn.classList.replace('btn-primary', 'btn-success');
        } else {
            alert("Error: " + data.message);
            btn.disabled = false;
            btn.innerHTML = 'Enviar Sugerencia';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error de conexión.");
        btn.disabled = false;
        btn.innerHTML = 'Enviar Sugerencia';
    });
}