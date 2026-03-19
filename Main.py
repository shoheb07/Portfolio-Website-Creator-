import os

def get_user_data():
    print("=== Portfolio Website Creator ===")

    name = input("Enter your name: ")
    bio = input("Enter your bio: ")
    skills = input("Enter skills (comma separated): ").split(",")
    projects = []

    num_projects = int(input("How many projects? "))

    for i in range(num_projects):
        print(f"\nProject {i+1}")
        title = input("Title: ")
        desc = input("Description: ")
        link = input("Link: ")

        projects.append({
            "title": title,
            "desc": desc,
            "link": link
        })

    email = input("Enter your email: ")

    return name, bio, skills, projects, email


def generate_projects_html(projects):
    project_html = ""
    for p in projects:
        project_html += f"""
        <div class="project">
            <h3>{p['title']}</h3>
            <p>{p['desc']}</p>
            <a href="{p['link']}" target="_blank">View Project</a>
        </div>
        """
    return project_html


def create_portfolio():
    name, bio, skills, projects, email = get_user_data()

    with open("templates/index_template.html", "r") as f:
        template = f.read()

    skills_html = "".join([f"<li>{skill.strip()}</li>" for skill in skills])
    projects_html = generate_projects_html(projects)

    final_html = template.replace("{{name}}", name)\
                         .replace("{{bio}}", bio)\
                         .replace("{{skills}}", skills_html)\
                         .replace("{{projects}}", projects_html)\
                         .replace("{{email}}", email)

    os.makedirs("output", exist_ok=True)

    with open("output/index.html", "w") as f:
        f.write(final_html)

    print("\n✅ Portfolio website created successfully!")
    print("📁 Check the 'output' folder")


if __name__ == "__main__":
    create_portfolio()
