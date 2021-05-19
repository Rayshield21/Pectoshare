
const deletePostModal = document.querySelector('.deletePostModal')
const modalBody = document.querySelector('.modal-body')
const buttons = document.querySelectorAll('.deleteModalTrigger')
const deletePostForm = document.querySelector('.deletePostForm')
const deletePostModalOptions = {
  keyboard: true,
  backdrop: 'static',
  focus: true
}

const deletePostModalInstance = new bootstrap.Modal(deletePostModal, deletePostModalOptions)

let action_url = ''

buttons.forEach(button => {
  button.addEventListener('click', e => {
    // DOM traversal to imageWrapper's child nodes
    let postElements = button.parentElement.parentElement.parentElement.children
    for(element of postElements){
      action_url = button.getAttribute('data-deleteURL')
      if(element.classList.contains('imageItem')){
        modalBody.appendChild(element.cloneNode())
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