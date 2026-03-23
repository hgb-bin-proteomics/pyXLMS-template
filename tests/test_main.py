#!/usr/bin/env python3


def test1():
    from main import count_csms

    nr_csms: int = count_csms("data/csms.txt")
    assert nr_csms == 826


def test2():
    from main import main

    status: int = main(["data/csms.txt"])
    assert status == 0
