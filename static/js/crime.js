const darkMode = localStorage.getItem('dark-mode') === 'true';
const body = document.body;
if (darkMode) {
    body.classList.add('dark-mode');
} else {
    body.classList.remove('dark-mode');
}
fetch('data/crimehead.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch CrimeHead.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('CrimeHead');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching crime:', error);
    });
    fetch('years.txt')
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
    fetch('data/crimehead.txt')
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch CrimeHead.txt');
        }
        return response.text();
    })
    .then(data => {
        const districts = data.trim().split('\n');
        const select = document.getElementById('crimehead');
        districts.forEach(district => {
            const option = document.createElement('option');
            option.text = district;
            select.add(option);
        });
    })
    .catch(error => {
        console.error('Error fetching crime:', error);
    });
    