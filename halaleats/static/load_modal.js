document.addEventListener('DOMContentLoaded', function () {
    // Function handles taking image url from loop and passing to modal
    var certificateModal = new bootstrap.Modal(document.getElementById('imageModal'));
    document.querySelectorAll('.btn-dark.float-end').forEach(function (button) {
        button.addEventListener('click', function () {
            var certificateImage = document.getElementById('certificateImage');
            var certificateUrl = button.getAttribute('data-certificate-url');
            certificateImage.src = certificateUrl;
            certificateModal.show();
        });
    });

    // Function handles taking eatery id from loop and passing to modal
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    document.querySelectorAll('.btn-outline-danger.float-end').forEach(function (button) {
        button.addEventListener('click', function () {
            var deleteUrl = button.getAttribute('data-eatery-url');
            var eateryId = button.getAttribute('data-eatery-id');
            var eateryIdInput = document.getElementById('eateryIdInput');
            eateryIdInput.value = eateryId;
            var deleteForm = document.getElementById('deleteForm');
            deleteForm.action = deleteUrl;
            console.log('Delete', eateryId);
            deleteModal.show();
        });
    });
});
