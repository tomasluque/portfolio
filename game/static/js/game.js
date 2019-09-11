new Vue({
    el: '#app',
    delimiters: ['${', '}$'],
    data: {
        isActive: 'firstMenu',
        wSolo: 0,
        lSolo: 0,
        dSolo: 0,
        wMulti: 0,
        lMulti: 0,
        dMulti: 0,
    },
    methods: {
        myFunction: function(string) {
            this.message = string;
            console.log(this.message);
        },
        changeMenu: function(name) {
            this.isActive = name;
        },
    }
});