from robograph.datamodel.nodes.lib import clock


def check_date(year, month, day):
    assert len(year) == 4
    assert len(month) == 2
    m = int(month)
    assert 1 <= m <= 12
    assert len(day) == 2
    d = int(day)
    assert 1 <= d <= 31


def check_time(hours, minutes, seconds):
    assert len(hours) == 2
    hh = int(hours)
    assert 0 <= hh <= 23
    assert len(minutes) == 2
    mm = int(minutes)
    assert 0 <= mm <= 59
    assert len(seconds) == 2
    ss = int(seconds)
    assert 0 <= ss <= 59


def test_date():
    instance = clock.Date()
    assert instance.requirements == []
    result = instance.output()
    year, month, day = result.split('-')
    check_date(year, month, day)


def test_formatted_date():
    expected_reqs = ['format']
    instance = clock.FormattedDate()
    assert instance.requirements == expected_reqs
    instance.input(dict(format='%Ybla%mbla%d'))
    result = instance.output()
    year, month, day = result.split('bla')
    check_date(year, month, day)


def test_now():
    instance = clock.Now()
    assert instance.requirements == []
    result = instance.output()
    d, t = result.split('T')
    year, month, day = d.split('-')
    check_date(year, month, day)
    hours, minutes, seconds = t.split(':')
    check_time(hours, minutes, seconds)


def test_utc_now():
    instance = clock.UtcNow()
    assert instance.requirements == []
    result = instance.output()
    d, t = result.split('T')
    year, month, day = d.split('-')
    check_date(year, month, day)
    hours, minutes, seconds = t.split(':')
    check_time(hours, minutes, seconds)



