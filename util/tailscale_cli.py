import subprocess

class TailscaleCli:
    """
    A class to handle Tailscale CLI operations.
    """

    def __init__(self, tailscale_path: str = "tailscale"):
        self.tailscale_path = tailscale_path

    def run_command(self, command: str) -> str:
        """
        Run a Tailscale CLI command and return the output.
        """

        result = subprocess.run(
            [self.tailscale_path] + command.split(),
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    
    def up(self):
        """
        Bring up the Tailscale interface.
        """
        return self.run_command("up")
    
    def down(self):
        """
        Bring down the Tailscale interface.
        """
        return self.run_command("down")