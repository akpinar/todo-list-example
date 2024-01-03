<template>
  <div class="card-text">
    <div class="card mb-4">
      <div class="card-body">
        <h5 class="card-title">{{task["title"]}}</h5>
        <p class="card-text">{{task["description"]}}</p>
      </div>
      <div class="p-3 border-top d-flex justify-content-between">
        <button class="btn btn-primary" @click="deleteTask">Delete</button>
        <button
          v-if="task['status'] != '3'"
          class="btn btn-secondary"
          @click="moveTask()"
        >
          Move to {{cardName}}
        </button>
      </div>
      <div id="toast-container" class="position-fixed top-0 end-0 p-3">
    </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props:{
      task: Object,
      id: String,
      cardName: String,

  },
  methods:{
      moveTask(){
        this.showToast = true

        axios
    .put(`http://127.0.0.1:5000/task/${this.id}`,{
      title:this.task["title"],
      description: this.task["description"],
      status: this.cardName == "testing" ? "2" : "3"})
    .then((response) => {
      if(response.status == 200){
        
        this.$emit("fetch-task");

      }
    })
    .catch((error) => {
      return error;
    });
      },

      deleteTask(){
        axios
    .delete(`http://127.0.0.1:5000/task/${this.id}`)
    .then((response) => {
      if(response.status == 200){
        this.$emit("fetch-task");
      }
    })
    .catch((error) => {
      return error;
    });
      },
  }
};
</script>

<style></style>
