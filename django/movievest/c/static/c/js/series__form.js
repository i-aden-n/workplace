document.addEventListener('DOMContentLoaded', ()=>{
    const fileInput = document.getElementById('file_input')
    const fileName = document.getElementById('file_name')
    fileInput.addEventListener('change', (e)=>{
        fileName.innerHTML = `Choosed file: ${e.target.files[0].name}`
    })
})