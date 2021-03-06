(function () {
  'use strict';

  var annotationsAppActiveLists = angular.module('annotationsAppActiveLists', []);

  annotationsAppActiveLists.controller('ActiveListsController',
    ['$scope', '$rootScope', '$timeout',
    function ($scope, $rootScope, $timeout) {

      $scope.activeListsChange = function() {
        var selected = $('.selectpicker option:selected').val();
        var newActive = {};
        $('.selectpicker option:selected').each(function(item, opt) {
          // ex opt:
          // <option id="list---748" value="MAINLIST">MAINLIST</option>
          var id = opt.id.split("---", 2)[1];
          newActive[id] = opt.value;
        });

        // ex: {745: "MAINLIST", 748: "MAPLIST"}
        $rootScope.activeLists = newActive;
      };

      $rootScope.$watchCollection('activeLists', function (newValue, oldValue) {
        if (newValue === undefined) return;
        $timeout(function() {
          $('.selectpicker').selectpicker('refresh');
        });
      });


      // FIXME: est-ce qu'on ne pourrait pas directement utiliser lists
      // au lieu  de recopier dans allListsSelect ?
      $rootScope.$watchCollection('lists', function (newValue, oldValue) {
        if (newValue === undefined) return;
        // reformat lists to allListsSelect
        var allListsSelect = [];
        // console.log($rootScope.lists)
        angular.forEach($rootScope.lists, function(value, key) {
          this.push({
            'id': key,
            'label': value
          });
          // initialize activeLists with the MAPLIST by default
          if (value == 'MAPLIST') {
            $rootScope.activeLists = {};
            $rootScope.activeLists[key] = value;
          }
        }, allListsSelect);

        $rootScope.allListsSelect = allListsSelect;

        $timeout(function() {
          $('.selectpicker').selectpicker();
          $('.selectpicker').selectpicker('val', ['MAPLIST']);
        });
      });

    }]);


})(window);
