// POST FORM TEMPLATE
const imageInput = document.querySelector('.image_input');
const imagePreview = document.querySelector('.imagePreview')
if(imageInput){
  imageInput.addEventListener('change', e => {
    let { files } = e.target;
    if(files.length){
      imagePreview.classList.remove('hidden')
      let reader = new FileReader()
      reader.addEventListener('load', () => {
        imagePreview.innerHTML = `
          <img class='img-fluid img-thumbnail' src='${reader.result}'/>
        `
      }, false)
      reader.readAsDataURL(files[0])
    } else {
      imagePreview.classList.add('hidden')
    }
  })
}
