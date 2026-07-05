def test(requirement):

    requirement = requirement.lower()

    if "student" in requirement:
        test_cases = [
            "Verify student registration",
            "Check login functionality",
            "Validate attendance records",
            "Verify marks entry",
            "Test report generation"
        ]

    elif "hospital" in requirement:
        test_cases = [
            "Verify patient registration",
            "Check appointment booking",
            "Validate billing system",
            "Verify doctor records",
            "Test medical reports"
        ]

    else:
        test_cases = [
            "Verify user login",
            "Check database connection",
            "Validate input fields",
            "Test dashboard",
            "Generate reports"
        ]

    return {
        "Status": "Testing plan prepared successfully",
        "Test Cases": test_cases
    }