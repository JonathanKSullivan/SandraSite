'use strict';

/**
 * @ngdoc function
 * @name qualitaxas.controller:AuthCtrl
 * @description
 * # AuthCtrl
 * Controller of the qualitaxas Authenication page.
 */
angular.module('qualitaxas')
  .controller('authCtrl', ['$scope', '$http', 
              function ($scope, $http) {
    $scope.view = 0
    $scope.setView = function(viewNumber){
      $scope.view = viewNumber
    }
    this.signIn = function(){
      console.log("Sign In")
    }
    this.signUp = function(){
      console.log("Sign Up") 
    }
    this.forgotPassword = function(){
      console.log("Forgot Password")
    }
  }]);
