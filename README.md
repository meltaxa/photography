# sd-copy

Copies your photos from a SD card to your computer.
Change the source and target appropriately.

Files are copied to a date based folder structure to help organize your photo library.

The modified date of the file becomes the target folder. For example, if you took a picture on 2 January 2016, the file will be copied to the following path: ~/Pictures/2016/2016/2016-01-02/000002.JPG.

The folder structure is:
```
   TARGET = ~/Pictures
              +-- /2016
                  +-- /2016-01-01 New Years
                  |   +-- 0000001.JPG
                  |
                  +-- /2016-01-02
                      +-- 0000002.JPG
                                 
```

The script will create the necessary directories and allows for custom names. If two folders start with the same date, then a folder ending with the word "latest" will be used. 

If the file already exists at the destination, it is skipped.
