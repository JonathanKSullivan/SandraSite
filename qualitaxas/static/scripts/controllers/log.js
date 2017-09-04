'use strict';

/**
 * @ngdoc function
 * @name qualitaxas.controller:CorrespondenceCtrl
 * @description
 * # AuthCtrl
 * Controller of the qualitaxas contact page.
 */
angular.module('qualitaxas')
  .controller('testimonialsCtrl', ['$scope', '$http',
    function($scope, $http) {
      $scope.loadData = function() {
        $http({
          method: "GET",
          url: "/testimonial_list"
        }).then(function(response) {
          $scope.testimonials = response.data;
          console.log($scope.testimonials);
          console.log(1);
        });
      };
      $scope.loadData();
    }
  ]);

angular.module('qualitaxas')
  .controller('testimonialCtrl', ['$scope', '$http', '$stateParams',
    function($scope, $http, $stateParams) {
      $scope.loadData = function() {
        $http({
          method: "GET",
          url: "/correspondence/" + $stateParams.testimonialID
        }).then(function(response) {
          $scope.testimonials = response.data;
        });
      };

      $scope.loadData();
      $scope.subject = "RE:";
    }
  ]);