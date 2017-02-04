angular.module("Banking").controller("createAccountController", ["$scope", "$location", "createAccountService",
		function ($scope, $location, createAccountService) {

		$scope.FormSubmitted=false;
		console.log("I am inside createAccountController!!");
		$scope.postRequest = function(){
			console.log("I am inside createAccountController postRequest funtion!!");
			createAccountService.postRequest($scope.fullName, $scope.fatherName, $scope.motherName, $scope.dob, $scope.gender, $scope.email, $scope.phoneNumber, $scope.panNumber, $scope.panCard, $scope.addressProof, $scope.idProof, $scope.accountType, $scope.startingAmount, function(response) {
				console.log($scope.idProof);
				console.log("hu hu ha ha", response.status);
				if (response.status == "201") {
					$scope.FormSubmitted=true;
					console.log("success!");
					console.log(response);
					$location.path("/createAccountRequestSuccessful");
				} else {
					console.log("Error!");
					console.log(response);
				}
			});
		};
	}]);

angular.module("Banking").directive("fileread", [function () {
    return {
        scope: {
            fileread: "="
        },
        link: function (scope, element) {
            element.bind("change", function (changeEvent) {
                var reader = new FileReader();
                reader.onload = function (loadEvent) {
                    scope.$apply(function () {
                        scope.fileread = loadEvent.target.result;
                    });
                };
                reader.readAsDataURL(changeEvent.target.files[0]);
            });
        }
    };
}]);