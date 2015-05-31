(function () {
  'use strict';

    var http = angular.module('annotationsAppHttp', ['ngResource']);

    http.factory('DocumentHttpService', function($resource) {
      return $resource(
        window.ANNOTATION_API_URL  + "document" + '/:docId/',
        {
          docId: '@docId'
        },
        {
          get: {
            method: 'GET',
            params: {docId: '@docId'}
          },
        }
      );
    });

    http.factory('AnnotationHttpService', function ($resource) {
      return $resource(
        window.ANNOTATION_API_URL  + "lists" + '/:listId/',
      	{
          listId: '@listId'
        },
  			{
        	get: {
      			method: 'GET',
      			params: {listId: '@listId'}
      		},
          post: {
            method: 'POST',
            params: {listId: '@listId', node: '@node'}
          },
          delete: {
            method: 'DELETE',
            params: {listId: '@listId', node: '@node'}
          }
        }
      );
      // return {
        // TODO check doublesx
        // get: function (docId) {
        //   // TODO remove timeout
        //   $timeout(function () {
        //     $rootScope.annotations = ;
        //   });
        // },
        // newAnnotationObject: function(text, category, level) {
        //   return {
        //     'text': text.trim(),
        //     'category': category,
        //     'level': level
        //   };
        // },
        // create: function(keyword, $rootScope) {
        //   if ($rootScope.annotations === undefined) $rootScope.annotations = [];
        //   // find duplicate by text
        //   var existing = _.find(
        //     $rootScope.annotations,
        //     function(annotation) { return annotation.text.trim().toLowerCase() === keyword.text.trim().toLowerCase(); }
        //   );
        //   // delete existing conflicting data before adding new
        //   if (existing) {
        //     if (existing.category == keyword.category && existing.level == keyword.level) return;
        //     this.delete(existing, $rootScope);
        //   }
        //   // TODO remove server mocking
        //   var mock = _.extend(keyword, {
        //     'uuid': jQuery.now().toString(),
        //     'occurrences': 322
        //   });
        //
        //   $timeout(function() {
        //     $rootScope.$apply(function() {
        //       $rootScope.annotations.push(mock);
        //     });
        //   });
        //
        //   return mock;
        // },
        // delete: function(keyword, $rootScope) {
        //   var filtered = _.filter($rootScope.annotations, function(item) {
        //     if (item.uuid == keyword.uuid) {
        //       return false;
        //     } else {
        //       return true;
        //     }
        //   });
        //   $timeout(function() {
        //     $rootScope.$apply(function() {
        //       $rootScope.annotations = filtered;
        //     });
        //   });
        // }
      // };
    });

})(window);
