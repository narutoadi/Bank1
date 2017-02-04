function routesConfig($routeProvider) {  
  $routeProvider
    .when("/", {
      templateUrl: _urlPrefixes.TEMPLATES + "components/home/home.html",
      label: "Home",
      controller: "HomeController",
    })
    .when("/createAccount",{
      templateUrl: _urlPrefixes.TEMPLATES+ "components/banking/views/createAccount.html",
      label: "CreateAccount",
      controller: "createAccountController",
    })
    .when("/formStatus",{
      templateUrl: _urlPrefixes.TEMPLATES+ "components/banking/views/formStatus.html",
      controller: "formStatusController",
    })
    .when("/creditCard",{
      templateUrl: _urlPrefixes.TEMPLATES+ "components/banking/views/creditCard.html",
    })
    .when("/login",{
      templateUrl: _urlPrefixes.TEMPLATES+ "components/banking/views/login.html",
    })
    .otherwise({
      templateUrl: _urlPrefixes.TEMPLATES + "404.html"
    });
}

routesConfig.$inject = ["$routeProvider"];

module.exports = routesConfig; 