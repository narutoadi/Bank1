var app = angular.module("Banking");
app.service("createAccountService", ["$http", function ($http) {

        console.log("I am inside createAccountService funtion!!");
    this.postRequest = function (fullName, fatherName, motherName, dob, gender, email, phoneNumber, panNumber, panCard, addressProof, idProof, accountType, startingAmount, callback) {
        console.log("I am inside createAccountService funtion!!");
        var data = {};
        data.fullName = fullName;
        data.fatherName = fatherName;
        data.motherName = motherName;
        data.dob = dob;
        data.gender = gender;
        data.email = email;
        data.phoneNumber = phoneNumber;
        data.panCard = panCard;
        data.addressProof = addressProof;
        data.idProof = idProof;
        data.accountType = accountType;
        data.startingAmount = startingAmount;
        data.panNumber = panNumber;
        console.log(data);
        $http({
            method: "POST",
            url: "/api/banking/AccountRequest/post/",
            headers: {
                "Content-Type": "application/json"
            },
            data: data,
        }).then(function success(response) {
            callback(response);
        }, function error(response) {
            callback(response);
        });
    };
}]);