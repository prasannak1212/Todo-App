import {useState} from 'react'
import '../Todo.css'
import '../App.css'

function Todo(){

    let [input, setInput] = useState("")
    let [todos, setTodo] = useState([])

    function addTodo(){
        setTodo([...todos, input])
    }

    function deleteTodo(t){
        setTodo(todos.filter((_, i) => i !== t))
    }

    return(
        <div className="todo-component">
            <h1>TODO APP</h1>
            <div className="input-field">
                <input placeholder='Enter your todo...' className="todo-input" id="todo-input" name="todo-input" type="text" onChange={(e)=>{setInput(e.target.value)}}/>
                <button onClick={addTodo}>Submit</button>
            </div>

            <h3>📌 Find your Todo List Here...</h3>
            <div className="todo-list">
                {todos.map((todo, index) => (
                    <div className='todo-list-item'>
                        <div key={index} className="todo-item">{todo}</div>
                        <button className="delete-todo" onClick={()=>deleteTodo(index)}>X</button>
                    </ div>
                    ))
                }
            </div>
        </ div>
    )
}

export default Todo