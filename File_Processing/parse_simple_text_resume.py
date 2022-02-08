# Program that parses resume files and extracts relevant information
from sys import argv

def resume_parser(resume_file):
    """
    Parses resume file and extracts relevant information
    Args:
        resume_file (str): path to resume file
    Returns:
        (dict): dictionary of extracted information
    """
    # Initialize dictionary
    resume = {}

    # Open file
    with open(resume_file, 'r') as f:
        # Read file line by line and extract relevant information
        for line in f:
            # Extract name
            if 'Name' in line:
                resume['Name'] = line.split(':')[1].strip()
            # Extract email
            elif 'Email' in line:
                resume['Email'] = line.split(':')[1].strip()
            # Extract phone number
            elif 'Phone' in line:
                resume['Phone'] = line.split(':')[1].strip()
            # Extract address
            elif 'Location' in line:
                resume['Location'] = line.split(':')[1].strip()
            # Extract education
            elif 'Education' in line:
                resume['Education'] = line.split(':')[1].strip()
            # Extract experience
            elif 'Experience' in line:
                resume['Experience'] = line.split(':')[1].strip()
            # Extract skills
            elif 'Skills' in line:
                resume['Skills'] = line.split(':')[1].strip()
            # Extract projects
            elif 'Projects' in line:
                resume['Projects'] = line.split(':')[1].strip()

    # Return dictionary
    return resume

def write(resume):
    """
    Writes resume information to a text file
    Args:
        resume (dict): dictionary of resume information
    """
    # Open file
    with open('parsed_resume.txt', 'w') as f:
        # Write name
        f.write('Name: ' + resume['Name'] + '\n')
        # Write email
        f.write('Email: ' + resume['Email'] + '\n')
        # Write phone number
        f.write('Phone: ' + resume['Phone'] + '\n')
        # Write address
        f.write('Location: ' + resume['Location'] + '\n')
        # Write education
        f.write('Education: ' + resume['Education'] + '\n')
        # Write experience
        f.write('Experience: ' + resume['Experience'] + '\n')
        # Write skills
        f.write('Skills: ' + resume['Skills'] + '\n')
        # Write projects
        f.write('Projects: ' + resume['Projects'] + '\n')

if __name__ == '__main__':
    # Test
    resume_file = argv[1]

    if resume_file is not None:
        resume = resume_parser(resume_file)
        write(resume)
    else:
        print('No file specified')