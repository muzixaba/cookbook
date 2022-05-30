// Installing nodejs
/*
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/\
install.sh | bash

command -v nvm
*/


//Create react app
mkdir project_name && cd project_name
npx create-react-app app_name
cd app_name
npm start // starts dev server

// install axios for making requests
npm install axios


// React component (Function)
export const Header = () => {
    return (
        <div><h1>My Header</h1></div>
    )
}


// React component (Class)
export default class Header extends React.Component {
    render() {
        <div><h1>My Header</h1></div>
    }
}

// Props - attributes or arguments used by components

// State
// Determines how a component renders and behaves
// App or Global state is available to the entire UI
// Functional components use hooks to manage state


// Hooks
// Functions that hook into state and lifecycle features from function components
// useState - Returns a stateful value and a function to update it.
// useEffect - Performs side effects in function components
// useContext
// useReducer
// useRef