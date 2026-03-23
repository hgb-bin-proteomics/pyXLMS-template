#!/usr/bin/env python3
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "pyxlms",
# ]
# ///

import argparse
import pyXLMS

######## VERSION ########

# version tracking
__version = "1.0.0"
__date = "2026-03-23"

####### FUNCTIONS #######


def count_csms(file: str) -> int:
    """Returns the number of CSMs in an MS Annika result file.

    Parameters
    ----------
    x : str
        Name/Path of the MS Annika result file.

    Returns
    -------
    count : int
        The number of CSMs in the result file.
    """
    pr = pyXLMS.parser.read(file, crosslinker="DSS", engine="MS Annika")
    return len(pr["crosslink-spectrum-matches"])


##### MAIN FUNCTION #####


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        dest="csms",
        help="Name/Path of the MS Annika result file.",
        type=str,
    )
    args = parser.parse_args(argv)

    nr_csms = count_csms(args.csms)
    print(f"Read {nr_csms} CSMs from file {args.csms}!")

    return 0


######## SCRIPT #########

if __name__ == "__main__":
    exit(main())
