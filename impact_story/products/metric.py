from datetime import datetime


class Metric:
    def __init__(self, raw_metrics):
        self._audience = str(raw_metrics.get('audience', ""))
        self._display_count = int(raw_metrics.get('display_count', 0))
        self._display_interaction = str(raw_metrics.get('display_interaction', ""))
        self._display_order = int(raw_metrics.get('display_order', 0))
        self._display_provider = str(raw_metrics.get('display_provider', ""))
        self._engagement_type = str(raw_metrics.get('engagement_type', ""))
        self._hide_badge = bool(raw_metrics.get('hide_badge', False))
        self._interaction = str(raw_metrics.get('interaction', ""))
        self._is_highly = bool(raw_metrics.get('is_highly', False))
        self._milestone_just_reached = raw_metrics.get('milestone_just_reached', None)
        self._can_diff = bool(raw_metrics.get('can_diff', False))
        self._latest_nonzero_refresh_timestamp = raw_metrics.get('latest_nonzero_refresh_timestamp', None)
        if self._latest_nonzero_refresh_timestamp:
            datetime.strptime(str(self._latest_nonzero_refresh_timestamp), "%Y-%m-%dT%H:%M:%S.%f")
        self._percentile_value_string = raw_metrics.get('percentile_value_string', None)
        self._provider_name = str(raw_metrics.get('provider_name', ""))
        self._diff_value = raw_metrics.get('diff_value', None)
        self._diff_window_length = raw_metrics.get('diff_window_length', None)
        self._drilldown_url = str(raw_metrics.get('drilldown_url', ""))
        self._fully_qualified_metric_name = str(raw_metrics.get('fully_qualified_metric_name', ""))
        self._percentile = raw_metrics.get('percentile', None)
        if self._percentile:
            self._parse_percentiles(self._percentile)

        # unique attributes in most_recent_snap
        self._most_recent_snap = dict(raw_metrics.get('most_recent_snap', {}))
        self._collected_date = self._most_recent_snap.get('collected_date', None)
        if self._collected_date:
            datetime.strptime(str(self._collected_date), "%Y-%m-%dT%H:%M:%S.%f")
        # depending on metric type, value can be list or int
        self._value = self._most_recent_snap.get('value', None)

        # metrics from first snap
        self._window_start_snap = raw_metrics.get('window_start_snap', None)
        if self._window_start_snap:
            self._value = self._window_start_snap.get('value', None)
            self._collected_date = self._window_start_snap.get('collected_date', None)
            if self._collected_date:
                datetime.strptime(str(self._collected_date), "%Y-%m-%dT%H:%M:%S.%f")
            self._start_percentile = self._window_start_snap.get('percentile', None)
            if self._start_percentile:
                # depending on metric type, value can be list or int
                self._start_percentile_value = self._start_percentile.get('value', None)

    def _parse_percentiles(self, percentiles):
        self._host = str(percentiles.get('host', ""))
        self._mendeley_discipline = percentiles.get('mendeley_discipline', None)
        self._provider = str(percentiles.get('provider', ""))
        # depending on metric type, value can be list or int
        self._percentile_value = percentiles.get('provider', None)

    def __str__(self):
        return ("\naudience: " + str(self._audience)
                + "\ndisplay_count: " + str(self._display_count)
                + "\ndisplay_interaction: " + str(self._display_interaction)
                + "\ndisplay_order: " + str(self._display_order)
                + "\ndisplay_provider: " + str(self._display_provider)
                + "\nengagement_type: " + str(self._engagement_type)
                + "\nhide_badge: " + str(self._hide_badge)
                + "\ninteraction: " + str(self._interaction)
                + "\nis_highly: " + str(self._is_highly)
                + "\nlatest_nonzero_refresh_timestamp: "
                + str(self._latest_nonzero_refresh_timestamp)
                + "\npercentile: " + str(self._percentile)
               	+ "\npercentile_value_string: " + str(self._percentile_value_string)
                + "\nprovider_name: " + str(self._provider_name)
                + "\ndiff_value: " + str(self._diff_value)
                + "\ndiff_window_length: " + str(self._diff_window_length)
                + "\ndrilldown_url: " + str(self._drilldown_url)
                + "\nfully_qualified_metric_name: " + str(self._fully_qualified_metric_name)
                + "\nlast_collected_date: " + str(self._collected_date)
                + "\nvalue: " + str(self._value))

    @property
    def audience(self):
        return self._audience

    @property
    def display_count(self):
        return self._display_count

    @property
    def display_interaction(self):
        return self._display_interaction

    @property
    def display_order(self):
        return self._display_order

    @property
    def display_provider(self):
        return self._display_provider

    @property
    def engagement_type(self):
        return self._engagement_type

    @property
    def hide_badge(self):
        return self._hide_badge

    @property
    def interaction(self):
        return self._interaction

    @property
    def is_highly(self):
        return self._is_highly

    @property
    def latest_nonzero_refresh_timestamp(self):
        return self._latest_nonzero_refresh_timestamp

    @property
    def host(self):
        return self._host

    @property
    def mendeley_discipline(self):
        return self._mendeley_discipline

    @property
    def provider(self):
        return self._provider

    @property
    def percentile_value_string(self):
        return self._percentile_value_string

    @property
    def provider_name(self):
        return self._provider_name

    @property
    def diff_value(self):
        return self._diff_value

    @property
    def diff_window_length(self):
        return self._diff_window_length

    @property
    def drilldown_url(self):
        return self._drilldown_url

    @property
    def fully_qualified_metric_name(self):
        return self._fully_qualified_metric_name

    @property
    def last_collected_date(self):
        return self._collected_date

    # number of [interaction] in [host]
    @property
    def value(self):
        return self._value

    @property
    def most_recent_snap(self):
        return self._most_recent_snap

    @property
    def percentile(self):
        return self._percentile
