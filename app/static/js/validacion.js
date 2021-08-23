
$(document).ready(function () {

    // Validaciones formulario registro
    $("#form-register").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            contraseña2:{
                equalTo: "#clave"
            }

        },
        messages: {
            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido'
            },
            nombre: {
                required: 'Debe ingresar su nombre'

            },
            contraseña: {
                required: 'Debe ingresar su nueva contraseña',
                minlength: 'La contraseña debe tener minimo 6 caracteres'
            },
            contraseña2:{
                required: 'Debe re-ingresar su nueva contraseña',
                minlength: 'La contraseña debe tener minimo 6 caracteres',
                equalTo:'Las contraseñas deben coincidir'
            },
            fecha :{
                required:'Debe ingresar su fecha de nacimiento',
                max:'Debe ser mayor de 14 años'
            },
            user:{
                required:'Debe crear un nombre de usuario',
                minlength:'El nombre de usuario debe ser mayor a 4 caracteres'
            }

        }

    });



    // Validaciones formulario login 
    $("#form-login").validate({
        rules: {
            usuario: {
                required: true,
            },
            contraseñaLogin:{
                required:true,
            }

        },
        messages: {
            contraseñaLogin:{
                required: 'Debe ingresar su contraseña',

            },
            usuario :{
                required:'Debe ingresar su nombre de usuario',

                
            }

        }

    });
    
 });


 $("#form-register").submit(function(){
    if($("#form-register").valid()){
        Swal.fire({
            type: 'success',
            title: 'Registro finalizado',
            text: 'Has sido registrado exitosamente!.',

        })
    }else{
        Swal.fire({
            type: 'warning',
            title: 'Formulario incompleto',
            text: 'Para registrarte debes llenar completamente el formulario',

        })
    }
    return false
})


$("#form-login").submit(function(){
    if($("#form-login").valid()){
        Swal.fire({
            type: 'success',
            title: 'Se ha iniciado sesión correctamente',
            text:''
            
        })
        $(location).attr('href', "index.html")
        
    }else{
        Swal.fire({
            type: 'warning',
            title: 'Ingrese sus datos para iniciar sesión',
            text: '',

        })
    }
    return false
})



