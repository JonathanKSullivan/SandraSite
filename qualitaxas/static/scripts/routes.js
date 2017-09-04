qualitaxas.config(function($stateProvider, $urlRouterProvider, $interpolateProvider) {
    
    $urlRouterProvider.otherwise('/');
    $interpolateProvider.startSymbol('[{');
    $interpolateProvider.endSymbol('}]');
    
    $stateProvider
        
        .state('home', {
            url: '/',
            templateUrl: Flask.url_for("static", {"filename": "views/home.html"}),
        })
        
        .state('meet', {
            url: '/meet',
            templateUrl: Flask.url_for("static", {"filename": "views/meet.html"}),
        })

        .state('service', {
            url: '/services',
            templateUrl: Flask.url_for("static", {"filename": "views/services.html"}),
        })

        .state('testimonial', {
            url: '/testimonials',
            templateUrl: Flask.url_for("static", {"filename": "views/testimonials.html"}),
            controller: 'testimonialCtrl as testimonial'
        })

        .state('contact', {
            url: '/contact',
            templateUrl: Flask.url_for("static", {"filename": "views/contact.html"}),
            controller: 'contactCtrl as auth'
        })

        // .state('login', {
        //     url: '/login',
        //     templateUrl: Flask.url_for("static", {"filename": "views/login.html"}),
        //     controller: 'authCtrl as auth'
        // })

        .state('admin', {
            url: '/admin',
            templateUrl: Flask.url_for("static", {"filename": "views/admin.html"}),
        })

        .state('admin_companies', {
            url: '/admin/companies',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/company.html"}),
            controller: 'CompaniesCtrl as company'
        })

        .state('admin_company', {
            url: '/admin/company/:companyId',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/company/company.html"}),
            controller: 'CompanyCtrl as company'
        })

        .state('admin_correspondences', {
            url: '/admin/correspondences',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/correspondence.html"}),
            controller: 'correspondencesCtrl as correspondence'
        })

        .state('admin_correspondence', {
            url: '/admin/correspondence/:emailID',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/correspondence/correspondence.html"}),
            controller: 'correspondenceCtrl as correspondence'
        })

        .state('admin_documentType', {
            url: '/admin/document/documentType',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/documentType.html"}),
            controller: 'documentTypeCtrl as documentType'
        })

        .state('admin_document', {
            url: '/admin/document',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/document.html"}),
            controller: 'documentsCtrl as document'
        })

        .state('admin_invoice', {
            url: '/admin/invoice',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/invoice.html"}),
            controller: 'invoiceCtrl as invoice'
        })

        .state('admin_users', {
            url: '/admin/users',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/user.html"}),
            controller: 'usersCtrl as user'
        })

        .state('admin_testimonials', {
            url: '/admin/testimonials',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/testimonial.html"}),
            controller: 'testimonialsCtrl as testimonial'
        })

        .state('admin_log', {
            url: '/admin/software',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/software.html"}),
            controller: 'softwaresCtrl as software'
        })

        .state('admin_payments', {
            url: '/admin/payments',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/payment.html"}),
            controller: 'paymentsCtrl as payment'
        })
        
        .state('admin_software', {
            url: '/admin/software',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/software.html"}),
            controller: 'softwaresCtrl as software'
        })

        .state('admin_softwareKeys', {
            url: '/admin/softwareKeys',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/softwareKeys.html"}),
            controller: 'softwareKeysCtrl as softwareKey'
        })

        .state('company_admin', {
            url: '/admin',
            templateUrl: Flask.url_for("static", {"filename": "views/admin.html"}),
        })

        .state('company_companies', {
            url: '/admin/companies',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/company.html"}),
            controller: 'CompaniesCtrl as company'
        })

        .state('company_company', {
            url: '/admin/company/:companyId',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/company/company.html"}),
            controller: 'CompanyCtrl as company'
        })

        .state('company_correspondences', {
            url: '/admin/correspondences',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/correspondence.html"}),
            controller: 'correspondencesCtrl as correspondence'
        })

        .state('company_correspondence', {
            url: '/admin/correspondence/:emailID',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/correspondence/correspondence.html"}),
            controller: 'correspondenceCtrl as correspondence'
        })

        .state('company_document', {
            url: '/admin/document',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/document.html"}),
            controller: 'documentsCtrl as document'
        })

        .state('company_invoice', {
            url: '/admin/invoice',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/invoice.html"}),
            controller: 'invoiceCtrl as invoice'
        })

        .state('company_users', {
            url: '/admin/users',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/user.html"}),
            controller: 'usersCtrl as user'
        })

        .state('company_testimonials', {
            url: '/admin/testimonials',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/testimonial.html"}),
            controller: 'testimonialsCtrl as testimonial'
        })

        .state('company_log', {
            url: '/admin/software',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/software.html"}),
            controller: 'softwaresCtrl as software'
        })

        .state('company_payments', {
            url: '/admin/payments',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/payment.html"}),
            controller: 'paymentsCtrl as payment'
        })
        
        .state('company_software', {
            url: '/admin/software',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/software.html"}),
            controller: 'softwaresCtrl as software'
        })

        .state('company_softwareKeys', {
            url: '/admin/softwareKeys',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/softwareKeys.html"}),
            controller: 'softwareKeysCtrl as softwareKey'
        })

        .state('user_users', {
            url: '/admin/users',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/user.html"}),
            controller: 'usersCtrl as user'
        })

        .state('user_company', {
            url: '/admin/company/:companyId',
            templateUrl: Flask.url_for("static", {"filename": "views/admin/company/company.html"}),
            controller: 'CompanyCtrl as company'
        })
});