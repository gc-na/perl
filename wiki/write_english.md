# [Unix] C Shell (csh) write usage: Send messages to other users

## Overview
The `write` command in C Shell (csh) is used to send messages to other users who are logged into the same system. This command allows for real-time communication between users, making it a useful tool for collaboration or simply checking in with colleagues.

## Usage
The basic syntax of the `write` command is as follows:

```csh
write [options] [username]
```

## Common Options
- `-n`: Suppresses the printing of the user's terminal name.
- `-h`: Sends a message to the user without notifying them.
  
## Common Examples

1. **Send a message to a user:**
   To send a message to a user named "john":
   ```csh
   write john
   ```
   After executing this command, you can type your message and press `Ctrl+D` to send it.

2. **Send a message without terminal name:**
   To send a message to "jane" without showing your terminal name:
   ```csh
   write -n jane
   ```
   Type your message and press `Ctrl+D`.

3. **Send a hidden message:**
   To send a message to "doe" without notifying them:
   ```csh
   write -h doe
   ```
   Again, type your message and press `Ctrl+D`.

## Tips
- Ensure that the user you are trying to message is logged in and has not disabled message reception.
- Use `who` command to check who is currently logged in before sending messages.
- To stop receiving messages, a user can use the `mesg n` command.