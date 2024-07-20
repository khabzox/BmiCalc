# import libs
from pydantic import BaseModel

class BMIOutput(BaseModel):
    bmi: float
    message: str

# function of calculate bmi
def calculate_bmi(weight, height):
    # weight = float(input("Enter your weight in kilograms: "))
    # height = float(input("Enter your height in metres: "))
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        message = "You are underweight all the more 🍎"
    elif 18.5 <= bmi < 25:
        message = "You have a normal weight and maintain it 😁"
    elif 25 < bmi < 30:
        message = "You are overweight. Exercise more ⚽"
    else:
        message = "If you suffer from obesity, see a doctor 🏥"

    return BMIOutput(bmi=bmi, message=message)