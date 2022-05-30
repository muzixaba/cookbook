import React from "react"
import PropTypes from 'prop-types'

import {Button} from './Button'

export const Header = ({title}) => {
    const onClick = () => {
        console.log('Clicked button')
    }
  return (
    <header className='header'>
        <h1>{title}</h1>
        <Button text='Add' onClick={onClick}/>
    </header>
  )
}

Header.defaultProps = {
    title: 'The Task Tracker',
}

Header.propTypes = {
    onClick: PropTypes.func
}
