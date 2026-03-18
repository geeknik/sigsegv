using System;
using System.Threading.Tasks;

namespace UsurperRemake.UI
{
    /// <summary>
    /// Displays the SIGSEGV splash screen.
    /// Kept text-first so it remains readable in BBS, SSH, and screen-reader contexts.
    /// </summary>
    public static class SplashScreen
    {
        private static readonly string[] SplashLines =
        {
            "SIGSEGV // THE HEAP LANDS",
            "Manage a server. Conquer a Lattice. Attain sudo.",
            "",
            "A generational rogue-like where code is law.",
            "",
            "BOOT > ROOT > PLAN > EXECUTE > EXTRACT",
            "Stay allocated. Stay dangerous. Never let the Garbage Collectors catch your PID."
        };

        public static async Task Show(dynamic terminal)
        {
            terminal.ClearScreen();

            bool isPlainText = false;
            try { isPlainText = terminal.IsPlainText; } catch { }

            terminal.WriteLine("");
            terminal.SetColor("bright_white");
            WriteCentered(terminal, SplashLines[0]);
            terminal.SetColor("gray");

            for (int i = 1; i < SplashLines.Length; i++)
            {
                WriteCentered(terminal, SplashLines[i]);
            }

            if (!GameConfig.ScreenReaderMode && !isPlainText)
            {
                terminal.WriteLine("");
                terminal.SetColor("white");
                WriteCentered(terminal, "root@sigsegv:~# bootstrap");
                terminal.SetColor("gray");
            }

            terminal.WriteLine("");

            string version = $"{GameConfig.ProductName} v{GameConfig.Version} \"{GameConfig.VersionName}\"";
            terminal.SetColor("gray");
            WriteCentered(terminal, version);

            terminal.SetColor("bright_white");
            WriteCentered(terminal, "Press any key...");
            terminal.SetColor("white");

            await terminal.WaitForKey("");
            terminal.ClearScreen();
        }

        private static void WriteCentered(dynamic terminal, string text)
        {
            int pad = Math.Max(0, (80 - text.Length) / 2);
            terminal.WriteLine(new string(' ', pad) + text);
        }
    }
}
