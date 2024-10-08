# Inspectio

## Overview

**Inspectio** is a powerful utility designed to help security assessors and penetration testers analyze logs for sensitive information. By leveraging regular expressions, it efficiently identifies and extracts potentially sensitive data, aiding in compliance and security assessments.

### Why Use Inspectio?

In today's digital landscape, sensitive data is frequently logged, posing security risks if not handled properly. Inspectio streamlines the process of detecting sensitive information within logs, allowing security professionals to focus on critical findings without wading through irrelevant data. This tool is essential for:

- **Security Assessments**: Quickly identify sensitive data during security assessments.
- **Compliance**: Ensure adherence to regulations like GDPR and HIPAA by monitoring log outputs.
- **Efficiency**: Save time and effort by automating the search for sensitive information.

## Installation

Install it easily using pip:
*pip install inspectio && python -m spacy download en_core_web_trf*

To install Inspectio manually, follow these steps:

1. **Clone the Repository**:
   ```
   git clone https://github.com/unpluggedsec/inspectio.git
   cd inspectio
   ```

2. **Build the package using below command:**

    ```
    python setup.py bdist_wheel
    ```
2. **Install the wheel:**

    ```
    pip install ./dist/inspectio*.whl
    ```
2. **Download Spacy model:**

    ```
    python -m spacy download en_core_web_trf
    ```
4. **Run the Utility: You can now run the utility using the following command:**

    ```
    inspectio --help
    usage: inspectio [-h] -l LOG [-f {json,raw,html}] [-o OUTPUT] [-r REGEX] [-i IGNORE]

    Secure Log Review Tool

    options:
    -h, --help            show this help message and exit
    -l LOG, --log LOG     Input log file path
    -f {json,raw,html}, --format {json,raw,html}
                            Output format (json, raw, html)
    -o OUTPUT, --output OUTPUT
                            Output file path (required if format is html or json)
    -r REGEX, --regex REGEX
                            Regex YAML file path
    -i IGNORE, --ignore IGNORE
                            File path containing ignore patterns
    ```

## Usage
Inspectio can be used from the command line with various options. Here are some common use cases:

### Normal Run
To analyze a log file for sensitive data using the default regex patterns, use the following command:

    ```
    inspectio -l path/to/your/logfile.log
    ```

### Ignore Patterns
If you want to exclude certain patterns from the analysis (say log dates which might spam your output due to default regex detecting dates), you can provide them in a separate file (see samples in misc/ignore_patterns.txt) using the -i option **(Line separated regexes)**:

    ```
    inspectio -l path/to/your/logfile.log -i path/to/ignore_patterns.yaml
    ```
### Additional Regex Patterns
To include additional regex patterns for matching, you can provide them in a separate file (see samples in misc/additional_patterns.txt) using the -r option **(Line separated regexes)**:

    ```
    inspectio -l path/to/your/logfile.log -r path/to/additional_patterns.yaml
    ```
### Example Command
Combining options, here’s an example command that uses a logfile with specified ignore patterns and additional regex patterns:

    ```
    inspectio -l path/to/your/logfile.log -i path/to/ignore_patterns.yaml -r path/to/additional_patterns.txt
    ```

## Output Formats
Inspectio supports multiple output formats. You can specify the output format using the -f option. Supported formats include:

1. JSON: Output results as a JSON file.
2. Raw: Default text output.
3. HTML: Generate an HTML report of the findings.

Example:
To output results in JSON format:

    ```
    inspectio -l path/to/your/logfile.log -f json -o output.json
    ```

## Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

## License
This utility is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software under the following terms:

- **Attribution**: You must give appropriate credit to the original creator (Ayman Abdul Kareem), provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

For more details, please refer to the full license text in the `LICENSE` file.

## Acknowledgments
Thank you for using Inspectio! Your feedback is invaluable to us as we continue to improve the utility.

## Credits
This utility uses regex patterns adapted from [secrets-patterns-db](https://github.com/mazen160/secrets-patterns-db), licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
