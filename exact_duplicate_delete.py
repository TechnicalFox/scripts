#!/usr/bin/env python
"""
    File name: exact_duplicate_delete.py
    Author: Jim Craveiro <jim.craveiro@gmail.com>
    Date: 2/26/2017
    
    Deletes duplicate files found in specified dir and sub-dirs.
"""

import hashlib
import os
import sys

def sha_256_sum(file_path):
    """Reads in a file and returns the sha256 hash of its contents.

    Args:
        file_path (str): the absolute or relative path to the file being hashed
    
    Returns:
        str: sha256 hash value of file contents
    """ 
    hash_buffer = hashlib.sha256()

    # reads in the specified file and adds the contents to the data to be hashed    
    with open(file_path, "rb") as infile:
        hash_buffer.update(infile.read())
    
    # hashes data in buffer and returns it
    return hash_buffer.hexdigest()

def recursive_parse_dir(target_path, hashes=[]):
    """Deletes duplicate files in specified dir and sub-dirs.
    
    Goes through every item in a specified directory and if it is a file
    it hashes its contents and then checks if the hash exists in a list.
    If it does not, it adds the hash to the list, otherwise it deletes the
    file because it is an exact duplicate. If it is a directory it recursively
    calls itself with the new target dir, and the current list of hashes, 
    returning the new hash list when it is done with a sub-dir.
    
    Args:
        target_path (str): the absolute or relative path to be traversed
        hashes (list[str]): current list of known files, defaults to an empty list
    
    Returns:
        hashes (list[str]): see above
    """
    if target_path[-1] != "/": target_path += "/"
    dir_contents = os.listdir(target_path)
    
    for item in dir_contents:
        full_path = target_path + item
    
        if os.path.isfile(full_path):
            file_hash = sha_256_sum(full_path)
            
            # check if the file is a duplicate
            if file_hash in hashes:
                os.remove(full_path)
            else:
                hashes.append(file_hash)        
        
        elif os.path.isdir(full_path):
            hashes = recursive_parse_dir(full_path, hashes)

    return hashes

def main():
    """Main function gets command line input and starts the parsing."""
    help_text = "Please pass in the target path as an argument."
    
    # don't allow the program to run without a path passed from the command line
    if len(sys.argv) <= 1:
        print help_text
    
    else:
        # allows for help to trigger informative text to be printed to the command line
        if sys.argv[1].lower() == "help":
            print help_text
    
        else:
            recursive_parse_dir(sys.argv[1])

if __name__ == "__main__":
    main()
