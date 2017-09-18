var app = angular.module('GBroker', ['ui.router', 'ngCookies']);

app.run(function($rootScope, $cookies, $state) {
  $rootScope.logOut = function() {
    $cookies.remove('username');
    $cookies.remove('customer_id');
    $cookies.remove('token');
    $rootScope.user_name = '';
    $rootScope.logState = false;
    $state.go('login');
  };
});

app.factory("GBroker_API", function factoryFunction($http, $cookies) {
  var service = {};

  service.displayHome = function() {
    return $http({
      url : '/home'
    })
  }

  service.displayGuns = function() {
    return $http({
      url : '/guns'
    })
  }
  return service;
});

app.controller('HomeController', function($scope, GBroker_API, $cookies, $rootScope){
    GBroker_API.displayHome();
});

app.controller('GunsController', function ($scope, GBroker_API, $cookies, $rootScope) {
  GBroker_API.displyGuns();
});

app.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider
    .state({
      name : 'home',
      url : '/home',
      templateUrl : 'home.html',
      controller: 'HomeController'
    }),
    .state({
      name : 'guns',
      url : '/guns',
      templateUrl : 'guns.html',
      controller: 'GunsController'
    });
});
