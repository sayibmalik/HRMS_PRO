import os

def add_migrations_to_apps(project_path):
    # Iterate through all directories in the project path
    for root, dirs, files in os.walk(project_path):
        # Check for apps (directories with a models.py file)
        if "models.py" in files:
            app_path = root
            migrations_path = os.path.join(app_path, "migrations")
            
            # Create the migrations folder if it doesn't exist
            if not os.path.exists(migrations_path):
                os.makedirs(migrations_path)
                print(f"Created 'migrations' folder in {app_path}")
            
            # Add the __init__.py file if not present
            init_file = os.path.join(migrations_path, "__init__.py")
            if not os.path.exists(init_file):
                with open(init_file, "w") as f:
                    pass  # Create an empty file
                print(f"Added '__init__.py' to {migrations_path}")

if __name__ == "__main__":
    # Specify your Django project's base directory
    project_base_path = os.path.abspath(os.curdir)  # Current directory
    add_migrations_to_apps(project_base_path)
