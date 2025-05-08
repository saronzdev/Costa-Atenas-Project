const getData = async () => {
  const response = await fetch("/api/courses")
  const result = await response.json()
  if (response.ok) return result
  else return {"msg": "error"}
}

const data = await getData()
const ul = document.getElementById("courses")
const h1 = document.getElementById("title")
const form = document.getElementById("form")
const inputName = document.getElementById("name")
const inputPrice = document.getElementById("price")

if (data.msg !== "error") {
  data.forEach(item => {
    const element = `<li>Nombre: ${item.name}    Precio${item.price}</li>`
    ul.insertAdjacentHTML("beforeend", element)
  })
}
else h1.innerText = "No hay cursos"

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
  if (response.ok) alert("Añadido")
  else alert("Error")
}



