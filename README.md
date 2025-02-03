# EchoPress

EchoPress is a Python script designed to securely delete sensitive files on Windows systems, making them unrecoverable using advanced file recovery algorithms. It overwrites the contents of the file with random data multiple times before deleting it, ensuring that the data cannot be reconstructed.

## Features

- Overwrites files with random data a specified number of times.
- Renames the file to a random name before deletion to obscure its original name.
- Simple command-line interface for easy usage.

## Usage

1. Ensure you have Python installed on your Windows system.
2. Download the `EchoPress.py` script to your local machine.
3. Open a command prompt and navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python EchoPress.py
   ```

5. When prompted, enter the path of the file you want to securely delete.

## Important Note

- This script is intended for educational purposes. Use it responsibly and at your own risk. Ensure you have backups of important data before using this script.
- Once a file is securely deleted using EchoPress, it cannot be recovered.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The developers are not responsible for any data loss or damage caused by using this script. Ensure you understand the ramifications of securely deleting files before proceeding.