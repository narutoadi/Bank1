angular.module("Banking", []).config(["$httpProvider", function($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = "csrftoken";
	$httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
}]);

require("./controllers/create-account-controller");
require("./services/create-account-service");