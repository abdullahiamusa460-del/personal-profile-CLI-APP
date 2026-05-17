"""
Personal Profile CLI Application
Collects user information and displays a formatted profile summary.
"""

# Collect user information
print("\n--- Personal Profile Form ---\n")

user_name = input("Enter your name: ")
school_name = input("Enter your school name: ")
favorite_programming_language = input("Enter your favorite programming language: ")
favorite_color = input("Enter your favorite color: ")
state_of_origin = input("Enter your state of origin: ")

# Format and display profile summary
profile_summary = f"""
{'='*45}
                 PROFILE SUMMARY
{'='*45}
Name:                           {user_name}
School:                         {school_name}
Favorite Programming Language:  {favorite_programming_language}
Favorite Color:                 {favorite_color}
State of Origin:                {state_of_origin}
{'='*45}
"""

print(profile_summary)