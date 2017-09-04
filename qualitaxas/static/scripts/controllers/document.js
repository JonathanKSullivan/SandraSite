'use strict';

/**
 * @ngdoc function
 * @name qualitaxas.controller:CorrespondenceCtrl
 * @description
 * # documentTypeCtrl
 * Controller of the qualitaxas contact page.
 */
angular.module('qualitaxas')
  .controller('documentsCtrl', ['$scope', '$http',
    function($scope, $http) {
      $scope.loadData = function() {
        $http({
          method: "GET",
          url: "/document_type_list"
        }).then(function(response) {
          $scope.documentTypes = response.data;
        });

        $http({
          method: "GET",
          url: "/companyList"
        }).then(function(response) {
          $scope.companies = response.data;
        });

        $http({
          method: "GET",
          url: "/document_list"
        }).then(function(response) {
          $scope.documents = response.data;
        });
      };

      $scope.submit = function() {
        $http({
          method: "POST",
          url: "/document_type_list",
          data:{
            name: $scope.newDocument.name,
            description: $scope.newDocument.description,
            companyId: $scope.newDocument.companyId,
            documentTypeId: $scope.newDocument.documentTypeId,
            file: $scope.newDocument.file
          }
        }).then(function(response) {
          $scope.loadData();
        });
      };

      $scope.loadData();
    }
  ]);
