* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #e0f7fa;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.container {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 8px;
    width: 450px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #333;
}

.task-input {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}

#task, #task-time, #am-pm {
    padding: 10px;
    font-size: 16px;
    border-radius: 4px;
    margin-bottom: 10px;
}

#task-time, #am-pm {
    width: 49%;
}

.time-container {
    display: flex;
    justify-content: space-between;
}

#add-task-btn {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

#add-task-btn:hover {
    background-color: #45a049;
}

.error-message {
    color: red;
    font-size: 12px;
    margin-top: 5px;
}

ul {
    list-style-type: none;
}

li {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 4px;
    margin-bottom: 10px;
    font-size: 16px;
}

li button {
    background-color: #ff4c4c;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 5px 10px;
    cursor: pointer;
}

li button:hover {
    background-color: #e43b3b;
}

li .edit-btn {
    background-color: #ffa500;
}

li .edit-btn:hover {
    background-color: #e68900;
}

.time-left {
    font-size: 14px;
    color: #555;
}
