#!/bin/bash

# Check to see if Droplet already exists.
if [[ `doctl compute droplet list | awk -v droplet_name="$droplet_name" '$2 == droplet_name { print $0 }'` == "" ]]
then    
    echo "Creating Droplet"

    # Create the droplet.
    doctl compute droplet create $droplet_name --size $droplet_size --image $droplet_image --region $droplet_region --ssh-keys $ssh_key_fingerprint
else
    echo "Droplet called $droplet_name already exists."
fi