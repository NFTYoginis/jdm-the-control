# How to run a clean no-folder control on claude.ai

Written for anyone re-running this repo (mods included) and for the next person who runs a control. Learned the hard way: five of our runs were protocol-invalid and were thrown out, and none of them looked wrong until the reply text gave it away. They are kept in `control/discarded/`, `treatment/discarded/` and `behavior/discarded/`.

A contaminated control reads as a result. Check each of these before you score a run.

1. **Chrome Incognito is not Claude incognito.** Use the ghost icon on a new chat page. The real switch shows an "Incognito" banner and the line "No history, memory, or Claude training." A chat that appears under Today in the sidebar is not incognito (our `run-0c`).
2. **Connectors stay on across chats.** Check the + menu on every run. Our `run-0b` searched Google Drive and Notion, and the reply said so.
3. **Web search can run unprompted**, even in incognito. A clean run has no "Searched the web" or "Used ..." line above the reply (our behavior `run-0a`).
4. **A reply that mentions "your past chats" or a Docs tool** means history or tools were reachable. Discard the run and keep the file with the reason.
5. **Projects cannot be incognito.** For the treatment arm, turn off Project > Memory > "Use account memory" and confirm project memory is empty.
6. **Project setup:** instructions go in the Instructions field and the files in Context. Sending the instruction line as a chat message, or chatting outside the Project, silently gives you a no-folder run (our treatment `run-0a`).
7. **The copy button drops markdown list numbers**, and curly apostrophes can break a regex. If a scorer needs answers numbered 1 to 9, restore the numbers and say so in the run file.

Keep every discarded run with its reason. Do not drop the bad run.
