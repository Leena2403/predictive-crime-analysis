const darkMode = localStorage.getItem('dark-mode') === 'true';
const body = document.body;
if (darkMode) {
    body.classList.add('dark-mode');
} else {
    body.classList.remove('dark-mode');
}
fetch('data/unitname.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch UnitName.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('unitname');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching unit name:', error);
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
        const select = document.getElementById('crimegroup');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching crime:', error);
    });
    fetch('data/beatname.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch BeatName.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('BeatName');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching beat:', error);
    });