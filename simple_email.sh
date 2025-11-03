#!/bin/dash

echo "Image attached? (yes/no)"
read answer

echo "Address this email to?"
read email

echo "Subject?"
read subject

echo "Message to accompany image?"
read emailMessage

if [ "$answer" = "yes" ]; then
    echo "Please provide the image file(s) to attach (space-separated):"
    read files  # no arrays in dash, just space-separated list

    # Check all files exist
    for file in $files; do
        if [ ! -f "$file" ]; then
            echo "File '$file' does not exist. Exiting."
            exit 1
        fi
    done

    echo "$emailMessage" | mutt -s "$subject" -e 'set copy=no' -a $files -- "$email"

    if [ $? -eq 0 ]; then
        echo "Email with attachments sent to $email."
    else
        echo "Failed to send email with attachments."
    fi

else
    echo "$emailMessage" | mail -s "$subject" "$email"

    if [ $? -eq 0 ]; then
        echo "Plain email sent to $email."
    else
        echo "Failed to send plain email."
    fi
fi
