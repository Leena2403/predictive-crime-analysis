const darkMode = localStorage.getItem('dark-mode') === 'true';
const body = document.body;
if (darkMode) {
    body.classList.add('dark-mode');
} else {
    body.classList.remove('dark-mode');
}
fetch('data/district.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch Districts.txt');
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
    });

fetch('data/year.txt')
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch years.txt');
    }
    return response.text();
})
.then(data => {
    const districts = data.trim().split('\n');
    const select = document.getElementById('Year');
    districts.forEach(district => {
        const option = document.createElement('option');
        option.text = district;
        select.add(option);
    });
})
.catch(error => {
    console.error('Error fetching years:', error);
});

fetch('data/fir.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch fir.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('FIRNo');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching FIR no.:', error);
    });
fetch('data/crimesno.txt')
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch crimesno.txt');
    }
    return response.text();
})
.then(data => {
    const districts = data.trim().split('\n');
    const select = document.getElementById('CrimeNo');
    districts.forEach(district => {
        const option = document.createElement('option');
        option.text = district;
        select.add(option);
    });
})
.catch(error => {
    console.error('Error fetching crime no:', error);
});
fetch('data/crimesno.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch crimesno.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('CrimesNo');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching crime no.:', error);
    });
fetch('data/arrested.txt')
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch arrested.txt');
    }
    return response.text();
})
.then(data => {
    const districts = data.trim().split('\n');
    const select = document.getElementById('arrestid');
    districts.forEach(district => {
        const option = document.createElement('option');
        option.text = district;
        select.add(option);
    });
})
.catch(error => {
    console.error('Error fetching arrest ids:', error);
});

fetch('data/unitid.txt')
.then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch unitid.txt');
    }
    return response.text();
})
.then(data => {
    const districts = data.trim().split('\n');
    const select = document.getElementById('Unitid');
    districts.forEach(district => {
        const option = document.createElement('option');
        option.text = district;
        select.add(option);
    });
})
.catch(error => {
    console.error('Error fetching unit ids:', error);
});

// document.getElementById('District').addEventListener('change', function() {
//     const selectedDistrict = this.value;
//     fetch('/FIR_Details_Data.csv')
//         .then(response => response.text())
//         .then(data => {
//             const rows = data.trim().split('\n');
//             const units = new Set();
//             rows.forEach(row => {
//                 const columns = row.split(',');
//                 if (columns.length >= 2) {
//                     const district = columns[0].trim();
//                     const unitName = columns[1].trim();
//                     if (district === selectedDistrict) {
//                         units.add(unitName);
//                     }
//                 }
//             });
//             const select = document.getElementById('UnitName');
//             select.innerHTML = '';
//             units.forEach(unit => {
//                 const option = document.createElement('option');
//                 option.text = unit;
//                 select.add(option);
//             });
//         })
//         .catch(error => {
//             console.error('Error fetching unit names:', error);
//         });
// });

document.getElementById('ConfidenceMatrix').addEventListener('click', function() {
    const selectedDistrict = document.getElementById('District').value;
    const selectedUnit = document.getElementById('UnitName').value;
    const selectedCrimeNo = document.getElementById('CrimeNo').value;
    const selectedMonth = document.getElementById('Month').value;
    const selectedYear = document.getElementById('Year').value;

    const data = {
        'District': selectedDistrict,
        'UnitName': selectedUnit,
        'CrimeNo': selectedCrimeNo,
        'Month': selectedMonth,
        'Year': selectedYear
    };

    fetch('/process_confidence_matrix', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    })
    .catch(error => {
        console.error('Error processing Confidence Matrix:', error);
    });
});
document.getElementById('arrestID').addEventListener('click', function() {
    const selectedArrestID = document.getElementById('arrestid').value;

    const data = {
        'arrestid': selectedArrestID
    };

    fetch('/arrest_id', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    })
    .catch(error => {
        console.error('Error fetching Arrest IDs Data:', error);
    });
});
document.getElementById('criminalprediction').addEventListener('click', function() {
    const selectedCrimesNo = document.getElementById('CrimesNo').value;
    const selectedUnitid = document.getElementById('Unitid').value;

    const data = {
        'CrimesNo': selectedCrimesNo,
        'Unitid': selectedUnitid
    };

    fetch('/criminal_prediction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log(result);
    })
    .catch(error => {
        console.error('Error fetching Criminal Prediction data:', error);
    });
});