from unittest import TestCase
import json
from impact_story.products.metric import Metric

__author__ = 'ericabaranski'


class TestMetric(TestCase):
    def setUp(self):
        raw_json = open("./fixtures/HeatherPiwowar_070914.json")
        raw_dict = json.load(raw_json)
        product_list = raw_dict.get("products")
        product_object = product_list[5]

        metrics = []
        metric_list = product_object.get('metrics', None)
        for metric in metric_list:
            metrics.append(Metric(metric))
        self.m = metrics[0]

        #change to assertEquals tests to check values
        '''
        self.assertTrue(self.m._audience)
        self.assertTrue(self.m._display_count)
        self.assertTrue(self.m._display_interaction)
        self.assertTrue(self.m._display_order)
        self.assertTrue(self.m._display_provider)
        self.assertTrue(self.m._engagement_type)
        self.assertFalse(self.m._hide_badge)
        self.assertTrue(self.m._interaction)
        self.assertFalse(self.m._is_highly)
        self.assertTrue(self.m._latest_nonzero_refresh_timestamp)
        self.assertFalse(self.m._provenance_url)
        self.assertTrue(self.m._provider_name)
        self.assertFalse(self.m._top_percentile)
        self.assertFalse(self.m._metrics_raw_sum)
        self.assertFalse(self.m._update_status)
        self.assertFalse(self.m._diff_value)
        self.assertTrue(self.m._diff_window_length)
        self.assertTrue(self.m._drilldown_url)
        self.assertTrue(self.m._fully_qualified_metric_name)
        self.assertTrue(self.m._most_recent_snap)
        self.assertTrue(self.m._milestone_just_reached)
        self.assertTrue(self.m._can_diff)
        self.assertTrue(self.m._window_start_snap)
        '''

    def test__parse_percentiles(self):
        percentiles = self.m.percentiles
        Metric._parse_percentiles(self.m, percentiles)

        #change to assertEquals tests to check values
        '''
        self.assertFalse(self.m._host)
        self.assertFalse(self.m._mendeley_discipline)
        self.assertFalse(self.m._provider)
        self.assertFalse(self.m._value)
        '''