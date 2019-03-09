function changeToLogin() {
    var register = document.getElementById('register');
    register.style.display = 'none';
    var login = document.getElementById('login');
    login.style.display = 'block';
    // login.style.transform = 'rotateY(180deg)';
    // login.style.transformStyle = 'preserve-3d';
    // login.style.transition = 'transform 0.8s'
}

function changeToRegister() {
    var register = document.getElementById('register');
    register.style.display = 'block';
    var login = document.getElementById('login');
    login.style.display = 'none';
}