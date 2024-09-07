document.addEventListener('DOMContentLoaded', function () {
    // Function handles taking project id from loop and passing to modal
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    document.querySelectorAll('.btn-outline-danger.float-end').forEach(function (button) {
        button.addEventListener('click', function () {
            var deleteUrl = button.getAttribute('data-project-url');
            var projectId = button.getAttribute('data-project-id');
            var projectIdInput = document.getElementById('projectIdInput');
            projectIdInput.value = projectId;
            var deleteForm = document.getElementById('deleteForm');
            deleteForm.action = deleteUrl;
            console.log('Delete', projectId);
            deleteModal.show();
        });
    });
});
