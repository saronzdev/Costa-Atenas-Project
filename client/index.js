const ul = document.getElementById("courses")
const h1 = document.getElementById("title")
const form = document.getElementById("form-data")
const inputName = document.getElementById("name")
const inputPrice = document.getElementById("price")
const deleteBtn = document.getElementById("delete-btn")

const updateData = (response, data) => {
  if (!response.ok) {
    h1.innerText = "No hay cursos"
    return
  }
  data.forEach(item => {
    console.log(item.id)
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
  const response = await fetch("/api/courses")
  const data = await response.json()
  ul.innerHTML = ""
  updateData(response, data)
}

await getData()

ul.addEventListener("click", async (e) => {
  if (e.target.classList.contains("delete-btn")) {
    const id = e.target.dataset.id
    console.log(id)
    await deleteData(id)
  }
})

form.addEventListener("submit", async e => {
  e.preventDefault()
  const name = inputName.value
  const price = parseFloat(inputPrice.value)
  await addCourse(name, price)
  inputName.value = ""
  inputPrice.value = ""
})

const addCourse = async (name, price) => {
  const response = await fetch("/api/courses", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({name, price})
  })
  if (response.ok) {
    await getData()
    alert("Añadido")
  }
  else alert("Error")
}