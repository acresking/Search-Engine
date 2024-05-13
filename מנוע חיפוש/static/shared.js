// JavaScript for showing/hiding login modal
document.addEventListener('DOMContentLoaded', function () {
    var loginButton = document.getElementById('login-button');
    var loginModal = document.getElementById('login-modal');
    var closeModal = document.getElementById('close-modal');
    var loginRedirectButton = document.getElementById('login-redirect-button');
    var registrationRedirectButton = document.getElementById('registration-redirect-button');

    // Show modal when login button is clicked
    loginButton.addEventListener('click', function () {
        loginModal.style.display = 'block';
    });

    // Hide modal when close button is clicked
    closeModal.addEventListener('click', function () {
        loginModal.style.display = 'none';
    });

    // Redirect to login page
    loginRedirectButton.addEventListener('click', function () {
        window.location.href = 'login.html';
    });

    // Redirect to registration page
    registrationRedirectButton.addEventListener('click', function () {
        window.location.href = 'registration.html';
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var loginButton = document.getElementById('login-button');
    var loginModal = document.getElementById('login-modal');
    var closeModal = document.getElementsByClassName('close-modal')[0];

    // Show modal when login button is clicked
    loginButton.addEventListener('click', function () {
        loginModal.style.display = 'block';
    });

    // Hide modal when close button is clicked
    closeModal.addEventListener('click', function () {
        loginModal.style.display = 'none';
    });
});
