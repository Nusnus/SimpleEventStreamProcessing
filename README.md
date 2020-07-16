# SimpleEventStreamProcessing

A basic code for processing an endless stream of integers based on a defined processors pipeline.

### Example Usage
```
if __name__ == '__main__':
    example_pipeline = Pipeline([
        ProcessorX(),
        ProcessorY(),
        ...
    ])

    example_pipeline.run_indefinitely()
```

## How to run

### Locally
Just run `run_locally.sh` (install [figlet](http://www.figlet.org/figlet-man.html) for the following effect locally) and you should see something like that if everything was done correctly:
```
 ____  _                 _        ___       _     _____                 _   
/ ___|(_)_ __ ___  _ __ | | ___  |_ _|_ __ | |_  | ____|_   _____ _ __ | |_ 
\___ \| | '_ ` _ \| '_ \| |/ _ \  | || '_ \| __| |  _| \ \ / / _ \ '_ \| __|
 ___) | | | | | | | |_) | |  __/  | || | | | |_  | |___ \ V /  __/ | | | |_ 
|____/|_|_| |_| |_| .__/|_|\___| |___|_| |_|\__| |_____| \_/ \___|_| |_|\__|
                  |_|                                                       
 ____                              _             
|  _ \ _ __ ___   ___ ___  ___ ___(_)_ __   __ _ 
| |_) | '__/ _ \ / __/ _ \/ __/ __| | '_ \ / _` |
|  __/| | | (_) | (_|  __/\__ \__ \ | | | | (_| |
|_|   |_|  \___/ \___\___||___/___/_|_| |_|\__, |
                                           |___/ 
(Ctrl+C to exit)
> 

```

### Running from a docker container
!! Assuming all docker dependencies are already set and configured as a normal user !!

Just run `run_in_docker.sh` and you should see something like that if everything was done correctly:
```
*** Simple Int Event Processing ***
(Ctrl+C to exit)
> 
```