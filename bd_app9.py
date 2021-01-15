from tkinter import Tk, Text, BOTH, W, N, E, S, END, messagebox
from tkinter.ttk import Frame, Button, Label, Entry, Style
import sqlite3 as sq

with sq.connect("book_of_recipes1.db") as con:
    cur = con.cursor()


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def delete_recipes(self):

        lbl = Label(self, text="Удаление рецепта")
        lbl.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5)
        lbl_satus = Label(self, text="")
        lbl_satus.grid(row=5, column=0, columnspan=1, rowspan=1, padx=5)

        field = Entry(self, width=20)
        field.grid(row=2, column=0, columnspan=1, rowspan=1, padx=5)

        def deleting():
            search_recipes = field.get()
            sql = "delete from book_of_recipes where recipe_name like '" + search_recipes + "%' "
            print(sql)
            cur.execute(sql)
            cur.connection.commit()
            lbl_satus.config(text = "Удалено")

        def close_delete_recipes():
            field.grid_remove()
            lbl.grid_remove()
            deleting.grid_remove()
            closing.grid_remove()
            lbl_satus.grid_remove()

        deleting = Button(self, text="Удалить", command=deleting)
        deleting.grid(row=3, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        closing = Button(self, text="Закрыть", command=close_delete_recipes)
        closing.grid(row=4, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

    def all_recipes(self):
        lbl = Label(self, text="Выбрать рецепты")
        lbl.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5)
        txt = Entry(self, width=80)
        txt.grid(row=2,column=0, columnspan=1, rowspan=1, padx=5)
        field = Text(self, width=80)
        field.grid(row=2, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        field.grid_remove()

        def close_all_recipes():
            lbl.grid_remove()
            txt.grid_remove()
            search.grid_remove()
            close_all.grid_remove()
            field.grid_remove()

        def all_recipes_search():
            search.grid_remove()
            txt.grid_remove()
            lbl.config(text='Рецепт')

            search_recipes = txt.get()
            sql = "select recipe from book_of_recipes where recipe_name like '"+ search_recipes + "%' "
            print(sql)
            cur.execute(sql)
            for row in cur.fetchall():
                field.insert(END, row[0])
            field.grid()
        search = Button(self, text="Поиск", command=all_recipes_search)
        search.grid(row=3, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        close_all = Button(self, text="Закрыть", command=close_all_recipes)
        close_all.grid(row=4, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

    def food_types(self):
        lbl = Label(self, text="Прочитать рецепты")
        lbl.grid(row=1, column=0)
        text1 = Label(self, text='')
        text1.grid(row=2, column=1)
        text2 = Label(self, text='')
        text2.grid(row=3, column=1)

        def soup_types():
            text1.config(text='Горячие')
            text2.config(text='Холодные')

        def salads_types():
            text1.config(text='Мясной')
            text2.config(text='Вегетарианский')

        def side_dishes_types():
            text1.config(text='Апперетив')
            text2.config(text='Соусы')

        def desserts_types():
            text1.config(text='Холодные')
            text2.config(text='Горячие')

        def close_food_types():
            lbl.grid_remove()
            salads.grid_remove()
            soups.grid_remove()
            side_dishes.grid_remove()
            desserts.grid_remove()
            to_close.grid_remove()
            text1.grid_remove()
            text2.grid_remove()

        salads = Button(self, text="Салаты", command=salads_types)
        salads.grid(row=2, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        soups = Button(self, text="Супы", command=soup_types)
        soups.grid(row=3, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        side_dishes = Button(self, text="Гарниры", command=side_dishes_types)
        side_dishes.grid(row=4, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        desserts = Button(self, text="Десерты", command=desserts_types)
        desserts.grid(row=5, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        to_close = Button(self, text="Закрыть", command=close_food_types)
        to_close.grid(row=8, column=1, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

    def new_recipe(self):  # создаём новый рецепт
        lbl = Label(self, text="Создание рецепта")
        lbl.grid(row=0, column=0)
        name_of_recipe = Text(self, width=20, height=1)
        name_of_recipe.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        recipe = Text(self, width=20, height=1)
        recipe.grid(row=2, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        products = Text(self, width=20, height=1)
        products.grid(row=3, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

        def is_full_text():  # функция, проверяющая пустое ли поле ввода: если оно пустое, программа не будет добавлять поля в БД(удобно)
            if (len(name_of_recipe.get('1.0', 'end')) > 1) and (len(recipe.get('1.0', 'end')) > 1) and (
                    len(products.get('1.0', 'end')) > 1):
                return 1
            else:
                return 0

        def add_recipe():  # функция добавления данных в БД, введённых в поле пользователем
            if is_full_text():  # проверяем, пустое ли поле
                cur.execute('''INSERT INTO book_of_recipes (recipe_name, recipe, products) VALUES (?, ?, ?)''',  # добавляем в базу данных
                            (name_of_recipe.get('1.0', 'end'), recipe.get('1.0', 'end'), products.get('1.0', 'end')))
                cur.connection.commit()
            name_of_recipe.delete('1.0', 'end')  # очищаем поля ввода
            recipe.delete('1.0', 'end')
            products.delete('1.0', 'end')

        def close_add_recipe():  # функция закрытия ячеек для добавления данных в БД
            lbl.grid_remove()
            name_of_recipe.grid_remove()
            recipe.grid_remove()
            products.grid_remove()
            to_close.grid_remove()
            to_add.grid_remove()

        to_close = Button(self, text="Закрыть", command=close_add_recipe)
        to_close.grid(row=7, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        to_add = Button(self, text="Добавить", command=add_recipe)
        to_add.grid(row=6, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

    def recipes_table(self):  # Вывод названий всех рецептов для чтения
        lbl = Label(self, text="Cписок рецептов")
        lbl.grid(row=1, column=0, columnspan=1, rowspan=1, padx=5)
        ent = Text(self, width=80)  # текстовое поле для вывода рецепта
        ent.grid(row=10, column=0, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        ent.insert(END, "Выберете рецепт")
        sql = "select recipe_name, recipe from book_of_recipes"  # выбираем имя рецепта и рецепт из БД
        cur.execute(sql)
        button = []  # создаём массив кнопок рецептов
        delets = []  # массив кнопок удаления
        updates = []  # массив кнопок обновления

        def show_text(text_show, res, de1, up1):  # показ выбранного рецепт
            ent.delete('1.0', END)
            ent.configure(state="normal")
            print(res)
            ent.insert(END, text_show)  # теперь нет лишнего отступа при при выводе рецепта
            de1.grid(row=7, column=1, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
            up1.grid(row=8, column=1, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

        def delete_recipe(result):  # удаление рецепта
            sql = "delete from book_of_recipes where recipe_name like '" + result + "%' "
            cur.execute(sql)
            messagebox.showinfo("Удаление рецепта", "Рецепт был удалён")  # информация об удалении рецепта
            cur.connection.commit()

        def update_recipe(result):  # функция обновления рецепта
            update_text = ent.get('1.0', 'end')
            sql = "UPDATE book_of_recipes SET recipe=? WHERE recipe_name like ?", (update_text, result)
            cur.execute(*sql)  # почитать про использование execute и args kwargs
            messagebox.showinfo("Обновление рецепта", "Рецепт был обновлён")
            cur.connection.commit()

        for row in cur.fetchall():  # добавляем все кнопки-рецепты на экран
            if row[0] != None:
                string = row[0]  # имя рецепта
                string_text = row[1]  # рецепт
                deleting = Button(self, text='Удалить', command=lambda j=string: delete_recipe(j))
                updating = Button(self, text='Обновить', command=lambda j=string: update_recipe(j))
                x = Button(self, text= string, command=lambda j=string_text, res=string, de1=deleting, up1=updating: show_text(j, res, de1, up1))
                button.append(x)  # добавляем очередную кнопку в массив
                delets.append(deleting)
                updates.append(updating)
        for i, x in enumerate(button):  # вывод кнопок на экран
            x.grid(column=0, row=i+2, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

        def close_all_recipes_sp():
           lbl.grid_remove()
           for i, x in enumerate(button):
               x.grid_remove()
           for i, deleting in enumerate(delets):
               deleting.grid_remove()
           for i, updating in enumerate(updates):
               updating.grid_remove()
           ent.grid_remove()
           cbtn.grid_remove()

        cbtn = Button(self, text="Закрыть", command=close_all_recipes_sp)  # закрываем окно со списком рецептов
        cbtn.grid(row=6, column=1, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)

    def initUI(self):
        self.master.title("Книга рецептов")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=5)
        to_choose_recipe = Button(self, text="Выбрать рецепт", command=self.all_recipes)  # чтение рецепта по поиску
        to_choose_recipe.grid(row=1, column=3, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        to_create_recipe = Button(self, text="Создать рецепт", command=self.new_recipe)  # создание нового рецепта
        to_create_recipe.grid(row=2, column=3, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        to_read_recipe = Button(self, text="Прочитать рецепт", command=self.food_types)  # виды блюд
        to_read_recipe.grid(row=3, column=3, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        delete_the_recipe = Button(self, text="Удалить рецепт", command=self.delete_recipes) # удаление рецепта по поиску
        delete_the_recipe.grid(row=4, column=3, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)
        recipe_table = Button(self, text="Cписок рецептов", command=self.recipes_table)  # список всех доступных рецептов
        recipe_table.grid(row=5, column=3, columnspan=1, rowspan=1, padx=5, sticky=E + W + S + N)


def main():
    root = Tk()
    root.geometry("900x700+300+300")
    app = Example()
    app.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
