'use strict';

/**
 * @ngdoc function
 * @name qualitaxas.controller:CorrespondenceCtrl
 * @description
 * # AuthCtrl
 * Controller of the qualitaxas contact page.
 */
angular.module('qualitaxas')
  .controller('correspondencesCtrl', ['$scope', '$http',
    function($scope, $http) {
      $scope.loadData = function() {
        $http({
          method: "GET",
          url: "/correspondence_list"
        }).then(function(response) {
          $scope.correspondences = response.data;
          console.log($scope.correspondences);
        });
      };
      $scope.loadData();
    }
  ]);

angular.module('qualitaxas')
  .controller('correspondenceCtrl', ['$scope', '$http', '$stateParams',
    function($scope, $http, $stateParams) {
      $scope.loadData = function() {
        $http({
          method: "GET",
          url: "/correspondence/" + $stateParams.emailID
        }).then(function(response) {
          $scope.correspondences = response.data;
        });
      };

      $scope.submit = function() {
        $http({
            method: "POST",
            url: "/correspondence_list",
            data: {
                    "name": $scope.name,
                    "email": $stateParams.emailID,
                    "phone": $scope.phone,
                    "subject": $scope.subject,
                    "message": $scope.message,
                    "inboxSent": "sent"
                  }
          })
          .then(
            function(response) {
              $scope.loadData();         
            });
      };

      $scope.loadData();
      $scope.subject = "RE:";
    }
  ]);