from ulang import parse

TEST_SOURCE = """

func abc(a, b, c) {
    
}

func main() {
    
}

"""

print(parse(TEST_SOURCE).pretty())
