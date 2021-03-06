from rest_framework import serializers
from ..models import *



class CompetencyResultsSerializer(serializers.ModelSerializer):
    '''API serializers for Competency Ratings'''

    competencies = serializers.SerializerMethodField()

    def get_competencies(self,result):
        staff_results = {
            'organization':{
                'planning': result.organization.planning,
                'execution': result.organization.execution,
                'prioritization':result.organization.prioritization,
                'score':result.organization.score,
            },

            'innovation':{
                'vision_setting':result.innovation.vision_setting,
                'thinking':result.innovation.thinking,
                'adaptability':result.innovation.adaptability,
                'score':result.innovation.score,
            },

            'interpersonal_communication':{
                'investment_building': result.interpersonal_communication.investment_building,
                'effective_communication':result.interpersonal_communication.effective_communication,
                'delivery':result.interpersonal_communication.delivery,
                'score':result.interpersonal_communication.score,
            },

            'critical_thinking':{
                'data_compilation': result.critical_thinking.data_compilation,
                'data_analysis':result.critical_thinking.data_analysis,
                'problem_solving':result.critical_thinking.problem_solving,
                'continual_improvement':result.critical_thinking.continual_improvement,
                'score':result.critical_thinking.score,
            },

            'relationships':{
                'team_work':result.relationships.team_work,
                'stakeholder_management':result.relationships.stakeholder_management,
                'conflict_management':result.relationships.conflict_management,
                'score':result.relationships.score,

            },
        }
        return staff_results


    class Meta:
        model = CompetencyResults
        fields = ['pk','type','staff_id','last_modified','date_created','competencies']
