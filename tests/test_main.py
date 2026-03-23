#!/usr/bin/env python3


def test1():
    from main import count_csms

    nr_csms: int = count_csms("data/csms.txt")
    assert nr_csms == 826
