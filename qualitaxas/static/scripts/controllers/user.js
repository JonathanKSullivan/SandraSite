"use strict";

/**
 * @ngdoc function
 * @name qualitaxas.controller:usersCtrl
 * @description
 * # usersCtrl
 * Controller of the qualitaxas
 */
angular.module("qualitaxas")
 .controller("usersCtrl", ["$scope", "$http",
  function($scope, $http) {
   
   $scope.loadData = function() {
    $http({
      method: "GET",
      url: "/user_list"
     })
     .then(
      function(response) {
       var data = response.data;
       $scope.users = data
      });
   };

  }
 ]);
angular.module("qualitaxas")
 .controller("userCtrl", ["$scope", "$http", "$stateParams",
  function($scope, $http, $stateParams) {

   $scope.loadData = function() {
    $http({
      method: "GET",
      url: "/company/" + $stateParams.companyId,
     })
     .then(
      function(response) {
       var data = response.data;
       $scope.company = data
       $scope.company.address1 = $scope.company.address.split('|')[0];
       $scope.company.address2 = $scope.company.address.split('|')[1];
      },
      function(response) {
      });
   };
 }
 ]);