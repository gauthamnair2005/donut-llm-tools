class Tools:
    def LLMCreator(): 
        from createllm import CreateLLM

        print("AI/ML Model Trainer/Loader | DonutLLM Studio")
        while True:
            print("1. Create LLM")
            print("2. Load LLM")
            print("3. Exit")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                path = input("Enter the path of the dataset : ")
                mx_itr = input("Enter the maximum number of iterations : ")
                model = CreateLLM.GPTTrainer(path,max_iters=100)
                model = model.trainer()
            elif choice == 2:
                path = input("Enter the path of the model : ")
                model = CreateLLM.LLMModel(path)
                while True:
                    prompt = input("Enter prompt : ")
                    if prompt == "exit" or prompt == "Exit" or prompt == "EXIT" or prompt == "quit" or prompt == "Quit" or prompt == "QUIT":
                        break
                    else:
                        print(model.generate(prompt))
            elif choice == 3:
                break
            else:
                print("Invalid choice! Please enter a valid choice.")

    def DatasetCreator():
        import wikipedia
        import csv
        import signal
        import sys

        print("Donut Dataset Creator | DonutLLM Studio")

        def signal_handler(sig, frame):
            print('You pressed Ctrl+C!')
            sys.exit(0)

        def get_wiki_data(filename):
            first_page = True
            while True:
                try:
                    if first_page:
                        page_title = input("Enter Wikipedia page to start scrapping from : ")
                        first_page = False
                    else:
                        page_title = wikipedia.random(pages=1)
                    page_py = wikipedia.page(page_title)
                    with open(filename, mode='a', newline='', encoding='utf-8') as file:
                        print("Writing Wiki")
                        writer = csv.writer(file)
                        writer.writerow([page_py.title, page_py.summary])
                        print("Written Wiki")
                except KeyboardInterrupt:
                    break
                except wikipedia.exceptions.DisambiguationError as e:
                    print(str(e))
                except wikipedia.exceptions.PageError as e:
                    pass

        fileout = input("Enter output file name (with extension) : ")
        signal.signal(signal.SIGINT, signal_handler)
        get_wiki_data(fileout)


class HelpAndInfo:
    def create_llm():
        Tools.LLMCreator()
    
    def create_dataset():
        Tools.DatasetCreator()

    def help():
        print("DonutLLM Studio | AI/ML Model Trainer/Loader")
        print("1. Create LLM")
        print("2. Create Dataset")
        print("3. Exit")
        print("4. Help")
        print("5. About")

    def about():
        print("DonutLLM Studio | AI/ML Model Trainer/Loader")
        print("Version 24.05.27.2")
        print("Developed by Gautham Nair")

    def exit():
        print("Exiting DonutLLM Studio")
        exit()

    def main():
        while True:
            HelpAndInfo.help()
            choice = int(input("Enter your choice : "))
            if choice == 1:
                HelpAndInfo.create_llm()
            elif choice == 2:
                HelpAndInfo.create_dataset()
            elif choice == 3:
                HelpAndInfo.exit()
            elif choice == 4:
                HelpAndInfo.help()
            elif choice == 5:
                HelpAndInfo.about()
            else:
                print("Invalid choice! Please enter a valid choice.")