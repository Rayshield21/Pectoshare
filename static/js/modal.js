
// DELETE MODAL 

const deletePostModal = document.querySelector('.deletePostModal')
const deleteModalBody = document.querySelector('.deletePostModal > .modal-body')
const deleteButtons = document.querySelectorAll('.deleteModalTrigger')
const deletePostForm = document.querySelector('.deletePostForm')
const deletePostModalOptions = {
  keyboard: true,
  backdrop: 'static',
  focus: true
}

const deletePostModalInstance = new bootstrap.Modal(deletePostModal, deletePostModalOptions)

let action_url = ''

deleteButtons.forEach(button => {
  button.addEventListener('click', e => {
    // DOM traversal to imageWrapper's child nodes
    let postElements = button.parentElement.parentElement.parentElement.children
    for(element of postElements){
      action_url = button.getAttribute('data-deleteURL')
      if(element.classList.contains('imageItem')){
        deleteModalBody.appendChild(element.cloneNode())
      }
    }
    deletePostModalInstance.toggle()
  })
})

deletePostModal.addEventListener('show.bs.modal', ()=> {
  deletePostForm.setAttribute('action', action_url)
})

deletePostModal.addEventListener('hidden.bs.modal', ()=> {
  action_url = ''
  modalBody.innerHTML = ''
  deletePostForm.setAttribute('action', action_url)
})

// ZOOM MODAL 

const zoomModal = document.querySelector('.zoomModal')
const zoomModalBody = document.querySelector('.zoomModal .modal-dialog .modal-content > .modal-body')
const zoomButton = document.querySelector('.zoomModalTrigger')
const zoomModalOptions = {
  keyboard: true,
  backdrop: 'static',
  focus: true
}

const zoomPostModalInstance = new bootstrap.Modal(zoomModal, zoomModalOptions)

zoomButton.addEventListener('click', e => {
  e.preventDefault()
  let postElements = e.target.parentElement.children
  for(element of postElements){
    console.log(element)
    if(element.classList.contains('imageItem')){
      let newElement = element.cloneNode()
      zoomModalBody.appendChild(newElement)
    }
  }
  zoomPostModalInstance.toggle()
})

zoomModal.addEventListener('hidden.bs.modal', ()=> {
  zoomModalBody.innerHTML = ''
})