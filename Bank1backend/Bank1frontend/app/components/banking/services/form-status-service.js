var app = angular.module("Banking");
app.service("formStatusService", ["$http", function ($http) {

        console.log("I am inside formStatusService funtion!!");
    this.getStatus = function ( panNumber, callback) {
        
        $http({
            method: "GET",
            url: "api/banking/FormStatus/get/"+panNumber+"/",
            headers: {
                "Content-Type": "application/json"
            },
        }).then(function success(response) {
            callback(response);
        }, function error(response) {
            callback(response);
        });
    };
}]);