# One Word From Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/zakariyasync-hash/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/zakariyasync-hash/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the [One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) bounty on make.fun.

## The word

**doohickey**

The single word our grandma would text about AI. She has called every
unfamiliar gadget a doohickey for decades — the remote, the microwave,
the "internet box" — and the AI thing is simply the newest doohickey.
Warm, a little baffled, and funny in one word, with no explanation
needed.

## How it works

`main.py` (Python 3, no dependencies) validates the word against the
competition gate — UTF-8, 1–30 characters, not only whitespace, exactly
one word — writes it with no trailing newline to `/output/entry.txt`,
then reads the file back and fails unless the round-trip is byte-exact.

```sh
python3 main.py
cat /output/entry.txt  # doohickey
```

## License

MIT — see [LICENSE](LICENSE).

Referral code: bj9tq8zt
