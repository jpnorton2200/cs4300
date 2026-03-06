Feature: Movie theater booking API

  Scenario: User can view available movies
    Given there is a movie titled "A Quiet Place"
    When I request the movies API
    Then the response status should be 200
    And the movie list should include "A Quiet Place"


  Scenario: User can create a booking
    Given I am logged in as "jp" with password "pass12345"
    And there is a movie titled "Jurassic World"
    And there is a seat numbered 1
    When I create a booking for movie "Jurassic World" and seat 1
    Then the response status should be 201