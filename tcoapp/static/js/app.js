'use strict';


// Declare app level module which depends on filters, and services
var myApp = angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives', 'myApp.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/mpg', {templateUrl: '/static/partials/mpg.html', controller: 'MpgController'});
    $routeProvider.otherwise({redirectTo: '/mpg'});
  }]);
