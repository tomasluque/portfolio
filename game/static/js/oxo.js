new Vue({
    el: '#app',
    data: {
        'hideStart': false,
        'hideSelect': true,
        'hideScore': true
    },
    methods: {
        'toSelect': function() {
            this.hideStart = true;
            this.hideSelect = false;
        }
    }
});