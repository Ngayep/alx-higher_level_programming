#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Object to store the count of completed tasks for each user ID
const userTasks = {};

// Fetch data from the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const todos = JSON.parse(body);

    // Iterate through each todo item
    todos.forEach(todo => {
      if (todo.completed) {
        if (!userTasks[todo.userId]) {
          userTasks[todo.userId] = 0;
        }
        userTasks[todo.userId]++;
      }
    });

    // Print the number of completed tasks for each user ID
    for (const [userId, count] of Object.entries(userTasks)) {
      console.log(`User ${userId} completed ${count} tasks`);
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
