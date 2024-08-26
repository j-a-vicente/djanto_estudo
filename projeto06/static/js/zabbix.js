function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }
    
    return [bg_color, border_color];
    
}


function renderiza_cpu_ultimos_30_dias(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {

        const ctx = document.getElementById('uso_de_cpu').getContext('2d');
        const cores = gera_cor(qtd=30); // Gerar cores para os 30 dias
        const myChart = new Chart(ctx, {
            type: 'line', // Gráfico de linha para visualizar a tendência ao longo dos dias
            data: {
                labels: data.labels, // Labels são as datas dos últimos 30 dias
                datasets: [{
                    label: 'CPU (Últimos 30 dias)',
                    data: data.data, // Dados são os valores somados de cada dia
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 2,
                    fill: false
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Uso de CPU (%)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Dias'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }).catch(function(error) {
        console.error('Erro ao renderizar o gráfico:', error);
    });
}




function renderiza_ram_ultimos_30_dias(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {

        const ctx = document.getElementById('uso_de_memoria').getContext('2d');
        const cores = gera_cor(qtd=30); // Gerar cores para os 30 dias
        const myChart = new Chart(ctx, {
            type: 'line', // Gráfico de linha para visualizar a tendência ao longo dos dias
            data: {
                labels: data.labels, // Labels são as datas dos últimos 30 dias
                datasets: [{
                    label: 'RAM (Últimos 30 dias)',
                    data: data.data, // Dados são os valores somados de cada dia
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 2,
                    fill: false
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Uso de RAM (%)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Dias'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }).catch(function(error) {
        console.error('Erro ao renderizar o gráfico:', error);
    });
}




function renderiza_sistema_operacional(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('so_chart').getContext('2d');
        const cores = gera_cor(data.labels.length); // Gerar cores com base na quantidade de sistemas operacionais

        const myChart = new Chart(ctx, {
            type: 'bar', // Gráfico de barras
            data: {
                labels: data.labels, // Labels são os nomes dos sistemas operacionais
                datasets: [{
                    label: 'Quantidade por Sistema Operacional',
                    data: data.counts, // Dados são as quantidades de cada sistema operacional
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y', // Define o gráfico como barras horizontais
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    },
                    datalabels: {
                        display: true,
                        color: '#000', // Cor do texto das legendas
                        anchor: 'end', // Posição do texto nas barras
                        align: 'end', // Alinhamento do texto
                        formatter: (value) => value // Formatar o texto das legendas
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        suggestedMax: Math.max(...data.counts) + 10, // Adiciona um espaço extra
                        title: {
                            display: true,
                            text: 'Quantidade'
                        },
                        ticks: {
                            padding: 10 // Adiciona um padding extra para as legendas
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Sistemas Operacionais'
                        }
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            },
            plugins: [ChartDataLabels] // Adicionar o plugin datalabels
        });
    }).catch(function(error) {
        console.error('Erro ao renderizar o gráfico:', error);
    });
}





function renderiza_sistema_operacional_ii(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('so_chart').getContext('2d');
        const cores = gera_cor(data.labels.length); // Gerar cores com base na quantidade de sistemas operacionais

        const myChart = new Chart(ctx, {
            type: 'bar', // Gráfico de barras para os sistemas operacionais
            data: {
                labels: data.labels, // Labels são os nomes dos sistemas operacionais
                datasets: [{
                    label: 'Quantidade por Sistema Operacional',
                    data: data.counts, // Dados são as quantidades de cada sistema operacional
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Quantidade'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Sistemas Operacionais'
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }).catch(function(error) {
        console.error('Erro ao renderizar o gráfico:', error);
    });
}