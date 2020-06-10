$(document).ready(function() {

    var itreator = 0;
    $("#defaultRegisterFormFirstName").keyup(function(e) {
        var nom = $("#defaultRegisterFormFirstName").val();
        if (nom.length < 4) {
            $(this).removeClass('mb-4 is-valid').addClass('is-invalid');
            $("#nom").removeClass('valid-feedback').addClass('invalid-feedback mb-4');
            $("#nom").text("Le nom doit avoir plus de 4 caractères");
            itreator++;

        } else {
            $(this).removeClass('mb-4 is-invalid').addClass('is-valid');
            $("#nom").removeClass('invalid-feedback').addClass('valid-feedback mb-4');
            $("#nom").text("");
        }
    });
    $("#defaultRegisterFormLastName").keyup(function(e) {
        var nom = $("#defaultRegisterFormLastName").val();
        if (nom.length < 4) {
            $(this).removeClass('mb-4 is-valid').addClass('is-invalid');
            $("#post").removeClass('valid-feedback').addClass('invalid-feedback mb-4');
            $("#post").text("Le nom doit avoir plus de 4 caractères");
            itreator++;
        } else {
            $(this).removeClass('mb-4 is-invalid').addClass('is-valid');
            $("#post").removeClass('invalid-feedback').addClass('valid-feedback mb-4');
            $("#post").text("");
        }
    });
    $("#defaultRegisterFormEmail").keyup(function(e) {
        var nom = $("#defaultRegisterFormEmail").val();
        if (nom.length < 4) {
            $(this).removeClass('mb-4 is-valid').addClass('is-invalid');
            $("#email").removeClass('valid-feedback').addClass('invalid-feedback mb-4');
            $("#email").text("L'adresse email  doit avoir plus de 4 caractères");
            itreator++;

        } else {
            $(this).removeClass('mb-4 is-invalid').addClass('is-valid');
            $("#email").removeClass('invalid-feedback').addClass('valid-feedback mb-4');
            $("#email").text("");
        }
    });

    $("#defaultRegisterPhone").keyup(function(e) {
        var nom = $("#defaultRegisterPhone").val();
        if (nom.length < 10) {
            $(this).removeClass('mb-4 is-valid').addClass('is-invalid');
            $("#tel").removeClass('valid-feedback').addClass('invalid-feedback mb-4');
            $("#tel").text("Numero invalide");
            iterator++;
        } else {
            $(this).removeClass('mb-4 is-invalid').addClass('is-valid');
            $("#tel").removeClass('invalid-feedback').addClass('valid-feedback mb-4');
            $("#tel").text("");
        }
    });
    $("#nationalite").keyup(function(e) {
        var nom = $("#nationalite").val();
        if (nom.length < 4) {
            $(this).removeClass('mb-4 is-valid').addClass('is-invalid');
            $("#nat").removeClass('valid-feedback').addClass('invalid-feedback mb-4');
            $("#nat").text("La nationalite doit avoir plus de 4 caractères");
            itreator++;
        } else {
            $(this).removeClass('mb-4 is-invalid').addClass('is-valid');
            $("#nat").removeClass('invalid-feedback').addClass('valid-feedback mb-4');
            $("#nat").text("");
        }
    });
    $("#adresse").keyup(function(e) {
        var nom = $("#adresse").val();
        if (nom.length < 4) {
            $(this).removeClass('mb-4 is-valid').addClass('is-invalid');
            $("#addr").removeClass('valid-feedback').addClass('invalid-feedback mb-4');
            $("#addr").text("L'adresse doit avoir plus de 4 caractères");
            iterator++;
        } else {
            $(this).removeClass('mb-4 is-invalid').addClass('is-valid');
            $("#addr").removeClass('invalid-feedback').addClass('valid-feedback mb-4');
            $("#addr").text("");
        }
    });

    if (iterator > 0) {
        $("#save").Attr("disabled", "disabled");
    } else $("#save").RemoveAttr("disabled", "disabled");

});