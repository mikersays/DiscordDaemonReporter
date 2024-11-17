# Discord Bot: Service Status Checker

A lightweight Discord bot to monitor and report the status of specified system services directly within a Discord channel.

## Features
- Responds to the `!status` command to check if specific services are running on the host system.
- Notifies whether the services are online, offline, or if there’s an error during the check.

## Prerequisites
Before running the bot, ensure you have:
1. Python 3.8+ installed on your system.
2. The `discord.py` library installed (`pip install discord.py`).
3. A Discord bot token from the [Discord Developer Portal](https://discord.com/developers/applications).

## Setup Instructions
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/mikersays/DiscordDaemonReporter.git
   cd DiscordDaemonReporter
   ```

2. **Install Dependencies**  
   ```bash
   pip install discord.py
   ```

3. **Configure the Bot**  
   - Open the `dbot.py` file.
   - Replace `YOUR_BOT_TOKEN` with your actual bot token from the Discord Developer Portal.
   - Replace `service1` and `service2` in the `check_services` function with the exact names of the services you want to monitor.  
     - For example:
       ```python
       service1_status = subprocess.run(['pgrep', '-x', 'nginx'], capture_output=True, text=True)
       service2_status = subprocess.run(['pgrep', '-x', 'mysql'], capture_output=True, text=True)
       ```
     - Use the exact process names as they appear in your system’s process list. You can check them with:
       ```bash
       pgrep -x <service-name>
       ```
     - Both services must be running for the bot to report that the system is online.

4. **Run the Bot**  
   ```bash
   python dbot.py
   ```

## Usage
1. Invite the bot to your Discord server using an OAuth2 URL generated from the Developer Portal.
2. In any text channel, type:
   ```
   !status
   ```
   The bot will respond with the status of the monitored services:
   - ✅ `All services are online.`
   - ❌ `One or more services are offline. Please check the scripts.`
   - ⚠️ `Error checking service status: <error message>.`

## Customization
- **Monitor Additional Services**: Add more checks to the `check_services` function by including additional `pgrep` commands.
- **Enhance Commands**: Extend the `on_message` function to support additional bot commands.

## Troubleshooting
- **Bot not responding**: Ensure the bot is online and has the necessary permissions for reading messages in the channel.
- **Incorrect service names**: Verify the process names with `pgrep -x <service-name>` and update the script accordingly.
- **Python errors**: Ensure the required Python version and `discord.py` library are installed.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to open an issue or pull request on GitHub.

## License
This project is open-source and available under the [MIT License](LICENSE).
