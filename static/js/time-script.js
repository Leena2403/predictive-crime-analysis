const darkMode = localStorage.getItem('dark-mode') === 'true';
const body = document.body;
if (darkMode) {
    body.classList.add('dark-mode');
} else {
    body.classList.remove('dark-mode');
}
fetch('data/year.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch years.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('year');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching year:', error);
    });
fetch('data/crimegroup.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch CrimeGroups.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('crimegrp');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching year:', error);
    });

    document.getElementById('crime_grp').addEventListener('click', function() {
        const selectedCrimeGroup = document.getElementById('crimegrp').value;

        fetch(`/crime_data?crimegrp=${selectedCrimeGroup}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch crime data');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error fetching crime data:', error);
        });
    });

    document.getElementById('frequent').addEventListener('click', function() {
        const selectedCrimeGroup = document.getElementById('freq').value;

        fetch(`/frequency`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch frequency data');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error fetching frequency data:', error);
        });
    });