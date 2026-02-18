###########################################################################################
## Author: nhatNguyen (blitzkrieg-j)                                                     ##
## Python-version: 3.11                                                                  ##
## Source: https://www.github.com/blitzkrieg-jvonngu-foo/blitzkrieg-jvonngu-foo          ##
## Profile-link: https://www.github.con/blitzkrieg-jvonngu-foo                           ##
###########################################################################################

import random as rd
import re
from pathlib import Path

# Constants
BASE_DIR = Path(__file__).resolve().parent
GREAT_LIST_PATH = BASE_DIR / 'src' / 'great_list.txt'
SOURCE_PATH = BASE_DIR / 'src' / 'sources.txt'
README_PATH = BASE_DIR / 'README.md'

QUOTE_START_MARKER = "<!-- QUOTE_START -->"
QUOTE_END_MARKER = "<!-- QUOTE_END -->"

def load_quotes(source_path):
    """Loads quotes from the source file."""
    quotes = []
    if not source_path.exists():
        print(f"Warning: {source_path} not found.")
        return quotes

    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading source file: {e}")
        return quotes

    for line in lines:
        if ':' in line:
            parts = line.split(':', 1)
            author = parts[0].strip()
            quote = parts[1].strip()
            # Remove existing quotes if present in the text to avoid double quotes
            quote = quote.strip('"').strip("'")
            quotes.append((author, quote))
    return quotes

def get_next_quote_index(great_list_path, total_quotes):
    """Determines the next quote index to show."""
    great_list = []
    
    # Create file if it doesn't exist
    if not great_list_path.exists():
        try:
            great_list_path.parent.mkdir(parents=True, exist_ok=True)
            great_list_path.touch()
        except Exception as e:
             print(f"Error creating great_list file: {e}")

    try:
        with open(great_list_path, 'r+', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                great_list = [int(i) for i in content.split()]
            
            # Reset if empty or invalid
            if not great_list:
                great_list = list(range(total_quotes))
            
            # Select a random quote index
            if great_list:
                selected_index = rd.choice(great_list)
                great_list.remove(selected_index)
            else:
                 # Fallback if list logic fails efficiently (should only happen if total_quotes is 0)
                 if total_quotes > 0:
                    great_list = list(range(total_quotes))
                    selected_index = rd.choice(great_list)
                    great_list.remove(selected_index)
                 else:
                    return -1

            # Update file
            f.seek(0)
            f.truncate()
            f.write(' '.join(str(i) for i in great_list))
            
            return selected_index

    except Exception as e:
        print(f"Error managing great_list: {e}")
        return rd.randint(0, total_quotes - 1) if total_quotes > 0 else -1

def format_quote_for_markdown(author, quote):
    """Formats the quote and author for the README using a centered table."""
    
    # Define emojis for decoration
    quote_emoji = "🌟" 
    author_emoji = "🧠"

    # Create a centered table structure
    # Use <blockquote> for a distinct background if supported, or just a table for framing.
    # A table with a single cell often looks like a frame on GitHub.
    
    formatted_content = f"""
<div align="center">

| | |
| :---: | :---: |
| **{quote_emoji} Daily Wisdom {quote_emoji}** | |
| <br/>**_“{quote}”_**<br/><br/>| |
| | _{author_emoji} {author} {author_emoji}_ |

</div>
"""
    # Clean up multiple newlines to look neat
    return f"{QUOTE_START_MARKER}{formatted_content}{QUOTE_END_MARKER}"

def update_readme(readme_path, new_content):
    """Updates the README file with the new quote, preserving other content."""
    if not readme_path.exists():
        print(f"Error: {readme_path} not found.")
        return

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the block between markers
        pattern = re.compile(f"{re.escape(QUOTE_START_MARKER)}.*?{re.escape(QUOTE_END_MARKER)}", re.DOTALL)
        
        if pattern.search(content):
            updated_content = pattern.sub(new_content, content)
        else:
            # If markers not found, prepend to file
            print("Markers not found. Prepending quote to README.")
            updated_content = f"{new_content}\n\n{content}"

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print("README.md updated successfully.")

    except Exception as e:
        print(f"Error updating README: {e}")

def main():
    quotes = load_quotes(SOURCE_PATH)
    if not quotes:
        print("No quotes available.")
        return

    index = get_next_quote_index(GREAT_LIST_PATH, len(quotes))
    if index == -1:
        print("Could not select a quote index.")
        return

    author, quote = quotes[index]
    formatted_content = format_quote_for_markdown(author, quote)
    update_readme(README_PATH, formatted_content)

if __name__ == "__main__":
    main()
