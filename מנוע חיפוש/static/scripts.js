function toggleClearButton() {
    var searchBox = document.querySelector('.search-box');
    var clearButton = document.querySelector('.clear-button');
    clearButton.style.display = searchBox.value ? 'block' : 'none';
}

function clearSearchBox() {
    var searchBox = document.querySelector('.search-box');
    searchBox.value = '';
    toggleClearButton();
}

function changeLanguage(langCode) {
    var selectedLanguage = document.getElementById('selected-language');
    var langText = document.querySelector('#lang-dropdown option[value="' + langCode + '"]').innerText;
    selectedLanguage.innerText = 'Selected Language: ' + langText;

    // Set text direction based on the selected language
    document.body.dir = getDirection(langCode);
}

function getDirection(langCode) {
    // Define text direction based on language code
    // Return 'rtl' for right-to-left languages and 'ltr' for left-to-right languages
    switch (langCode) {
        case 'ar':
        case 'he':
        case 'fa':
            return 'rtl';
        default:
            return 'ltr';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    var searchForm = document.querySelector('.search-box-container form');
    var searchBox = document.querySelector('.search-box');

    searchForm.addEventListener('submit', function (event) {
        var inputValue = searchBox.value.trim();

        // Check if the input starts with a valid protocol
        if (/^(?:https?|ftp):\/\//i.test(inputValue)) {
            // If it's a valid URL, prevent the default form submission
            event.preventDefault();
            // Redirect directly to the URL
            window.location.href = inputValue;
        } else {
            // Perform the search action for regular search terms
            performSearch(inputValue);
            event.preventDefault(); // Prevent the default form submission
        }
    });

    // Function to perform the search action
    function performSearch(query) {
        // Implement the search functionality here for regular search terms
        alert("Perform search for query: " + query);
    }
});

