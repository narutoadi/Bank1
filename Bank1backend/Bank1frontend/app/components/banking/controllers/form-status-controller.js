angular.module("Banking").controller("formStatusController", ["$scope", "$location", "formStatusService",
		function ($scope, $location, formStatusService) {
		console.log("I am inside formStatusController!!");
			$scope.FormSubmitted=false;
			$scope.FormNo;
			$scope.getStatus = function(){
			console.log("I am inside formStatusController getStatus funtion!!");
			formStatusService.getStatus($scope.statusPanNo, function(response) {
				
				console.log("hu hu ha ha", response.status);
				if (response.status == "201" || response.status == "200") {
					$scope.FormNo=response.data.formNumber;
					if(response.data.formStatus=="RP"){
						$scope.FormStatus="Request Pending!";
					}
					if(response.data.formStatus=="VF"){
						$scope.FormStatus="Verified but found false!";
					}
					if(response.data.formStatus=="VT"){
						$scope.FormStatus="Verified and found true!";
					}
					if(response.data.formStatus=="AC"){
						$scope.FormStatus="Account Created!";
					}
					$scope.FormSubmitted=true;
					console.log("success!");
					console.log(response);
				} else {
					console.log("Error!");
					console.log(response);
				}
			});
		};
	}]);