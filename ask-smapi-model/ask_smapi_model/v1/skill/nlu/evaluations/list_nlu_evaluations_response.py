# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum
from ask_smapi_model.v1.skill.nlu.evaluations.paged_response import PagedResponse


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.skill.nlu.evaluations.pagination_context import PaginationContext as Evaluations_PaginationContextV1
    from ask_smapi_model.v1.skill.nlu.evaluations.evaluation import Evaluation as Evaluations_EvaluationV1
    from ask_smapi_model.v1.skill.nlu.evaluations.links import Links as Evaluations_LinksV1


class ListNLUEvaluationsResponse(PagedResponse):
    """
    response body for a list evaluation API


    :param pagination_context: 
    :type pagination_context: (optional) ask_smapi_model.v1.skill.nlu.evaluations.pagination_context.PaginationContext
    :param links: 
    :type links: (optional) ask_smapi_model.v1.skill.nlu.evaluations.links.Links
    :param evaluations: 
    :type evaluations: (optional) list[ask_smapi_model.v1.skill.nlu.evaluations.evaluation.Evaluation]

    """
    deserialized_types = {
        'pagination_context': 'ask_smapi_model.v1.skill.nlu.evaluations.pagination_context.PaginationContext',
        'links': 'ask_smapi_model.v1.skill.nlu.evaluations.links.Links',
        'evaluations': 'list[ask_smapi_model.v1.skill.nlu.evaluations.evaluation.Evaluation]'
    }  # type: Dict

    attribute_map = {
        'pagination_context': 'paginationContext',
        'links': '_links',
        'evaluations': 'evaluations'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, pagination_context=None, links=None, evaluations=None):
        # type: (Optional[Evaluations_PaginationContextV1], Optional[Evaluations_LinksV1], Optional[List[Evaluations_EvaluationV1]]) -> None
        """response body for a list evaluation API

        :param pagination_context: 
        :type pagination_context: (optional) ask_smapi_model.v1.skill.nlu.evaluations.pagination_context.PaginationContext
        :param links: 
        :type links: (optional) ask_smapi_model.v1.skill.nlu.evaluations.links.Links
        :param evaluations: 
        :type evaluations: (optional) list[ask_smapi_model.v1.skill.nlu.evaluations.evaluation.Evaluation]
        """
        self.__discriminator_value = None  # type: str

        super(ListNLUEvaluationsResponse, self).__init__(pagination_context=pagination_context, links=links)
        self.evaluations = evaluations

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, ListNLUEvaluationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
