function createProductCard(product) {
    const card = document.createElement('div');
    card.classList.add('product-card');

    const image = document.createElement('img');
    image.src = product.Image;
    card.appendChild(image);

    const title = document.createElement('h3');
    title.textContent = product.Product;
    card.appendChild(title);

    const price = document.createElement('p');
    price.textContent = `Price: ${product.Price}`;
    card.appendChild(price);

    const description = document.createElement('p');
    description.textContent = `Description: ${product.Description}`;
    card.appendChild(description);

    const availability = document.createElement('p');
    availability.textContent = `Availability: ${product.Availability}`;
    card.appendChild(availability);

    const rating = document.createElement('p');
    rating.textContent = `Rating: ${product.Rating}`;
    card.appendChild(rating);

    const reviews = document.createElement('p');
    reviews.textContent = `Reviews: ${product.Reviews}`;
    card.appendChild(reviews);

    return card;
}

function displayResults(results) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    const keyword = Object.keys(results)[0]; // Extract the keyword used for search
    const products = results[keyword];

    products.forEach((product) => {
        const card = createProductCard(product);
        resultsDiv.appendChild(card);
    });
}

function displayLoader() {
    const loader = document.createElement('div');
    loader.classList.add('loader');
    document.getElementById('results').innerHTML = '';
    document.getElementById('results').appendChild(loader);
}

function removeLoader() {
    const loader = document.querySelector('.loader');
    if (loader) {
        loader.remove();
    }
}

function searchProducts() {
    const keyword = document.getElementById('keyword').value.trim();
    if (keyword === '') {
        alert('Please enter a keyword to search.');
        return;
    }

    displayLoader();

    fetch('http://localhost:5000/api/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ keyword: keyword }),
    })
        .then((response) => response.json())
        .then((data) => {
            displayResults(data);
            removeLoader();
        })
        .catch((error) => {
            console.error('Error:', error);
            removeLoader();
        });
}

document.getElementById('keyword').addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        searchProducts();
    }
});