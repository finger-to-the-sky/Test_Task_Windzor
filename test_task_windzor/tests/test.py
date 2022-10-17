import pytest
from test_task_windzor.сonversion.converter import FromGoogleCSVtoJSON

list_links = ['https://www.google.com/search?q=cats&biw=1920&bih=948&sxsrf=ALiC'
              'zsZoBW7e8XOxqJL1z6LMEq1WRCD2Ow%3A1666019602524&ei=EnFNY_bTH_Hwrw'
              'Tg8rOwDw&ved=0ahUKEwj2pOPUxuf6AhVx-IsKHWD5DPY4ChDh1QMIDg&uact=5&'
              'oq=cats&gs_lcp=Cgdnd3Mtd2l6EAMyCgguELEDENQCEEMyBAguEEMyDQguELEDE'
              'NQCEEMQiwMyCAgAEIAEEIsDMggIABCABBCLAzIFCAAQgAQyBQgAEIAEMgUIABCAB'
              'DIFCAAQgAQyCAguEIAEENQCOgcIIxDqAhAnOgQIIxAnOgQIABBDOgsIABCABBCx'
              'AxCDAToOCC4QgAQQsQMQxwEQ0QM6EQguEIAEELEDEIMBEMcBENEDOhAILhCxAxCD'
              'ARDHARDRAxBDOgoILhCABBCHAhAUOgoIABCxAxCDARBDOgcIABBDEIsDOgsILhCA'
              'BBDHARCvAToOCC4QgAQQsQMQgwEQ1AI6CAgAEIAEELEDOgcIABCxAxBDOg4IABCA'
              'BBCxAxCDARCLAzoUCC4QgAQQsQMQgwEQxwEQ0QMQiwM6CwgAELEDEIMBEIsDOhEI'
              'LhCABBDUAhCLAxCeAxCoAzoLCAAQgAQQsQMQiwNKBAhBGABKBAhGGABQqgpYsxRg'
              '-BVoAnABeACAAZUBiAGbBZIBAzAuNZgBAKABAbABCrgBA8ABAQ&sclient=gws-'
              'wiz',
              'sdfs',
              'https://www.youtube.com/']


@pytest.mark.parametrize('path', list_links)
def test_parse_method_url(path):
    test_converter = FromGoogleCSVtoJSON(path, ['date', 's'], 'ttt')
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        test_converter.parse()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 44


