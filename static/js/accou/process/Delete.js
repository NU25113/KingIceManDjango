var myApp = angular.module('myApp', []);
myApp.controller("myController", function($scope) {
    $scope.newUser = {};
    $scope.clickedUser = {};
    $scope.alertMassege = "";
    $scope.users = [{
        name: "Zayn",
        fullname: "Zayn Alaoudi",
        email: "zayn@yahoo.com"
    }, {
        name: "lu",
        fullname: "Lu Kang",
        email: "lk@hotmail.com"
    }, {
        name: "Myra",
        fullname: "Myra akera",
        email: "Myraakera@hotmail.com"
    }, {
        name: "Mac",
        fullname: "Mac Lu",
        email: "mac@yahoo.com"
    }, {
        name: "Jack",
        fullname: "Jack Omar",
        email: "omarj@gmail.com"
    }, {
        name: "mohammed",
        fullname: "mohammed malik",
        email: "mmalik@hotmail.com"
    }, ];
    $scope.saveUser = function() {
        $scope.users.push($scope.newUser);
        $scope.newUser = {};
        $scope.alertMassege = "New data added successfully!";
    };
    $scope.selectUser = function(user) {
        $scope.clickedUser = user;
    };
    $scope.updateUser = function() {
        $scope.alertMassege = "Data Update was saved!";
    };
    $scope.deleteUser = function() {
        $scope.users.splice($scope.users.indexOf($scope.clickedUser), 1);
        $scope.alertMassege = "Deleted successfully!!";
    };
    $scope.clickedAlert = function() {
        $scope.alertMassege = "";
    };
});