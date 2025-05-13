const form = document.getElementById("form-data")
const inputName = document.getElementById("name")
const inputPrice = document.getElementById("price")

form.addEventListener("submit", async e => {
  e.preventDefault()
  const name = inputName.value
  const price = parseFloat(inputPrice.value)
  await addCourse(name, price)
  inputName.value = ""
  inputPrice.value = ""
})

const addCourse = async (name, price) => {
  const response = await fetch("/api/courses/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({name, price})
  })
  if (response.ok) {
    //await getData()
    alert("Añadido")
  }
  else alert("Error")
}