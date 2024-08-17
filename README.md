
    _____ _ _           ____             _            
    |  ___(_) | ___     / ___|  ___  _ __| |_ ___ _ __ 
    | |_  | | |/ _ \____\___ \ / _ \| '__| __/ _ \ '__|
    |  _| | | |  __/_____|__) | (_) | |  | ||  __/ |   
    |_|   |_|_|\___|    |____/ \___/|_|   \__\___|_|   

    Simple Python program to sort your files based on this: 

    .jpeg => "Pictures",
    .png => "Pictures",
    .jpg => "Pictures",
    .gif => "Pictures",
    .svg => "Pictures",

    .mp3 => "Sound",
    .wav => "Sound",
    .m4a => "Sound",

    .exe => "Setups",
    .lnk => "Setups",

    .c => "Code",
    .py => "Code",
    .java => "Code",
    .cpp => "Code",
    .js => "Code",
    .html => "Code",
    .css => "Code",
    .php => "Code",

    .torrent => "Torrents"

    default => "Unsorted"


## Options

### Once
This will sort all of the current (pre-existing) files within the directory into their respective folders. If the respective folder does not exist then it will be created.

### Future
This will sort all of the future files within the directory into their respective folder. If the respective folder does not exist then it will be created. This will keep running and keep sorting until program is terminated.


## Fun fact

While creating this python script I accidentally moved all of my .exe files in my downloads folder into a SINGLE file, not a directory. The result being a file with 3gb of data and my .exe files being mashed together into a single file with me not being able to recover them.
