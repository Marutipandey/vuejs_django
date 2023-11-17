<!-- AboutPage.vue -->
<template>
    <div>
      <!-- Your template content goes here -->
      <div class="col-6 mx-auto">
        <form @submit.prevent="Submit">
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Email address</label>
            <input type="text" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            {{ username }}
          </div>
          <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
          </div>
  
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginForm', // or 'LoginView'
    // other options
  
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      Submit() {
        if (!this.username.length) {
          alert('Fill Username');
          return;
        }
  
        if (!this.password.length) {
          alert('Fill Password');
          return;
        }
  
        const requestOptions = {
          method: 'POST',
          headers: {
            'Content-type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        };
  
        fetch('http://127.0.0.1:8000/api/token/', requestOptions)
          .then(response => response.json())
          .then(data => {
            console.log(data.access);
            localStorage.setItem('token',data.access);
            window.location.href = '/'

            // Handle the response data as needed
          })
          .catch(error => {
            console.error('Error:', error);
            // Handle errors if any
          });
      }
    }
  };
  </script>
  
  <style scoped>
  /* Your component styles go here */
  </style>
  