#!/bin/bash
# Linux:
# soffice --calc --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager"
# Mac:
# /Applications/LibreOffice.app/Contents/MacOS/soffice --calc \
# --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager"
# Windows:
# "C:\\Program Files (x86)\LibreOffice 5\program\soffice.exe" --calc --accept="socket,host=localhost,port=2002;urp;"

# Checking for OS type and running LibreOffice Calc
# case "$OSTYPE" in
#   solaris*) echo "SOLARIS OS is not supported" ;;
#   darwin*)  /Applications/LibreOffice.app/Contents/MacOS/soffice --calc --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager" ;;
#   linux*)   soffice --calc --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager" ;;
#   bsd*)     echo "BSD OS is not supported" ;;
#   msys*)    "C:\\Program Files (x86)\LibreOffice 5\program\soffice.exe" --calc --accept="socket,host=localhost,port=2002;urp;" ;;
#   *)        echo "unknown: $OSTYPE" ;;
# esac

soffice --accept="socket,host=localhost,port=2002;urp;" --norestore --nologo --nodefault # --headless
