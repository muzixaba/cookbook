// Installing nodejs
/*
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/\
install.sh | bash

command -v nvm
*/


//Create react app
mkdir project_name && cd project_name
npx create-react-app app_name // --template typescript
cd app_name
npm start // starts dev server

// install axios for making requests
npm install axios

// install dotenv for environment variables
npm install dotenv --save

// React component (Function)
// Name components like PythonClasses
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

// Component States //

// ComponentDidMount
// When component is initialized

// ComponentDidUpdate
// When a component state changes

// ComponentWillUnmount
// When component gets destroyed


// Props - attributes or arguments used by components

// State
// Determines how a component renders and behaves
// App or Global state is available to the entire UI
// Functional components use hooks to manage state


// Hooks //
// Functions that hook into state and lifecycle features from function components
// Must be called at the top level of a function component
// useState - Returns a stateful value and a function to update it.
// Must be called in the exact sequence in which they are created.
// Don't put them inside control-flow
function myComponent() {
    // create state object
    // const [currentState, stateModifierFunct] = useState
    // useState returns array of two values (state var & state modifying function )
    // takes one optional argument, the default value/state
    const [counter, setCounter] = useState(0)

    // create state obj that gets ran only once
    const [items, setItems] = useState(() => {
        console.log("My items");  
    })

    function addCount() {
        setCounter(prevCount => prevCount + 1)
    }

    return (
        <>
        {counter}
        </>
    );
}

// useEffect //
/*
- takes in 2 arguments:
-    A function to run when component is mounter and or updated
-    An array of dependencies. If empty [], the function will only run @ init
- Component teardown code can be added as the returned value from useEffect
- Performs side effects in function components
- Normally used to do something when the page loads
*/
useEffect(() => {
    console.log("execute if other param changes")

    return () => {
        console.log("This will run cleanup")
    }
}, [otherParam])

// add function side effects
useEffect(() => {
    // run this block at mount
    console.log("execute on mount");
    // run return statement on unmount
    return () => {
        console.log("Run when component unmounts")
    };
},
    // rerun if one of components in array is updated
    // if empty array, function will only run at mount 
    [])

// useContext //
/*
- Gives access to React's context api
- Helps in sharing data without passing props
- Consumes value from nearest parent provider
*/

// useReducer

// useRef
/*


*/


// FETCHING DATA ONLINE //
// GET - Use built-in fetch()
const [data, setData] = useState();
useEffect(() => {
    fetch("url")
    .then((resp) => resp.json())
    .then((apiData) => {
        setData(apiData.message);
    });
}, []);

// POST - Use built-in fetch()
const [postResponse, setPostResponse] = useState();
fetch('url', {
  method: 'POST',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    parameterOne: 'something',
    parameterTwo: 'somethingElse'
  })
})
.then(response => response.json())
.then(setPostResponse(response.statusCode) );

// GET - axios (npm install axios)
const [apiData, setApiData] = useState();
useEffect(() => {
    axios.get("url").then((resp) => {
        setApiData(resp.data.message);
    });
}, []);

// POST - axios (npm install axios)
axios.post('/endpoint', {
    name: 'John Doe',
  })
  .then(function (response) {
    return response;
  })
  .catch(function (error) {
    return error;
  });

// build static assets for production
npm run build

// install serve http server glabally
npm install -g serve

// serve build folder locally on port 5000
serve -p 5000 -s build

// JSON-SERVER //
// install
npm install json-server
// add script in package.json
"server": "json-server --watch db.json --port 5000"
// run the json server
npm run server


// REACT-ROUTER
// https://reactrouter.com/docs/en/v6/getting-started/installation
npm install react-router-dom@6

// Index.js
import { BrowserRouter } from "react-router-dom";

root.render(
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </React.StrictMode>
  );

// App.js
import { Routes, Route, Link } from "react-router-dom";

function App() {
    return (
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="about" element={<About />} />
        </Routes>
      </div>
    );
  }


// Home.js
import { Link } from "react-router-dom";

function Home() {
    return (
      <>
        <main>
          <h2>Welcome to the homepage!</h2>
          <p>You can do this, I believe in you.</p>
        </main>
        <nav>
          <Link to="/about">About</Link>
        </nav>
      </>
    );
  }


// REACT-BOOTSTRAP
// installation
npm install react-boostrap bootstrap
// add link to react app
import 'bootstrap/dist/css/bootstrap.css';
// import a bootstrap component
import Button from 'react-bootrap/Button';
import { Button } from 'react-bootstrap';

// react-bootstrap-icons
//install
npm install react-bootstrap-icons --save

// usage
import { ArrowRight } from 'react-boostrap-icons';

export default function App() {
    return <ArrowRight color="royalblue" size={96} />;
}



// REACT ON AWS AMPLIFY

// Install UI toolkit for react
npm install aws-amplify @aws-amplify/ui-react

// index.js
import Amplify from 'aws-amplify';
import awsExports from './aws-exports'
Amplify.configure(awsExports)

// App.js
import Amplify, { API } from 'aws-amplify'
const myAPI = "apiName" //appName/amplify/backend/api/apiName
const path = "/items"

//Fetch from backend and update customers array
const [customers, setCustomers] = useState([])
  function getCustomer(e) {
    let customerId = e.input
    API.get(myAPI, path + "/" + customerId)
       .then(response => {
         console.log(response)
         let newCustomers = [...customers]
         newCustomers.push(response)
         setCustomers(newCustomers)
       })
       .catch(error => {
         console.log(error)
       })
  }