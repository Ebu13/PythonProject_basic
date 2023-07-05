# Import the requests module
import requests

# Ask the user for the GitHub profile name
profileName = input("Enter the GitHub profile name of the person you want: ")

# GitHub API URL
api_url = "https://api.github.com/users/" + profileName + "/repos"

# Get the JSON data from the API
response = requests.get(api_url)
data = response.json()

# Process the data in a loop
for repo in data:
    # Get the repository name and description
    name = repo["name"]
    description = repo["description"]

    # Assign an empty string if the description is None
    if description is None:
        description = ""

    # Print the name and description to the console
    print(name + ": " + description)
