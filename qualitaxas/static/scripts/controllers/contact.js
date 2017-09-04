'use strict';

/**
 * @ngdoc function
 * @name qualitaxas.controller:contactCtrl
 * @description
 * # AuthCtrl
 * Controller of the qualitaxas contact page.
 */
angular.module('qualitaxas')
  .controller('contactCtrl', ['$scope', '$http', 
              function ($scope, $http) {
    $scope.view = 0;

    $scope.submitCorrespondence = function() {
      $http({
          url: '/correspondence_list',
          method: "POST",
          data: { 
            "name" : $scope.name,
            "email" : $scope.email,
            "phone" : $scope.phone,
            "subject" : $scope.subject,
            "message" : $scope.message,
            "inboxSent" : "inbox"
          }
      }).then(function(resp) {
        $scope.view = 1;
      });
    };
  }]);
