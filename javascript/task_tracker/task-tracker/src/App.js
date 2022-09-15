import React from 'react'
import {Header} from './components/Header'
import {Tasks} from './components/Tasks'
import {AddTask} from './components/AddTask'
import {Footer} from './components/Footer'
import {About} from './components/About'
import {useState, useEffect} from 'react'
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

function App() {
  const [showAddTask, setShowAddTask] = useState(true)
  const [tasks, setTasks] = useState(
    [
        {id: 1, text: 'Doctors appointment',
        day: 'Feb 5th at 2:30pm', reminder: true},
        {id: 2, text: 'School meeting',
        day: 'Feb 6th at 3:30pm', reminder: true},
        {id: 3, text: 'Groceries',
        day: 'Feb 5th at 2:30pm', reminder: false},
    ]
  )



  // add task
  const addTask = async (task) => {
    // create a random id
    const res = await fetch('http://localhost:5000/tasks',
    {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(task)
    })

    const data = await res.json()

    setTasks([...tasks, data])

    //const id = Math.floor(Math.random() * 10000) + 1
    // create a brand new task with the given id
    //const newTask = { id, ...task }
    // add new task to list of tasks
    //setTasks([...tasks, newTask])
    // console.log(task)

  }

  //fetch tasks
  useEffect(() => {
      const getTasks = async () => {
        const tasksFromServer = await fetchTasks()
        setTasks(tasksFromServer)
      }
    getTasks()
  }, [])

  const fetchTasks = async () => {
    const res = await fetch("http://localhost:5000/tasks")
    const data = await res.json()
    console.log(data)
    return data
  }

  // fetch task
  const fetchTask = async (id) => {
    const res = await fetch(`http://localhost:5000/tasks/${id}`)
    const data = await res.json()
    console.log(data)
    return data
  }

  // delete task
  const deleteTask = async (id) => {
    await fetch(`http://localhost:5000/tasks/${id}`,
    {method: 'DELETE'})
    setTasks(tasks.filter((task) => task.id !== id))
  }

  // toggle reminder
  const toggleReminder = async (id) => {
    const taskToToggle = await fetchTask(id)
    const updTask = {...taskToToggle,
      reminder: !taskToToggle.reminder
    }

    const res = await fetch(`http://localhost:5000/tasks/${id}`,
    {
      method: 'PUT',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify(updTask)
    })

    const data = await res.json()

    setTasks(tasks.map((task) =>
      task.id === id ? 
      {...task, reminder: data.reminder } : task))
  }

  return (
    <Router>
    <div className="container">
      <Header onAdd={() => setShowAddTask(!showAddTask)} showAdd={showAddTask}/>

      <Routes>

      <Route path="/" exact element={
        <>
        {showAddTask && <AddTask onAdd={addTask} />}
        {tasks.length > 0 ? (
        <Tasks 
        tasks={tasks} 
        onDelete={deleteTask} 
        onToggle={toggleReminder}/> )
        : ('No Tasks To Show')}
        </>
      } />

     <Route path="/about" element={<About />} />
     </Routes>

     <Footer />
    </div>
    </Router>
    );
}

export default App;
