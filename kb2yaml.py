import sys
import re
import yaml

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def parse_content(content):
    # Regex to match the specific pattern
    pattern = re.compile(r"\[([A-Z]{4})\]\s((?:\d+\.)?(?:\d+\.)?(?:\d+))\s(.*)\n")
    items={}
    matches = pattern.findall(content)
    for match in matches:
        items[match[1]]={"Status": match[0], "Description": match[2]}
    return items

def dict_to_markdown_table(items):
    markdown_table = "| Status | Item | Description |\n| --- | ------- | ---- |\n"
    
    # Add the data
    for item in items.keys():
        markdown_table += f"| {items[item]['Status']} | {item} | {items[item]['Description']} |\n"
    
    return markdown_table

def dict_to_yaml(data_list):
    # this seemed like it was going to be more complicated
    return yaml.dump(data_list, default_flow_style=False)

def main(filename):
    content = read_file(filename)
    items = parse_content(content)
    markdown_table = dict_to_markdown_table(items)
    print("Markdown Table:\n")
    print(markdown_table)
    # ^ just for reassurance that it works 
    actionable={}
    for item in items.keys():
         if items[item]['Status'] == 'WARN' or items[item]['Status'] == 'FAIL':
            actionable[item]={"Status": items[item]['Status']}
    # seems lame recreating another dict, probably a nicer way to do this
    # also nicer to dump it to a file I guess, but who knows where that will live
    print(dict_to_yaml(actionable))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python kb2yaml.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)
