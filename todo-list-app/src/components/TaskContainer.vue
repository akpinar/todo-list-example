<template>
        <div class="col-md-4">
          <div class="card mb-4">
            <div class="card-body">
              <h5 class="card-title">{{ title }}</h5>
              <div  v-for="task in tasks" :key="task.id" >
               <TaskCard :task="task"/>
              </div>
             
            </div>
          </div>
        </div>
  </template>
  
  <script>
  import TaskCard from './TaskCard.vue';
  
  export default {
    components:{
      TaskCard
  },
  props:{
    title:String,
    tasks: Array,
  },
  };
  </script>
  
  <style></style>
  