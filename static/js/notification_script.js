function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        const notification = document.querySelector('.notification');
        notification.textContent = 'Текст скопирован';
        notification.style.display = 'block';
        notification.style.opacity = 1;

        setTimeout(() => {
            notification.style.opacity = 0;
            setTimeout(() => {
                notification.style.display = 'none';
            }, 500);
        }, 2000);
    }).catch(err => {
        console.error('Ошибка копирования: ', err);
    });
}
