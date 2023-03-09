import pynecone as pc


class State(pc.State):
  items = ["Learn Python", "Learn Pynecone", "Have Fun"]
  new_item: str
  
  def add_item(self):
    self.items += [self.new_item]
    self.new_item = ""
  
  def finish_item(self, item):
    self.items = [i for i in self.items if i !=item]
    
    
def render_item(item):
  return pc.list_item(
    pc.hstack(
    pc.text(item, font_size="1.5em"),
    pc.button(
      "X",
      color_scheme="red",
      size="sm",
      on_click=lambda: State.finish_item(item),
      ),
    justify_content="space-between",
    )
  )
    
def todo_list():
  return pc.container(
    pc.vstack(
      pc.heading("Todos"),
      pc.input(
        on_blur=State.set_new_item,
        placeholder = "Add a todo ...",
        bg="white",
      ),
      pc.button("add", on_click=State.add_item, bg='green', color='white'),
      pc.divider(),
      pc.ordered_list(
        pc.foreach(
          State.items, lambda item: render_item(item)
        ),
      ),
      bg="#ededed",
      margin="5em",
      padding="1em",
      border_radius="0.5em",
      shadow="1lg",
    )
  )
    
    
    
app = pc.App(state=State)
app.add_page(todo_list,path="/")
app.compile()