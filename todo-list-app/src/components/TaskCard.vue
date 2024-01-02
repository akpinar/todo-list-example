<template>
    <div class="card-text">
                <div class="card mb-4">
                  <div class="card-body">
                    <h5 class="card-title">{{ task.title }}</h5>
                    <p class="card-text">{{ task.description }}</p>
                  </div>
                  <div class="p-3 border-top d-flex justify-content-between">
                    <button class="btn btn-primary" @click="deleteTask">Delete</button>
                    <!-- If task status is done move button should be not visible -->
                    <button class="btn btn-secondary" @click="moveTask">Move to testing</button>
                  </div>
                </div>
              </div>
  </template>
  
  <script>
  
  export default {
    props:{
        task: Object
    },
    methods:{
        moveTask(){
            // TODO: add move task operations
        },

        deleteTask(){
            // TODO: delete task operations
        }
    }
  };
  </script>
  
  <style></style>
  