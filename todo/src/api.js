import axios from 'axios'

const API_URL = 'http://13.60.254.238:8000/';

export const getTasks = async ()=>{
    const response = await axios.get(`${API_URL}/tasks`);
    // return Array.isArray(response.data) ? response.data : response.data.tasks || [];
    return response.data.data;
}

export const addTask = async (task)=>{
    const response = await axios.post(`${API_URL}/add_task`, {task});
    return response.data.data;
}

export const deleteTask = async (id)=>{
    const response = await axios.delete(`${API_URL}/tasks/${id}`)
    return response.message;
}
