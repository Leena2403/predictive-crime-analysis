
document.addEventListener('DOMContentLoaded', () => {
    fetch('data/district.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch unique_districts.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('District');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching districts:', error);
    })

fetch('/data/year.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch years.txt');
        }
        return response.text();
    })
    .then(data => {
        const years = data.trim().split('\n');
        const select = document.getElementById('Year');
        years.forEach(year => {
            const option = document.createElement('option');
            option.text = year;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching years:', error);
    });

const darkMode = localStorage.getItem('dark-mode') === 'true';
const body = document.body;
if (darkMode) {
    body.classList.add('dark-mode');
} else {
    body.classList.remove('dark-mode');
}
document.getElementById('districtAnalysisBtn').addEventListener('click', function() {
    document.getElementById('districtForm').submit();
    
});

// Add event listener for the analysis button
document.getElementById('yearAnalysisBtn').addEventListener('click', function() {
    const district = document.getElementById('district').value;
    const year = document.getElementById('year').value;
   
    fetch('/analysis', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ district: district, year: year })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        return response.json();
    })
    .then(data => {
        // Process the received data and render the chart
        renderChart(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// added from gchat
let chart = null;

    document.getElementById('yearAnalysisBtn').addEventListener('click', function() {
        const selectedDistrict = document.getElementById('district').value;
        const selectedYear = document.getElementById('year').value;
        
        fetch('Datasets/FIR_Details_Data.csv')
        .then(response => response.text())
        .then(csv => {
            const data = [];
            const labels = [];
            const rows = csv.split('\n');
            for (let i = 1; i < rows.length; i++) {
                const row = rows[i].split(',');
                const year = parseInt(row[4]);
                const district = row[0];
                const crimeGroup = row[9];
                if (year === parseInt(selectedYear) && district === selectedDistrict) {
                    data.push(crimeGroup);
                }
            }

            const counts = data.reduce((acc, val) => {
                acc[val] = (acc[val] || 0) + 1;
                return acc;
            }, {});

            const crimeCounts = Object.entries(counts)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 17);

            const crimeLabels = crimeCounts.map(([crimeGroup]) => crimeGroup);
            const crimeValues = crimeCounts.map(([, count]) => count);

            const ctx = document.getElementById('crimeChart').getContext('2d');
            
            if (chart) {
                chart.destroy();
            }

            chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: crimeLabels,
                    datasets: [{
                        label: 'Frequency of Crimes',
                        data: crimeValues,
                        backgroundColor: 'seagreen'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    title: {
                        display: true,
                        text: `Top Crimes in ${selectedDistrict} during ${selectedYear}`
                    },
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                autoSkip: false
                            }
                        }]
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error fetching CSV:', error);
        });

    });
fetch('/district_crimes', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ district: selectedDistrict, year: selectedYear })
})
.then(response => response.text())
.then(html => {
    const newWindow = window.open();
    newWindow.document.open();
    newWindow.document.write(html);
    newWindow.document.close();
})
.catch(error => {
    console.error('Error fetching district crimes:', error);
    throw new Error('Failed to fetch district crimes map');
})
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch district crimes map');
    }
    return response.blob();
})
.then(blob => {
    const url = URL.createObjectURL(blob);
    window.open(url, '_blank');
})
.catch(error => {
    console.error('Error fetching district crimes:', error);
});

});

