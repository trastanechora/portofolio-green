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

function nextStepTransaction() {
    var bank = document.getElementsByName('bank-option').values
    console.log(bank)
    var step_1 = document.getElementsByClassName('step-1')[0]
    step_1.style.display = 'none'
    var step_2 = document.getElementsByClassName('step-2')[0]
    step_2.style.display = 'block'
}