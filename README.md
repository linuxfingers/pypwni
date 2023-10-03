# PYPWNI v1.0

This program was written for use with the "Have I Been Pwned?" v3 API, specifically using the Tier 1 API which is rate-limited to 10 requests per minute. 

## USAGE

```
-f, --file                  Location of the text file to load.
-o, --output_file           Where the output file should go.
```

The command syntax looks like:

`python3 pypwni.py -f <your_input_file> -o <your_output_file>`

Where `<your_input_file>` is a newline seperated list of emails, and `<your_output_file>` is where you'd like to save your CSV file.

✭ Before running the program for the first time, you need to add your API key to the `hibp_api_key` on line 12 of `pypwni.py`. Pypwni **will not work** if you don't add an API key. Sorry.

If you are using T2 or higher, you can change the sleep timer on line 60 of `pypwni.py`.

## REQUIREMENTS

- The program was written using Python 3.10.12, but is likely fine in 3.X. Feel free to test and let me know what breaks.
- You will need the Python module Requests (2.31.0).

## FUTURE GOALS

I'd like to make it Pypwni a little more robust in the future by:

- Outputting breach data for emails in console as it comes in, instead of after post-processing.
- Add the ability to search for a single email.
- Exporting custom file names to "dataset" folder with timestamps appended.
- Adding domain search functionality.
- Putting in more ponies.

Enjoy! :)
