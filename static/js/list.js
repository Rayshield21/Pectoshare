
// List Template

const imageItem = document.querySelectorAll('.imageItem');

// render as portrait or landscape depending on the image file original dimension 
imageItem.forEach(item=> {
  let img = new Image()
  img.addEventListener('load', ({target:{width, height}})=> {
    console.log(`${width} x ${height}`)
    if(width > height && (width - height) > 150){
      item.parentNode.classList.add('landscape')
    } else {
      if(width > 350 && width < 1000){
        item.parentNode.classList.add('big')
      } 
    }
  })
  img.src = item.getAttribute('src')
  // console.log(item.getAttribute('src'))
})

// detail