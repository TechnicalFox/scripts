#!/bin/bash

openssl aes-256-cbc -a -d -in $1 -out $2
