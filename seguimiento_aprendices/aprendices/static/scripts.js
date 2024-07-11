document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete-btn');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            if (!confirm("¿Estás seguro de que deseas eliminar este aprendiz?")) {
                event.preventDefault();
            }
        });
    });
});
