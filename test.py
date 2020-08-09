from ulang import parse

TEST_SOURCE = """

func abc(a, b, c) {
    b = a
}

func main() {
    a = 1
    b = 2
    c = abc(
        a=a,
        b=b,
        c=c,
    )
}

"""

print(parse(TEST_SOURCE).pretty())
