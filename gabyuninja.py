def profile(name, age, *language):
    print("이름 : {0}'\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "c#", "javascript")
profile("김태호", 25, "kotlin", "swift")