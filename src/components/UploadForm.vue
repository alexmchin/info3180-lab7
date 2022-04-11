<template>

        <form  @submit.prevent="uploadPhoto" class="form">
            <div class="input-group mx-sm-3 mb-2">
                <label class="visually-hidden" for="search">Search</label>
                <input type="search" name="search" v-model="uploadPhoto"
        id="search" class="form-control mb-2 mr-sm-2" placeholder="Enter
        search term here" />
                <button class="btn btn-primary mb-2">Search</button>
            </div>
            <p>You are searching for {{ uploadPhoto }}</p>
        </form>

</template>

<script>
export default {
        data() {return {articles: [], searchTerm: ''} },

        methods: {
            uploadPhoto() {
                fetch("/api/upload", {method: 'POST'})
                .then(function (response) {return response.json();})
                .then(function (data) {
                // display a success message
                console.log(data);
                })
                .catch(function (error) {
                console.log(error);
                });
            }
        }
    };
</script>
