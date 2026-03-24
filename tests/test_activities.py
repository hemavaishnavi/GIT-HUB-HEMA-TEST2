"""
Tests for the Mergington High School Activities API.
Uses the AAA (Arrange-Act-Assert) pattern for test structure.
"""

import pytest


class TestGetActivities:
    """Tests for GET /activities endpoint"""

    def test_get_activities_returns_all_activities(self, client, reset_activities):
        """
        GIVEN: No preconditions
        WHEN: Client makes GET request to /activities
        THEN: Response status is 200 and returns all activities as dictionary
        """
        # Arrange
        # No setup needed - using default activities from app

        # Act
        response = client.get("/activities")

        # Assert
        assert response.status_code == 200
        activities_data = response.json()
        assert isinstance(activities_data, dict)
        assert len(activities_data) > 0

    def test_get_activities_returns_required_fields(self, client, reset_activities):
        """
        GIVEN: Activities exist in the system
        WHEN: Client makes GET request to /activities
        THEN: Each activity contains required fields (description, schedule, max_participants, participants)
        """
        # Arrange
        required_fields = {"description", "schedule", "max_participants", "participants"}

        # Act
        response = client.get("/activities")

        # Assert
        activities_data = response.json()
        for activity_name, activity_details in activities_data.items():
            assert isinstance(activity_details, dict)
            assert required_fields.issubset(activity_details.keys())
            assert isinstance(activity_details["participants"], list)
            assert isinstance(activity_details["max_participants"], int)

    def test_get_activities_contains_chess_club(self, client, reset_activities):
        """
        GIVEN: Chess Club activity exists
        WHEN: Client makes GET request to /activities
        THEN: Chess Club is included in the response
        """
        # Arrange
        # Default data includes Chess Club

        # Act
        response = client.get("/activities")

        # Assert
        activities_data = response.json()
        assert "Chess Club" in activities_data
        assert activities_data["Chess Club"]["description"] == "Learn strategies and compete in chess tournaments"


class TestRootEndpoint:
    """Tests for GET / endpoint"""

    def test_root_redirects_to_static_index(self, client, reset_activities):
        """
        GIVEN: Client is at root path
        WHEN: Client makes GET request to /
        THEN: Response is a redirect (307) to /static/index.html
        """
        # Arrange
        # No setup needed

        # Act
        response = client.get("/", follow_redirects=False)

        # Assert
        assert response.status_code == 307
        assert "/static/index.html" in response.headers["location"]


class TestSignupForActivity:
    """Tests for POST /activities/{activity_name}/signup endpoint"""

    def test_signup_new_student_success(self, client, reset_activities):
        """
        GIVEN: A student email that is not signed up for an activity
        WHEN: Client makes POST request to signup endpoint with valid activity and email
        THEN: Response status is 200 and student email is added to participants
        """
        # Arrange
        activity_name = "Chess Club"
        email = "newstudent@mergington.edu"

        # Act
        response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )

        # Assert
        assert response.status_code == 200
        assert "Signed up" in response.json()["message"]

    def test_signup_duplicate_email_returns_400(self, client, reset_activities):
        """
        GIVEN: A student email already signed up for an activity
        WHEN: Client makes POST request to signup endpoint with same email and activity
        THEN: Response status is 400 with "already signed up" error message
        """
        # Arrange
        activity_name = "Chess Club"
        # Using an email that's already in Chess Club participants
        email = "michael@mergington.edu"

        # Act
        response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )

        # Assert
        assert response.status_code == 400
        response_body = response.json()
        assert "detail" in response_body
        assert "already signed up" in response_body["detail"].lower()

    def test_signup_nonexistent_activity_returns_404(self, client, reset_activities):
        """
        GIVEN: An activity that does not exist
        WHEN: Client makes POST request to signup endpoint with invalid activity name
        THEN: Response status is 404 with "Activity not found" error message
        """
        # Arrange
        activity_name = "Nonexistent Activity"
        email = "student@mergington.edu"

        # Act
        response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )

        # Assert
        assert response.status_code == 404
        response_body = response.json()
        assert "detail" in response_body
        assert "not found" in response_body["detail"].lower()

    def test_signup_new_student_persists_in_activity(self, client, reset_activities):
        """
        GIVEN: A new student signs up for an activity
        WHEN: Client makes GET request to /activities after signup
        THEN: The new student email appears in the activity's participants list
        """
        # Arrange
        activity_name = "Programming Class"
        email = "alice@mergington.edu"

        # Act
        signup_response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )
        get_response = client.get("/activities")

        # Assert
        assert signup_response.status_code == 200
        activities_data = get_response.json()
        assert email in activities_data[activity_name]["participants"]

    def test_signup_multiple_different_students_same_activity(self, client, reset_activities):
        """
        GIVEN: Multiple different students sign up for the same activity
        WHEN: Client makes sequential signup requests
        THEN: All students are added to the activity's participants
        """
        # Arrange
        activity_name = "Gym Class"
        emails = ["alice@mergington.edu", "bob@mergington.edu", "charlie@mergington.edu"]

        # Act
        for email in emails:
            response = client.post(
                f"/activities/{activity_name}/signup?email={email}"
            )
            assert response.status_code == 200

        get_response = client.get("/activities")

        # Assert
        activities_data = get_response.json()
        for email in emails:
            assert email in activities_data[activity_name]["participants"]

    def test_signup_same_student_different_activities(self, client, reset_activities):
        """
        GIVEN: A student wants to sign up for multiple different activities
        WHEN: Client makes multiple signup requests with same email, different activities
        THEN: Student successfully signs up for both activities
        """
        # Arrange
        email = "alice@mergington.edu"
        activities_to_join = ["Chess Club", "Programming Class"]

        # Act
        for activity_name in activities_to_join:
            response = client.post(
                f"/activities/{activity_name}/signup?email={email}"
            )
            assert response.status_code == 200

        get_response = client.get("/activities")

        # Assert
        activities_data = get_response.json()
        for activity_name in activities_to_join:
            assert email in activities_data[activity_name]["participants"]

    def test_signup_response_contains_success_message(self, client, reset_activities):
        """
        GIVEN: A valid signup request
        WHEN: Client makes POST request to signup endpoint
        THEN: Response JSON contains a success message with email and activity name
        """
        # Arrange
        activity_name = "Debate Club"
        email = "alice@mergington.edu"

        # Act
        response = client.post(
            f"/activities/{activity_name}/signup?email={email}"
        )

        # Assert
        assert response.status_code == 200
        response_body = response.json()
        assert "message" in response_body
        assert email in response_body["message"]
        assert activity_name in response_body["message"]
