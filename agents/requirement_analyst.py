def analyze(requirement):

    requirement = requirement.lower()

    if "student" in requirement:
        return {
            "Functional Requirements": [
                "Student Registration",
                "Course Management",
                "Attendance Management",
                "Marks Management",
                "Faculty Management"
            ],
            "Non Functional Requirements": [
                "Security",
                "Fast Performance",
                "Scalability",
                "Reliability",
                "Easy to Use"
            ]
        }

    elif "hospital" in requirement:
        return {
            "Functional Requirements": [
                "Patient Registration",
                "Doctor Management",
                "Appointment Booking",
                "Billing",
                "Medical Records"
            ],
            "Non Functional Requirements": [
                "High Security",
                "Fast Response",
                "Availability",
                "Scalability",
                "Reliability"
            ]
        }

    else:
        return {
            "Functional Requirements":[
                "User Login",
                "Dashboard",
                "Database",
                "Reports",
                "Admin Panel"
            ],
            "Non Functional Requirements":[
                "Security",
                "Performance",
                "Reliability",
                "Scalability",
                "Usability"
            ]
        }