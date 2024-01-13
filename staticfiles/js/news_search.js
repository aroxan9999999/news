document.getElementById('searchQuery').addEventListener('input', function() {
    var query = this.value;
    if (query.length > 1) {
        fetch(`/search?q=${encodeURIComponent(query)}`)
            .then(response => response.text())
            .then(html => {
                document.getElementById('searchResults').innerHTML = html;
            })
            .catch(error => {
                console.error('Error during fetch:', error);
            });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var listItems = document.querySelectorAll('#searchResults li');

    listItems.forEach(function(item) {
        item.addEventListener('click', function() {
            var link = item.getAttribute('data-url');
            if (link) {
                window.location.href = link;
            }
        });
    });
});
