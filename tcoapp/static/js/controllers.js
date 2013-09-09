'use strict';

angular.module('myApp.controllers', []);

myApp.controller('MpgController', ['$scope','$http', function($scope, $http) {
  	$scope.foo = 'bar';
	// $scope.miles = 400;
	// $scope.litres = 50;

	$scope.averageMpg = 0;

	// $http.get('data/journeys.json').success(function(data) {
 //    	$scope.journeys = data;
	// });

	$http.get('/drf/journeys/').success(function(data) {
    	$scope.journeys = data;
	});

	// $scope.setFoo = function(e, str){
	// 	e.preventDefault();
	// 	$scope.foo = str;
	// }

	$scope.calcMpg = function(journey){

		//var litres = journey.litres;
		var gallons = journey.litres/4.54609;
		return journey.miles/gallons;
	}

	$scope.addJourney = function(){
		var journey = {
			"id": 0,
			"miles": null,
			"litres": null
		} 

		//$scope.calcAverageMpg();
		$scope.journeys.push(journey);

	}

	$scope.calcAverageMpg = function(){

		if($scope.journeys && $scope.journeys.length){
			var total = 0;
			var lengthCount = 0;
			for(var i = 0; i < $scope.journeys.length; i++){
				var mpg = $scope.calcMpg($scope.journeys[i]);
				if(mpg){
					total += $scope.calcMpg($scope.journeys[i]);
					lengthCount++;
				}
			}
			$scope.averageMpg = total/lengthCount;
		}

		return $scope.averageMpg;
	}


 }]);