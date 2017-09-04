'use strict';
/**
 * @ngdoc function
 * @name qualitaxas.controller:CompaniesCtrl
 * @description
 * # CompaniesCtrl
 * Controller of the qualitaxas
 */
angular.module("qualitaxas")
 .controller("CompaniesCtrl", ["$scope", "$http", 'Upload',
  function($scope, $http, Upload) {

   $scope.searchForCompanyByID = function(companyKey, companyArray) {
    for (var i = 0; i < companyArray.length; i++) {
     if (companyArray[i].id === companyKey) {
      return companyArray[i];
     }
    }
   };

   $scope.updateCompany = function(companyId) {
    $http({
     method: "POST",
     url: "/company/" + companyId,
     data: $scope.updateCompanyData[companyId]
    }).then(function(response) {
     $scope.loadData();
    });
    $scope.hideUpdateForm(companyId);
   };

   $scope.loadData = function() {
    $http({
      method: "GET",
      url: "/companyList"
     })
     .then(function(response) {
      $scope.companies = response.data;

      for (var company in $scope.companies) {
       $scope.showForm.company = false
       $scope.companies[company].address1 = $scope.companies[company].address.split('|')[0];
       $scope.companies[company].address2 = $scope.companies[company].address.split('|')[1];
      }
     });
   };

   $scope.is_int = function(value) {
    if ((parseFloat(value) == parseInt(value)) && !isNaN(value)) {
     return true;
    } else {
     return false;
    }
   };

   $scope.autoFillZipNew = function($event) {
    // Cache
    var zipcode = $scope.newCompany.zip_code;

    // Did they type five integers?
    if ((zipcode.length == 5) && ($scope.is_int(zipcode))) {

     // Call Ziptastic for information
     $http({
       method: "GET",
       url: "https://zip.getziptastic.com/v2/US/" + zipcode
      })
      .then(function(result, success) {
       $scope.showCity = true;
       $scope.newCompany.city = result.data.city;
       $scope.newCompany.state = result.data.state;
       $scope.error = "";
      }, function(result, success) {
       $scope.showCity = false;
       $scope.newCompany.city = "";
       $scope.newCompany.state = "";
       $scope.error = result.data.message;
      });
    }
   };

   $scope.autoFillZipUpdate = function($event, companyId) {
    // Cache
    var zipcode = $scope.newCompany.zip_code;

    // Did they type five integers?
    if ((zipcode.length == 5) && ($scope.is_int(zipcode))) {

     // Call Ziptastic for information
     $http({
       method: "GET",
       url: "https://zip.getziptastic.com/v2/US/" + zipcode
      })
      .then(function(result, success) {

       $scope.updateCompanyData[companyId].city = result.data.city;
       $scope.updateCompanyData[companyId].state = result.data.state;
      }, function(result, success) {
       $scope.updateCompanyData[companyId].city = "";
       $scope.updateCompanyData[companyId].state = "";
      });
    }
   };

   $scope.activateCompany = function(companyId) {
    $http({
      method: "POST",
      url: "/activate/company/" + companyId
     })
     .then(function(response) {
      $scope.loadData();
     });
   };

   $scope.showUpdateForm = function(companyId) {
    $scope.updateCompanyData[companyId] = $scope.searchForCompanyByID(companyId, $scope.companies);
    $scope.updateCompanyData[companyId].required = true;
    $scope.updateCompanyData[companyId].disabled = true;
    console.log($scope.updateCompanyData);
    $scope.showForm[companyId] = true;
    $scope.loadData();
   };

   $scope.hideUpdateForm = function(companyId) {
    $scope.updateCompanyData[companyId] = $scope.searchForCompanyByID(companyId, $scope.companies);
    $scope.showForm[companyId] = false;
    $scope.loadData();
   };

   $scope.isShowForm = function(companyId) {
    return $scope.showForm[companyId];
   };

   $scope.submit = function() {
    if ($scope.companyForm.file && $scope.newCompany.logo_file) {
     $http({
       method: "POST",
       url: "/companyList",
       data: $scope.newCompany
      })
      .then(
       function(response) {
        $http({
          method: "GET",
          url: "/companyList"
         })
         .then(function(response) {
          $scope.companies = response.data;
          $scope.newCompany = {};
         });
       });
    } else {
     $scope.newCompany.logo_file = null;
     $http({
      method: "POST",
      url: "/companyList",
      data: $scope.newCompany
     });
     $http({
       method: "GET",
       url: "/companyList"
      })
      .then(function(response) {
       $scope.companies = response.data;
       $scope.newCompany = {};
      });
    };
    $scope.showCity = false;
   };

   $scope.hideLogoUrl = function() {
    console.log($scope.isLogoUrlHidden);
    $scope.isLogoUrlHidden = !$scope.isLogoUrlHidden;
   };

   $scope.isLogoUrlHidden = true;
   $scope.loadData();
   $scope.showForm = {};
   $scope.name = "Company";
   $scope.newCompany = {};
   $scope.updateCompanyData = {};
   $scope.error = "";
   $scope.showCity = false;
  }

 ]);
angular.module("qualitaxas")
 .controller("CompanyCtrl", ["$scope", "$http", "$stateParams",
  function($scope, $http, $stateParams) {

   $scope.updateCompany = function() {
    $http({
     method: "POST",
     url: "/company/" + $stateParams.companyId,
     data: $scope.updateCompanyData
    }).then(function(response) {
     $scope.loadData();
    });
    $scope.hideUpdateForm($stateParams.companyId, );
   };

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
      function(response) {});
   };

   $scope.isShowForm = function() {
    return $scope.showForm;
   };

   $scope.showUpdateForm = function() {
    $scope.updateCompanyData = $scope.company;
    $scope.showForm = true;
    $scope.loadData();
   };

   $scope.hideUpdateForm = function() {
    $scope.updateCompanyData = $scope.company;
    $scope.showForm = false;
    $scope.loadData();
   };

   $scope.activateCompany = function() {
    $http({
      method: "POST",
      url: "/activate/company/" + $stateParams.companyId,
     })
     .then(function(response) {
      $scope.loadData();
     });
   };


   $scope.showForm = false;
   $scope.loadData();
  }
 ]);