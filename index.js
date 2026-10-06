

let logout = document.querySelector('.logout');

if (logout) {
    logout.addEventListener('click', function () {
        showToast('Logout successfully');
    });
}

function showToast(message) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    toast.textContent = message;
    toast.style.display = 'block';
    setTimeout(() => {
        toast.style.display = 'none';
    }, 3000);
}



