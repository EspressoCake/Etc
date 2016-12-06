#!/bin/bash
file $(ls -d $1.[!.]?*)|sort -k2 -d