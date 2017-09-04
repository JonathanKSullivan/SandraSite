'use strict';

/**
 * @ngdoc function
 * @name qualitaxas.controller:CorrespondenceCtrl
 * @description
 * # documentTypeCtrl
 * Controller of the qualitaxas contact page.
 */
angular.module('qualitaxas')
  .controller('documentTypeCtrl', ['$scope', '$http',
    function($scope, $http) {
      $scope.loadData = function() {
        $http({
          method: "GET",
          url: "/document_type_list"
        }).then(function(response) {
          $scope.documentTypes = response.data;
        });
      };

      $scope.submit = function() {
        $http({
          method: "POST",
          url: "/document_type_list",
          data:{
            typeName: $scope.documentType.typeName
          }
        }).then(function(response) {
          $scope.loadData();
        });
      };

      $scope.loadData();
    }
  ]);
