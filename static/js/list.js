
// List Template

const gridImageItem = document.querySelectorAll('.grid .imageWrapper .imageItem');

// render as portrait or landscape depending on the image file original dimension 
// imageItem.forEach(item=> {
//   let img = new Image()
//   img.addEventListener('load', ({target:{width, height}})=> {
//     console.log(`${width} x ${height}`)
//     console.log(width-height)
//     if(width > height && (width - height) >= 130){
//       item.parentNode.classList.add('landscape')
//     } else {
//       if(width >= 350 && width <= 1000){
//         item.parentNode.classList.add('big')
//       } 
//     }
//   })
//   img.src = item.getAttribute('src')
// })

function getSpan(size){
  if(size > 700){
    return 3;
  } else if(size > 400){
    return 2;
  } else {
    return 1;
  }
  // return size > 250 ? 2 : 1;
}

gridImageItem.forEach(item=> {
  let img = new Image()
  img.addEventListener('load', ({target:{width, height}})=> {
    console.log(`${width} x ${height}`)
    let { style: gridItemStyle } = item.parentElement
    gridItemStyle.gridColumnEnd = `span ${getSpan(width)}`
    gridItemStyle.gridRowEnd = `span ${getSpan(height)}`
  })
  img.src = item.getAttribute('src')
})