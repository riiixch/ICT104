let num = 2
let multi = 12
let author = "65064435 สมภพ เอี่ยมสมบีติ"

for (let i = 1; i < multi + 1; i++) {
    console.log(num + " * " + i + " = " + num * i)
    if (i === multi) {
      console.log(author)
    }
}