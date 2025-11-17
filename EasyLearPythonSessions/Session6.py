

Subject1 = "EMail"
Task1 = "Generate an email body to inform the cousulate that I will be missing the visa interview"

def RunLLMTask(Subject,Task):
    print(Subject,":",Task)
    return Subject + ":" + Task


T1 = RunLLMTask("SendSMS","Send an sms to home that i will be late")
T2 = RunLLMTask(Subject1,Task1)

print(T1)


def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

sum = add(5,10)

print(sum)
