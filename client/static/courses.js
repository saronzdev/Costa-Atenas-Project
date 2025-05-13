const h1 = document.getElementById("title")
const deleteBtn = document.getElementById("delete-btn")
const ul = document.getElementById("courses")

const updateData = (response, data) => {
  if (!response.ok) {
    h1.innerText = "No hay cursos"
    return
  }
  data.forEach(item => {
    const li = document.createElement("li")
    li.dataset.id = item.id
    li.classList.add("course-li")
    li.innerHTML = `
      <div class="course-card">
        <span id="span-name"><strong>Nombre:</strong> ${item.name}</span>
        <span id="span-price"><strong>Precio:</strong> ${item.price}</span>
      </div>
      <button class="delete-btn" data-id="${item.id}">Borrar</button>
    `
    ul.appendChild(li)
  })
}

const deleteData = async (id) => {
  const response = await fetch(`/api/courses/${id}`, {
    method: "DELETE"
  })
  if (!response.ok) {
    alert("Error deleting course...")
    return
  }
  await getData()
  alert("Borrado")
}

const getData = async () => {
  const response = await fetch("/api/courses/")
  const data = await response.json()
  ul.innerHTML = ""
  updateData(response, data)
}

await getData()

ul.addEventListener("click", async (e) => {
  if (e.target.classList.contains("delete-btn")) {
    const id = e.target.dataset.id
    await deleteData(id)
  }
})