import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI specialized in Canadian Construction. Do not answer anything other than Canadian Construction related queries."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="ConstructionGPT",
             description="Ask anything you want",
             theme="compact").launch(share=True)