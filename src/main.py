"""
Main entry point for the Open Source Maintenance Toolkit CLI.
"""

from pr_analyzer import analyze_pull_request
from doc_generator import generate_docs


def main():
    print("Open Source Maintenance Toolkit")

    # Example workflow
    repo_path = "./example_repo"

    print("Analyzing pull requests...")
    analyze_pull_request(repo_path)

    print("Generating documentation...")
    generate_docs(repo_path)


if __name__ == "__main__":
    main()