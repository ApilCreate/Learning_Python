# re = "regular expression" module. Lets us search/match text against a pattern
# instead of chaining lots of .replace() / .startswith() / slicing calls.
import re

url = input("URL: ").strip()

# --- Earlier, simpler attempts (kept for reference) ---
# .replace() only works if the prefix matches EXACTLY (case, http vs https, www or not).
# username = url.replace("https://twitter.com/", "")
# .removeprefix() has the same problem - no flexibility, no "optional" parts.
# username = url.removeprefix("https://twitter.com/", "")
# print(f"Username: {username}")

# re.sub(pattern, repl, string, count=0, flags=0)
# re.sub() finds text matching "pattern" and replaces it with "repl".
# Here it would strip the whole domain part, leaving just the username.

# ? means "0 or 1 of the thing right before it" -> makes that thing OPTIONAL.
# So (https?://)? means: "http:// or https://, and even that whole group is optional".
# username = re.sub(r"^(https?://)?(www\.|)?twitter\.com/", "", url)

# print(f"Username: {username}")


# re.search(pattern, string, flags) scans the string for the FIRST place the
# pattern matches, and returns a "Match" object (or None if nothing matches).
# The walrus operator (:=) lets us assign the result to `matches` AND check it
# in the same `if`, instead of doing `matches = re.search(...)` then `if matches:`.
#
# Breaking down the pattern r"^https?://(?:www\.)?twitter\.(.+)/(\w+)$":
#   ^            - start of the string (nothing allowed before this point)
#   https?       - "http" or "https" (the "s" is optional, see ? above)
#   ://          - literal "://"
#   (?:www\.)?   - an OPTIONAL, NON-CAPTURING group for "www."
#                  (?: ... ) groups things WITHOUT saving it as matches.group(N),
#                  because we don't actually need the "www." text later.
#   twitter\.    - literal "twitter." (the backslash escapes "." so it means
#                  an actual dot, not "any character")
#   (.+)         - CAPTURING group 1: one-or-more of ANY character.
#                  This grabs the domain ending, e.g. "com" or "com.au".
#   /            - literal "/" separating domain from username
#   (\w+)        - CAPTURING group 2: one-or-more "word" characters
#                  (letters, digits, underscore) -> the actual username.
#   $            - end of the string (nothing allowed after this point)
#   re.IGNORECASE - makes the match case-insensitive, so "HTTPS://TWITTER.COM/x"
#                    still matches.
#
# ^...$ together force the WHOLE url to match this shape, not just part of it.
if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(\w+)$", url, re.IGNORECASE):
    # matches.group(1) = whatever (.+) captured -> should be "com" for a real
    # twitter.com link (rejects lookalikes like "twitter.evil.net/user").
    if matches.group(1) == "com":
        # matches.group(2) = whatever (\w+) captured -> the username itself.
        print(f"Username:", matches.group(2))
else:
    print("Wrong url")