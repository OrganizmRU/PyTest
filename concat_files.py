
def main():

    def concat_files(file_out_name: str, lst: list) -> None:
        try:
            with open(file_out_name, 'w+', encoding='utf-8') as outfile:
                all_str = []
                for i in lst:
                    with open(i, 'r', encoding='utf-8') as infile:
                        for s in infile:
                            all_str.append(s)
                            outfile.write(s)
                        outfile.write('\n')
                    outfile.write('\n')
            print(all_str)
        except:
            print('Что-то пошло не так')

    # n = int(input())
    # lst = [input() for _ in range(n)]
    in_lst = ['in_text1.txt', 'in_text2.txt', 'in_text3.txt']
    concat_files('out_text123.txt', in_lst)





if __name__ == '__main__':
    main()
