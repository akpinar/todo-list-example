<template>
    <div
      :style="{ display: visible ? 'flex' : 'none' }"
      class="modal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered w-100" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5>New Task Modal</h5>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <label for="taskTitle">Task Title</label>
              <input
                type="text"
                class="form-control"
                id="taskTitle"
                v-model="newTask.title"
              />
            </div>
            <div class="form-group">
              <label for="taskDescription">Task Description</label>
              <textarea
                class="form-control"
                id="taskDescription"
                rows="3"
                v-model="newTask.description"
              ></textarea>
            </div>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-dismiss="modal"
              @click="changeModalStatus"
            >
              Discard
            </button>
            <button type="button" class="btn btn-primary" @click="addTask">
              Save
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props:{
        visible: Boolean
    },
    data() {
        return {
            newTask: { title: "", description: ""   },
        };
    },
    methods: {
        addTask() {
            axios
      .post(`http://127.0.0.1:5000/task`,{title:this.newTask.title, description: this.newTask.description})
      .then((response) => {
        if(response.status == 200) {
            this.changeModalStatus()
            this.$emit('update:tasks');
        }
      })
      .catch((error) => {
        return error;
      });
        },
        changeModalStatus() {
            this.$emit('update:visible', !this.visible);
        },
  
    },
  }
  </script>
  
  <style></style>
  