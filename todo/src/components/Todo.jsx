import {useState, useEffect} from 'react'
import '../Todo.css'
import '../App.css'
import {getTasks, addTask, deleteTask} from '../api'

function Todo(){
    const [loading, setLoading] = useState(true);
    let [input, setInput] = useState("")
    let [todos, setTodo] = useState([])

    const fetchTasks = async () => {
            try {
                const data = await getTasks();
                setTodo(data);
            } catch (err){ 
                console.error("Error fetching tasks:", err);
            } finally {
                setLoading(false);
            }
        }

    useEffect(()=>{
        fetchTasks()
    }, [])

    const handleAdd = async (e)=>{
        e.preventDefault();
        if(!input.trim()) return;
        try {
            const created = await addTask(input.trim());
            setTodo((prev) => [...prev, created]);
            setInput('');
            fetchTasks();
        } catch (err) {
            console.error("Error adding task:", err);
        }
    }

    const handleDelete = async (id)=>{
        try {
            await deleteTask(id);
            setTodo((prev) => prev.filter((todo) => todo._id !== id))
            fetchTasks();
        } catch (err) {
            console.error("Error deleting task:", err);
        }
    }

    if (loading) return <h2>Loading tasks...</h2>;

    return(
        <div className="todo-component">
            <h1>TODO APP</h1>
            <div className="input-field">
                <input placeholder='Enter your todo...' className="todo-input" id="todo-input" name="todo-input" type="text" value={input} onChange={(e)=>{setInput(e.target.value)}}/>
                <button onClick={handleAdd}>Submit</button>
            </div>

            <h3>📌 Find your Todo List Here...</h3>
            <div className="todo-list">
                {
                    todos.map((todo) => {
                        return (
                            <div key={todo._id} className='todo-list-item'>
                                <div className="todo-item">{todo.task}</div>
                                <button className="delete-todo" onClick={() => handleDelete(todo._id)}>X</button>
                            </ div>
                        )
                    })
                }
            </div>
        </ div>
    )
}

export default Todo