from neuralintents import GenericAssistant
import pandas_datareader as web
import sys

stocks_tickers=[
    'APPLE','FB','GS','TSLA'
]
todos=["Wash Car","Watch Anime","Go Shopping","Do Coding"]


def stock_function():
    for ticker in stocks_tickers:
        data=web.DataReader(ticker,'yahoo')
        print(data)
        print(f"the last price of {ticker} was {data['Close'].iloc[-1]}")
    

def todo_show():
    print("Yyour Todo list")
    for todo in todos:
        print(todo)

def todo_add():
    todo=input("What TODO do You want To Add")
    todos.append(todo)

def todo_remove():
    idx=int(input("Which Todo To remove (number) : "))-1

    if idx < len(todos):
        print(f"removig {todos[idx]}")
        todos.remove(idx)
    else:
        print("There Is no todo list")

def bye():
    print("Bye")
    sys.exit()


mapping={
    'stocks':stock_function,
    'todoshow':todo_show,
    'todoadd':todo_add,
    'todoremove':todo_remove,
    'goodbye':bye,

}
assistent=GenericAssistant("shorts_intens.json",mapping)

# assistent.train_model()
assistent.load_model()
# assistent.save_modelhi()

while True:
    message=input("message :")
    assistent.request(message)