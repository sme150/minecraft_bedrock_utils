# Minecraft Bedrock Utils

Welcome!  The purpose of this repository is to provide some utilities to help out your Minecraft (Bedrock Edition) gameplay.  Nothing around dupes, cheats, etc, just some calculation tools to save you a bit of time.

So far, we've only added a Guardian farm spawn mapper, which I am sure already exists, but we are open to providing more quick calculation tools as we find them or requests come in. 

# Requirements

You can either access the helper scripts directly after downloading the repo locally (Python 3.X required), or you can use the provided docker commands to remove the need to download and run Python locally (Docker is required, and you can either build the docker image locally, or reference our docker image on Docker hub)

## Running locally
- Pros/Cons:  Docker not required, but python3 must be installed
- Download to repo locally and `cd` into the root directory of the repo, and run the command for the tool you wish to use.
	> Guardian Spawn Mapper: `python guardian_mapper.py <monument_topleft_corner_x_coord> <monument_topleft_corner_z_coord>`

## Using Docker image

- Pros/Cons: No repo download or python required, but docker must be installed
	> Guardian Spawn Mapper: `docker run scottestes/minecraft-bedrock-utils:latest python guardian_mapper.py <monument_topleft_corner_x_coord> <monument_topleft_corner_z_coord>`

