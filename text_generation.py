from chain import MarkovChain


def main():
    green_eggs_chain = MarkovChain('sample/greenEggs.txt')
    print(green_eggs_chain.generate_text())

if __name__ == '__main__':
    main()
