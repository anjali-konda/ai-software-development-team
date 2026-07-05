def document(requirement):

    requirement = requirement.lower()

    if "student" in requirement:
        documents = [
            "Software Requirement Specification (SRS)",
            "System Design Document",
            "User Manual",
            "Test Plan",
            "Project Report"
        ]

    elif "hospital" in requirement:
        documents = [
            "Software Requirement Specification (SRS)",
            "Database Design Document",
            "User Manual",
            "Test Report",
            "Project Report"
        ]

    else:
        documents = [
            "Software Requirement Specification (SRS)",
            "Design Document",
            "User Manual",
            "Testing Report",
            "Project Report"
        ]

    return {
        "Status": "Documentation completed successfully",
        "Documents": documents
    }