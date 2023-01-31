import pynvim
from pynvim import Nvim
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()

PROMPTS_FILE = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"

@pynvim.plugin
class ChatGPT(object):
    def __init__(self, nvim: Nvim):
        self.nvim = nvim

    @pynvim.command("ChatGPT", nargs="*", range="", sync=False)
    def chatgpt(self, args, range):
        self.nvim.out_write("testing\n")
