/* Libs */
require("angular/angular");
require("angular-route/angular-route");
require("angular-resource/angular-resource");
/* Globals */
_ = require("lodash");  
_urlPrefixes = {  
  API:"api/banking/",
  TEMPLATES:"static/app/"
};
/* Components */
require("./components/home/home");
require("./components/banking/banking");

/* App Dependencies */
angular.module("myApp", [  
  "Home", // this is our component
  "Banking",
  "ngResource",
  "ngRoute",
]);

/* Config Vars */
var routesConfig = require("./routes");
// @TODO in Step 13.

/* App Config */
angular.module("myApp").config(routesConfig);  