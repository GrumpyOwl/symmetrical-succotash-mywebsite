/**
 * Created by marta on 25/09/16.
 */


app.controller("listController", function($scope){
    $scope.showMe = false;
    $scope.showList = function() {
        $scope.showMe = !$scope.showMe;
    }
});