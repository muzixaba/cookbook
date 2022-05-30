import React from 'react'
import PropTypes from 'prop-types'
 
export const Button = ({colour, text, onClick}) => {
  return (
    <button 
    onClick={onClick}
    style={{backgroundColor:colour}}
     className='btn'>{text}</button>
  )
}

Button.defaultProps = {
    colour: 'steelBlue'
}

Button.propTypes = {
    text: PropTypes.string,
    colour: PropTypes.string
}