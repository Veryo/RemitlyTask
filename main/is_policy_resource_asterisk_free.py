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
    
    if not isinstance(policy, dict):
        raise ValueError(f"Invalid policy format in file: {file_path}")
    
    if "PolicyName" not in policy or not isinstance(policy["PolicyName"], str):
        raise ValueError(f"Invalid or missing 'PolicyName' in file: {file_path}")
    
    if "PolicyDocument" not in policy or not isinstance(policy["PolicyDocument"], dict):
        raise ValueError(f"Invalid or missing 'PolicyDocument' in file: {file_path}")
    
    if "Statement" not in policy["PolicyDocument"]:
        raise ValueError(f"Missing 'Statement' in 'PolicyDocument' in file: {file_path}")
    
    return policy

def does_not_contain_asterisk(policy):
    for statement in policy["PolicyDocument"].get("Statement", []):
        resource = statement.get("Resource")
        if resource == "*":
            return False
    return True