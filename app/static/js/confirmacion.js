function confirmarEliminar(id){
    Swal.fire({
        title: '¿Estás seguro?',
        text: "Esta acción no puede deshacerse.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/products/eliminar/"+id+"/";
        }
      })
}