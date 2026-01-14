from pathlib import Path

root = Path(__file__).resolve().parent
src = root / "bouncr copy 2.html"
dst = root / "bouncr copy.html"

header_token = "</header>"
footer_token = "<footer"

src_text = src.read_text(encoding="utf-8")
dst_text = dst.read_text(encoding="utf-8")

if header_token not in src_text or footer_token not in src_text:
    raise SystemExit("Source file missing header or footer token")
if header_token not in dst_text or footer_token not in dst_text:
    raise SystemExit("Destination file missing header or footer token")

src_after_header = src_text.split(header_token, 1)[1]
src_between = src_after_header.split(footer_token, 1)[0]

dst_before_header, dst_after_header = dst_text.split(header_token, 1)
dst_footer_rest = dst_after_header.split(footer_token, 1)[1]

new_text = dst_before_header + header_token + src_between + footer_token + dst_footer_rest

dst.write_text(new_text, encoding="utf-8")
