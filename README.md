# Temporal Accessibility

These are the tools used to generate maps of accessibility through
time. They're pretty customized to the data used for the project, but
may serve as a guide to folks wanting to do something similar.

## Workflow

Once you have your data as a CSV, you can use generateTimes.js to
generate a set of CSV files with a field indicating whether the
establishment is open at a given time. You'll get 168 CSV's, one for
each hour in a typical week.

You can then use generateConfigs.py to generate OpenTripPlanner batch
analyst configuration files for each CSV.

Then, use run.sh to run OpenTripPlanner Batch Analyst for each config.

You can then use animation.py to generate animations from your
GeoTIFF's. It runs in QGIS script runner.

## License

This code is licensed under the Apache License, version 2.
