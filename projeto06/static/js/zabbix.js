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
                    label: 'Sistema Operacional',
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
                            display: false,
                            text: 'Quantidade'
                        },
                        ticks: {
                            padding: 10 // Adiciona um padding extra para as legendas
                        }
                    },
                    y: {
                        title: {
                            display: false,
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

function renderiza_servidor_tip(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('st_chart').getContext('2d');
        const cores = gera_cor(data.labels.length); // Gerar cores com base na quantidade de tipos de servidores

        const myChart = new Chart(ctx, {
            type: 'bar', // Gráfico de barras verticais
            data: {
                labels: data.labels, // Labels são os nomes dos tipos de servidores
                datasets: [{
                    label: 'Tipo de Servidor',
                    data: data.counts.map(count => count + 10), // Adicionar 10 a cada valor
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
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
                        formatter: (value) => value // Formatar o texto das legendas para mostrar o valor exato
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        suggestedMax: Math.max(...data.counts.map(count => count + 10)) + 10, // Adiciona espaço extra no topo
                        title: {
                            display: false,
                            text: 'Quantidade'
                        },
                        ticks: {
                            padding: 10 // Adiciona padding extra para as legendas
                        }
                    },
                    x: {
                        title: {
                            display: false,
                            text: 'Tipo de Servidor'
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

function renderiza_monito_zabbix(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        // Converter valores booleanos para "Sim" e "Não"
        const labels = data.labels.map(label => label === true ? 'Sim' : 'Não');
        const ctx = document.getElementById('mz_chart').getContext('2d');
        const cores = gera_cor(labels.length); // Gerar cores com base na quantidade de respostas "Sim" e "Não"

        const myChart = new Chart(ctx, {
            type: 'pie', // Gráfico de pizza
            data: {
                labels: labels, // Labels são "Sim" e "Não"
                datasets: [{
                    label: 'Monitorado pelo Zabbix',
                    data: data.counts, // Dados são as quantidades de "Sim" e "Não"
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    },
                    datalabels: {
                        display: true,
                        color: '#000', // Cor do texto nas fatias
                        formatter: (value, context) => {
                            const label = context.chart.data.labels[context.dataIndex];
                            return `${label}: ${value}`; // Exibir "Sim" ou "Não" com o valor
                        }
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            },
            plugins: [ChartDataLabels] // Adicionar o plugin datalabels para mostrar os valores
        });
    }).catch(function(error) {
        console.error('Erro ao renderizar o gráfico:', error);
    });
}


function renderiza_srv_backup(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        // Converter valores booleanos para "Sim" e "Não"
        const labels = data.labels.map(label => label === true ? 'Sim' : 'Não');
        const ctx = document.getElementById('sb_chart').getContext('2d');
        const cores = gera_cor(labels.length); // Gerar cores com base na quantidade de respostas "Sim" e "Não"

        const myChart = new Chart(ctx, {
            type: 'pie', // Gráfico de pizza
            data: {
                labels: labels, // Labels são "Sim" e "Não"
                datasets: [{
                    label: 'Monitorado pelo Zabbix',
                    data: data.counts, // Dados são as quantidades de "Sim" e "Não"
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    },
                    datalabels: {
                        display: true,
                        color: '#000', // Cor do texto nas fatias
                        formatter: (value, context) => {
                            const label = context.chart.data.labels[context.dataIndex];
                            return `${label}: ${value}`; // Exibir "Sim" ou "Não" com o valor
                        }
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            },
            plugins: [ChartDataLabels] // Adicionar o plugin datalabels para mostrar os valores
        });
    }).catch(function(error) {
        console.error('Erro ao renderizar o gráfico:', error);
    });
}


function renderiza_origem_data(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('or_chart').getContext('2d');
        const cores = gera_cor(data.labels.length); // Gerar cores com base na quantidade de tipos de servidores

        const myChart = new Chart(ctx, {
            type: 'bar', // Gráfico de barras verticais
            data: {
                labels: data.labels, // Labels são os nomes dos tipos de servidores
                datasets: [{
                    label: 'Oriem do dados',
                    data: data.counts.map(count => count + 10), // Adicionar 10 a cada valor
                    backgroundColor: cores[0],
                    borderColor: cores[1],
                    borderWidth: 1
                }]
            },
            options: {
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
                        formatter: (value) => value // Formatar o texto das legendas para mostrar o valor exato
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        suggestedMax: Math.max(...data.counts.map(count => count + 10)) + 10, // Adiciona espaço extra no topo
                        title: {
                            display: false,
                            text: 'Quantidade'
                        },
                        ticks: {
                            padding: 10 // Adiciona padding extra para as legendas
                        }
                    },
                    x: {
                        title: {
                            display: false,
                            text: 'Tipo de Servidor'
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

function renderiza_evolucao_volume_dado(url) {
    fetch(url, {
        method: 'get',
    }).then(function(result) {
        return result.json();
    }).then(function(data) {
        const ctx = document.getElementById('ev_chart').getContext('2d');
        const cores = gera_cor(data.labels.length); // Gerar cores com base na quantidade de sistemas operacionais

        const myChart = new Chart(ctx, {
            type: 'line', // Gráfico de linhas
            data: {
                labels: data.labels, // Labels são os nomes dos sistemas operacionais
                datasets: [{
                    label: 'Sistema Operacional',
                    data: data.counts, // Dados são as quantidades de cada sistema operacional
                    backgroundColor: cores[0], // Cor de fundo para a área abaixo da linha
                    borderColor: cores[1], // Cor da linha
                    borderWidth: 2, // Largura da linha
                    fill: false // Não preencher a área abaixo da linha
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                    },
                    datalabels: {
                        display: true,
                        color: '#000', // Cor do texto das legendas
                        formatter: (value) => value // Formatar o texto das legendas
                    }
                },
                scales: {
                    x: {
                        title: {
                            display: true,
                            text: 'Sistemas Operacionais'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Quantidade'
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
