from difflib import SequenceMatcher
from typing import BinaryIO, Optional, TextIO, Union
from .objects import S_ISGITLINK, Blob, Commit
from .pack import ObjectContainer
def write_commit_patch(f, commit, contents, progress, version=None, encoding=None):
    f.write(
        b"From "
        + commit.id
        + b" "
        + time.ctime(commit.commit_time).encode(encoding)
        + b"\n"
    )
    f.write(
        b"Date: " + time.strftime("%a, %d %b %Y %H:%M:%S %Z").encode(encoding) + b"\n"
    )
    f.write(
        ("Subject: [PATCH %d/%d] " % (num, total)).encode(encoding)
        + commit.message
        + b"\n"
    )

        p = subprocess.Popen(
            ["diffstat"], stdout=subprocess.PIPE, stdin=subprocess.PIPE
        )

    decoded = commit.message.decode(errors="replace")
        return f"{beginning}"
    return f"{beginning},{length}"


def unified_diff(
    a,
    b,
    fromfile="",
    tofile="",
    fromfiledate="",
    tofiledate="",
    n=3,
    lineterm="\n",
    tree_encoding="utf-8",
    output_encoding="utf-8",
):
            fromdate = f"\t{fromfiledate}" if fromfiledate else ""
            todate = f"\t{tofiledate}" if tofiledate else ""
            yield "--- {}{}{}".format(
                fromfile.decode(tree_encoding), fromdate, lineterm
            ).encode(output_encoding)
            yield "+++ {}{}{}".format(
                tofile.decode(tree_encoding), todate, lineterm
            ).encode(output_encoding)
        yield f"@@ -{file1_range} +{file2_range} @@{lineterm}".encode(
            output_encoding
        )
            if tag == "equal":
                    yield b" " + line
            if tag in ("replace", "delete"):
                    if not line[-1:] == b"\n":
                        line += b"\n\\ No newline at end of file\n"
                    yield b"-" + line
            if tag in ("replace", "insert"):
                    if not line[-1:] == b"\n":
                        line += b"\n\\ No newline at end of file\n"
                    yield b"+" + line
    return b"\0" in content[:FIRST_FEW_BYTES]
def write_object_diff(f, store: ObjectContainer, old_file, new_file, diff_binary=False):
    Note: the tuple elements should be None for nonexistent files
            return Blob.from_string(b"")

    f.writelines(
        gen_diff_header((old_path, new_path), (old_mode, new_mode), (old_id, new_id))
    )
    if not diff_binary and (is_binary(old_content.data) or is_binary(new_content.data)):
        f.writelines(
            unified_diff(
                lines(old_content),
                lines(new_content),
                patched_old_path,
                patched_new_path,
            )
        )
                yield ("old file mode %o\n" % old_mode).encode("ascii")
            yield ("new file mode %o\n" % new_mode).encode("ascii")
            yield ("deleted file mode %o\n" % old_mode).encode("ascii")
        yield (" %o" % new_mode).encode("ascii")

    f.writelines(
        gen_diff_header(
            (old_path, new_path),
            (old_mode, new_mode),
            (getattr(old_blob, "id", None), getattr(new_blob, "id", None)),
        )
    )
    f.writelines(
        unified_diff(old_contents, new_contents, patched_old_path, patched_new_path)
    )
        write_object_diff(
            f,
            store,
            (oldpath, oldmode, oldsha),
            (newpath, newmode, newsha),
            diff_binary=diff_binary,
        )
def git_am_patch_split(f: Union[TextIO, BinaryIO], encoding: Optional[str] = None):
    if isinstance(contents, bytes):
        bparser = email.parser.BytesParser()
        msg = bparser.parsebytes(contents)
        uparser = email.parser.Parser()
        msg = uparser.parsestr(contents)
        subject = msg["subject"][close + 2 :]
                c.author = line[len(b"From: ") :].rstrip()