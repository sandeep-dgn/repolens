import sys
import os

# This line is the 'Magic': It tells Python to look inside 'src' 
# so it can find the 'repolens' package.
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from repolens.engine import analyze_repo

if __name__ == "__main__":
    print("--- 🛠️  RepoLens Diagnostic Boot ---")
    analyze_repo()