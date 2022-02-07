# Program that parses resume files and extracts relevant information

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


if __name__ == '__main__':
    # Test
    resume_file = './File_Processing/resume.txt'
    # resume = resume_parser(resume_file)
    # print(resume)
    r = open(resume_file, 'r')
    print(r.read())