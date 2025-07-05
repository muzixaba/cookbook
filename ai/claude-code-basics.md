# Claude Code (CC) Basics
No indexing or external databases made from yout code

## Common workflows
1. Explore > Plan > Confirm > Code > Commmit
> Check the case for issue #934, then process a few fixes. Let me choose an approach before you code. ultrathink

2. Write tests > Commit > Code > Iterate > Commit
> Write tests for @utitls/file.py to make sure the requests are sent properley (note the tests will fails since links aren't yet implemeneted). Then commit. The update the code to make the tests pass.  

3. Write code > screenshot result > iterate
> Implement [some-impage.png] then screenshot with Puppeteer and iterate till it looks like the mock

4. Decide feature > Plan > Confirm > Code
> I want to add the ability for the user to upload their profile pic. Come up with a plan on how this could be achieved. Let me confirm if the plan if fine before your continue. think hard  

## Give CC some context
Place a `CLAUDE.md` file on root folder.  
This file will be read on all requests
`CLAUDE.local.md` is not check into git


## Starting CC
`claude`

## Creating a CLAUDE.md file
This file pulls context into Claude when starting a conversation

### CLAUDE.md contain any of the following:
- Bash commands
- Core files & utility functions
- Code style guidelines
- Testing instructions
- Repo etiquette (branch naming, merge vs rebase, etc)
- Dev environment setup
- Anything else Claude should know about the repo

### Where to create a CLAUDE.md file
- Project root `<root-folder>/CLAUDE.md` (can use `/init` for this)
- Any parent of the directory `root/foo/CLAUDE.md`
- Your home folder `~/.claude/CLAUDE.md`
- Create a local version `CLAUDE.local.md` that will be gitignored 

### Adding/Modifying content in CLAUDE.md
- Can add manually
- Use `#` to give Claude an instruction that will update CLAUDE.md
- Can use the `prompt improver` to fine tune instructions

### Start REPL with intial prompt
`claude "some query"` Starts REPL with an initial prompt
`claude -p "some query"` Query viw the SDK then exit
`cat file | claude -p "some query"` Process piped content
`claude -c` Continue most recent conversation
`claude -c -p "some query"` Continue via SDK
`claude -r "<session-id>" Resume session by ID
`claude update` Update to latest version
`claude mcp` Configure MCP servers

# Setting things up

## Slash Commands
`/init` Initialise project with CLUADE.md guide
`/clear` Clear the conversation history
`/config` View or modify config
`/cost` Show token usage stats
`/model` Select AI model
`/allowed tools` customise tool permissions
`/install-github-app` Tag `@claude` on GT issues & PRs
`/config` Turn on notifications
`/terminal-setup` Enable shift-enter to instert new lines
`/theme` Enable light/dark theme
`/vim` Enter vim mode
`/memory` Edit CLUADE.md memory files


## 1: Codebase Q & A (First Steps)
Asking CC questions about the codebase like the following:
- What is `@some_file.py` used for?
- Look at PR #2344, and let me know which functions were affected
- What did I ship last last week?

## 2: Editing Code
CC has the following tools to edit code
- `Bash` to run bash commands
- `file`
- `search`
- `file listing`
- `file read`
- `file write`
- `web fetch`
- `TODOs`
- `sub-agents`

## Managing allowed tools
- Select `Always allow` when prompted during a session
- Use the `/permissions` command to manage tool allowlist
- Manually edit `.claude/settings.json` or `~/.claude.json`
- Use the `--allowedTools` CLI flag for session-specific permissions

