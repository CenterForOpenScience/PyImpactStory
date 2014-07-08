from unittest import TestCase
import json
from impact_product import Metric

__author__ = 'ericabaranski'


class TestMetric(TestCase):
    def setUp(self):
        raw_json = open("Heather_metric")
        raw_dict = json.load(raw_json)
        metric_list = raw_dict.get("metrics")
        self.m = Metric(metric_list[0])

        self.assertTrue(self.m._audience)
        self.assertTrue(self.m._display_count)
        self.assertTrue(self.m._display_interaction)
        self.assertTrue(self.m._display_order)
        self.assertTrue(self.m._display_provider)
        self.assertTrue(self.m._engagement_type)
        self.assertFalse(self.m._hide_badge)
        self.assertTrue(self.m._interaction)
        self.assertTrue(self.m._is_highly)
        self.assertTrue(self.m._latest_nonzero_refresh_timestamp)
        self.assertTrue(self.m._provider_name)
        self.assertFalse(self.m._diff_value)
        self.assertTrue(self.m._diff_window_length)
        self.assertTrue(self.m._drilldown_url)
        self.assertTrue(self.m._fully_qualified_metric_name)
        self.assertTrue(self.m._most_recent_snap)
        self.assertTrue(self.m._collected_date)
        self.assertTrue(self.m._value)


    def test__parse_percentiles(self):
        percentile = self.m.percentile
        Metric._parse_percentiles(self.m, percentile)

        self.assertTrue(self.m._host)
        self.assertFalse(self.m._mendeley_discipline)
        self.assertTrue(self.m._provider)
