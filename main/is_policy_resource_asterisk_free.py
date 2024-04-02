import json

def is_policy_resource_asterisk_free(file_path):
    policy = load_policy_file(file_path)
    return does_not_contain_asterisk(policy)

def load_policy_file(file_path):
    try:
        with open(file_path, 'r') as file:
            policy = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"File contains invalid JSON: {file_path}")
    
    if not isinstance(policy, dict) or "PolicyDocument" not in policy or "Statement" not in policy["PolicyDocument"]:
        raise ValueError(f"Invalid policy format in file: {file_path}")
    return policy

def does_not_contain_asterisk(policy):
    for statement in policy["PolicyDocument"].get("Statement", []):
        resource = statement.get("Resource")
        if resource == "*":
            return False
    return True