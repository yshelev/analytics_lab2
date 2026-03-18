from src.services.LLMQueryService import LLMQueryService
from src.services.LLMQueryBuilder import LLMQueryBuilder
from src.config import LLMConfig
from src.constants import user_prompt_base, system_prompt 
import pandas as pd
import json

class LLMService: 
    query_service: LLMQueryService 
    query_builder: LLMQueryBuilder
    
    def __init__(self):
        self.input_filename = "data/input.csv"
        self.output_filename = "data/output.csv"
        
        llm_config = LLMConfig()
        
        self.query_builder = LLMQueryBuilder(
            system_prompt=system_prompt,
            user_prompt_base=user_prompt_base
        )
        
        self.query_service = LLMQueryService(
            llm_config=llm_config
        )
    
    def proccess_csv(self) -> bool: 
        df = pd.read_csv(self.input_filename)
        
        review = df.sample(n=1).iloc[0].to_dict()["review"]
        
        prompt = self.query_builder.build(review)
        
        response, error = self.query_service.proccess_query(prompt["system_prompt"], prompt["user_prompt"])
        if error: 
            return
        
        # тут по хорошему парсить ответ, однако модель довольно хорошо отвечает, системный промпт нормальный и
        # просит модель отвечать сразу в json формате, поэтому я просто записываю ответ в json
        with open('data/output.json', 'w', encoding='utf-8') as f:
            f.write(response)
        