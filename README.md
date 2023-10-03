# Pypwni v1.0

Designed for use with the HIBP v3 API with the T1 plan, which is rate limited to 10 requests per minute.

## To use:

1. Add your API key (required by HIBP) in main.py. You can adjust the sleep timer (defaulst to 7 seconds) as needed based on your API key tier.
2. Provide a newline seperated email list
3. Run the program.

## Requirements

- Written using Python 3.10.12, likely fine in 3.X
- Requests==2.31.0

## Future working goals

- Output breach data for emails in console as it comes in, instead of after post-processing.
- Add single email check option (already written in previous version, just need to implement into new code.)
- Exporting custom file name to "dataset" folder with timestamps appended.
- More ponies.
