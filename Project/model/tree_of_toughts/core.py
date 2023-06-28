# *************************************************************************** #
#                                                                              #
#    core.py                                                                   #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/06/21 15:02:33 by Widium                                    #
#    Updated: 2023/06/21 15:02:33 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append("/home/widium/Programming/AI/GPT4-Summarizer/Project")

from pprint import pprint

from typing import Any, List, Dict
from openai import Completion
from openai import ChatCompletion

from pathlib import Path

from functions.utils.file import read_content
from functions.utils.file import renplace_token
from functions.utils.file import verify_file_path

from .role import RoleCreator
from .generator import ToughtGenerator
from .evaluator import ToughtEvaluator
from .selector import ToughtSelector

from .. api import setup_api_key

setup_api_key(key="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")

class TreeOfToughtModel:
    
    def __init__(
        self,
        model_version : str,
        prompt_path : str,
        tree_width : int = 3,
        iterations : int = 3,
    ):
        
        self.model = model_version
        self.tree_width = tree_width
        self.iterations = iterations
        
        PROMPT_PATH = Path(prompt_path) 
        
        role_path = PROMPT_PATH / "role" / "main_role.txt"
        speciality_role_path = PROMPT_PATH / "role" / "summarizer.txt"
        task_path = PROMPT_PATH / "task" / "summarization.txt"
        init_generator_path = PROMPT_PATH / "generator" / "first_generator.txt"
        generator_path = PROMPT_PATH / "generator" / "generator.txt"
        evaluator_path = PROMPT_PATH / "evaluator" / "evaluator.txt"
        selector_path = PROMPT_PATH / "evaluator" / "selector.txt"
        
        verify_file_path(
            filepaths=[
                role_path,
                speciality_role_path,
                init_generator_path,
                generator_path,
                evaluator_path,
                selector_path,
                task_path,
            ]
        )
        
        self.role = RoleCreator(
            main_role_path=role_path,
            speciality_path=speciality_role_path,
        )
        
        self.task = read_content(filepath=task_path)
        
        self.generator = ToughtGenerator(
            init_prompt_path=init_generator_path,
            generator_prompt_path=generator_path,
            nbr_to_generate=self.tree_width,
        )
        
        self.evaluator = ToughtEvaluator(
            prompt_file_path=evaluator_path,
        )
        
        self.selector = ToughtSelector(
            prompt_file_path=selector_path,
        )
        
            
    
    def gpt_response(self, messages : List[Dict]) -> str:
        
        generations = ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=0
        )

        response = generations.choices[0]["message"]["content"]
        
        return (response)
    
    def init_reasoning(self, content : str)->str:
        
        self.task = renplace_token(
            prompt=self.task,
            token="<CONTENT>",
            value=content,
        )
        
        generator_prompt = self.generator(
            task=self.task,
            previous_winner=None,
        )
        
        init_message = [
            self.role(),
            generator_prompt,
        ]
        
        first_solutions = self.gpt_response(messages=init_message)
        
        return (first_solutions)
    
    def generate_solutions(self, previous_winner : str) -> str:
        
        message = self.generator(
            task=self.task,
            previous_winner=previous_winner,
        )
        
        solutions = self.gpt_response(messages=[message])
        return (solutions)
        
    
    def evaluate_solutions(self, solutions : str) ->str:
        
        message = self.evaluator(
            toughts=solutions,
            task=self.task,
        )
        
        evaluation = self.gpt_response(messages=[message])
        return (evaluation)
    
    def select_solutions(self, evaluation : str) ->str:
        
        message = self.selector(
            toughts=evaluation,
        )
        
        selection = self.gpt_response(messages=[message])
        return (selection)
    
    
    def reasoning(self, content : str)->str:
        
        first_solutions = self.init_reasoning(content=content)
        print("\n---- FIRST SOLUTIONS : ----\n", first_solutions)
        evaluation = self.evaluate_solutions(solutions=first_solutions)
        print("\n---- EVALUATION : ----\n", evaluation)
        selection = self.select_solutions(evaluation=evaluation)
        print("\n---- SELECTION: ----\n", selection)
        # return (selection)
        
        