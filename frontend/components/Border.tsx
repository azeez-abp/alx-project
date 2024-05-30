import React from 'react'
const style_border  ={
    border: '3px solid #fff',
    padding: '5px',
    display: 'flex',
    borderRadius: '4px'
}
const Border = ({...props}) => {
  return (
    <div className='button-outline' style={{...style_border, ...props.styles_border}} >
        {props.children?props.children:<></>}
    </div>
  )
}

export default Border