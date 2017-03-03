# scripts
Collection of quick scripts I wrote. All licenced under MIT licence, so do whatever you want with them...

===
encrypt.sh
- just a small bash script that encrypts the a file using aes-256-cbc with salt, and hashes it using base64.
- usage: ./encrypt.sh (file to encrypt) (output encrypted file)

decrypt.sh
- another small bash script, except it decrypts files encrypted with aes-256-cbc that are also hashed using base64.
- usage: ./decrypt (file to decrypt) (output decrypted file)

purge.sh
- small bash script that overwrites specified files with random data using dd, then removes them.
- usage: ./purge (file to purge) [more files to purge]...

exact_duplicate_delete.py
- python script that parses a directory and all sub-directories, and deletes any files it finds who's hash exactly match
  an file that it already hashed. it uses SHA256 as its hashing algorithm. it's currently not scalable, as it just stores them in a
  list, which would use a lot of memory in large directory trees, but I plan on making it use a sqlite3 db in the future.
  
