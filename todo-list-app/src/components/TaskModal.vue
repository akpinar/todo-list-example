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
            <!-- Input field -->
            <div class="form-group">
            <label for="taskTitle">Task Title</label>
            <input
                type="text"
                class="form-control"
                id="taskTitle"
                v-model="newTask.title"
            />
            </div>
            <!-- Textarea field -->
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
            <button type="button" class="btn btn-primary">Save</button>
        </div>
        </div>
    </div>
    </div>
        
  </template>
  
  <script>
  export default {
    props:{
        visible: Boolean
    },
    data() {
        return {
            newTask: { title: "", description: ""   },
            show: this.visible
        };
    },
    methods: {
        addTask() {
            // TODO: add task method api connection
        },
        changeModalStatus() {
            this.$emit('update:visible', !this.visible);    
        },
    },
  }
  </script>
  
  <style></style>
  