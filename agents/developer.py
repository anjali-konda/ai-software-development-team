def develop(requirement):

    requirement = requirement.lower()

    if "student" in requirement:
        return {
            "Frontend": ["HTML", "CSS", "JavaScript", "Bootstrap"],
            "Backend": ["Python", "Flask"],
            "Database": ["SQLite"]
        }

    elif "hospital" in requirement:
        return {
            "Frontend": ["HTML", "CSS", "Bootstrap"],
            "Backend": ["Python", "Flask"],
            "Database": ["MySQL"]
        }

    else:
        return {
            "Frontend": ["HTML", "CSS"],
            "Backend": ["Python"],
            "Database": ["SQLite"]
        }