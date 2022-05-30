import {Header} from './components/Header'
import {Tasks} from './components/Tasks'
import {AddTask} from './components/AddTask'
import {useState} from 'react'

function App() {
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

  // toggle reminder
  const toggleReminder = (id) => {
    setTasks(tasks.map(
      (task) =>
      task.id === id ? 
      {...task, reminder: !task.reminder } 
      : task))
  }

  // add task
  const addTask = (task) => {
    // const id = Math.floor(Math.random() * 10000) + 1
    // const newTask = { id, ...task }
    // setTasks([...tasks, newTask])
    console.log(task);
  }

  // delete task
  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id))
  }

  return (
    <div className="container">
      <Header />
      <AddTask onAdd={addTask} />
     {tasks.length > 0 ? 
     <Tasks tasks={tasks} onDelete={deleteTask} onToggle={toggleReminder}/> 
     : 'No Tasks To Show'}
    </div>
  );
}

export default App;
