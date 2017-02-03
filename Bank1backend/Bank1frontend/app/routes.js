function routesConfig($routeProvider) {  
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/home.html",
      label: "Home"
    })
    .when("/createAccount",{
      templateUrl: _urlPrefixes.TEMPLATES+ "components/banking/views/createAccount.html",
      label: "CreateAccount",
      controller: "createAccountController"
    })
    .when("/createAccountRequestSuccessful",{ 
      templateUrl: _urlPrefixes.TEMPLATES+ "components/banking/views/createAccountRequestSuccessful.html",
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig; 