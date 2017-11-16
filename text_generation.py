from chain import TrigramMarkovChain


def main():
    green_eggs_chain = TrigramMarkovChain('sample/greenEggs.txt')
    print(green_eggs_chain.generate_text())

if __name__ == '__main__':
    main()
