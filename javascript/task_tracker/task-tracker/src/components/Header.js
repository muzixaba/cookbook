import React from "react"
import PropTypes from 'prop-types'

import {Button} from './Button'

export const Header = ({title, onAdd, showAdd}) => {
  return (
    <header className='header'>
        <h1>{title}</h1>
        <Button 
        text={showAdd ? 'Close' : 'Add'}
        colour={showAdd ? 'red' : 'green'}
         onClick={onAdd}/>
    </header>
  )
}

Header.defaultProps = {
    title: 'The Task Tracker',
}

Header.propTypes = {
    onClick: PropTypes.func
}
