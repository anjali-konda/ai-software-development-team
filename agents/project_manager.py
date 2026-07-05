def plan(requirement):

    requirement = requirement.lower()

    if "student" in requirement:
        return {
            "Timeline": "12 Weeks",
            "Modules": [
                "Student Registration",
                "Course Management",
                "Attendance Management",
                "Marks Management",
                "Report Generation"
            ]
        }

    elif "hospital" in requirement:
        return {
            "Timeline": "16 Weeks",
            "Modules": [
                "Patient Registration",
                "Doctor Management",
                "Appointment Booking",
                "Billing System",
                "Medical Records"
            ]
        }

    else:
        return {
            "Timeline": "10 Weeks",
            "Modules": [
                "Authentication",
                "Dashboard",
                "Database",
                "Reports",
                "Settings"
            ]
        }