const App = () => {
  const now = new Date()
  const a = 10
  const b = 20
  console.log(now, a+b)
  console.log('Hello from component')
  return (
    <div>
      <p>Hello world</p>
      <p>
        {a} plus {b} is {a + b}
      </p>
    </div>
  )
}

export default App