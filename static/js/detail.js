// Detail Template
const stretchedLink = document.querySelector('.stretched-link')
const imageWrapper = document.querySelector('.imageWrapper')
window.addEventListener('DOMContentLoaded', () =>{

  if(stretchedLink.classList.contains('zoom-in')){
    imageWrapper.classList.add('zoomed-out')
  }
})

stretchedLink.addEventListener('click', (e)=>{
  const zoomToggle = (cursor) => {
    let currentState = {cursor: '', mode: ''}
    let prevState = {cursor: '', mode: ''}
    if(cursor === 'zoom-in'){
      prevState.cursor = 'zoom-in',
      prevState.mode = 'zoomed-out'
      currentState.cursor = 'zoom-out',
      currentState.mode = 'zoomed-in'
    } else {
      prevState.cursor = 'zoom-out',
      prevState.mode = 'zoomed-in'
      currentState.cursor = 'zoom-in',
      currentState.mode = 'zoomed-out'
    }
    e.target.classList.remove(prevState.cursor)
    imageWrapper.classList.remove(prevState.mode)
    e.target.classList.add(currentState.cursor)
    imageWrapper.classList.add(currentState.mode)
  }
  if(e.target.classList.contains('zoom-in')){
    state = zoomToggle('zoom-in')
    zoomToggle('zoom-in')
  } else {
    zoomToggle('zoom-out')
  }
})