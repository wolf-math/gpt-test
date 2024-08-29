from api import get_gpt_response


def main():
    message = input("Ask the AI a question!!!")

    res = get_gpt_response(message)

    print(res)


if __name__ == "__main__":
    main()