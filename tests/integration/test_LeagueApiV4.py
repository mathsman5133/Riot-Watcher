import sys

import pytest

if sys.version_info > (3, 0):
    import unittest.mock as mock
else:
    import mock


@pytest.mark.integration
@pytest.mark.parametrize(
    "region",
    [
        "br1",
        "eun1",
        "euw1",
        "jp1",
        "kr",
        "la1",
        "la2",
        "na",
        "na1",
        "oc1",
        "tr1",
        "ru",
        "pbe1",
    ],
)
class TestLeagueApiV4(object):
    @pytest.mark.parametrize(
        "queue", ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
    )
    def test_challenger_by_queue(self, mock_context, region, queue):
        actual_response = mock_context.watcher.league.challenger_by_queue(region, queue)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}".format(
                region=region, queue=queue
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "queue", ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
    )
    def test_grandmaster_by_queue(self, mock_context, region, queue):
        actual_response = mock_context.watcher.league.grandmaster_by_queue(
            region, queue
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}".format(
                region=region, queue=queue
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "queue", ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
    )
    def test_masters_by_queue(self, mock_context, region, queue):
        actual_response = mock_context.watcher.league.masters_by_queue(region, queue)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}".format(
                region=region, queue=queue
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize("league_id", [1, 500, 99999999999999])
    def test_by_id(self, mock_context, region, league_id):
        actual_response = mock_context.watcher.league.by_id(region, league_id)

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/leagues/{league_id}".format(
                region=region, league_id=league_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "encrypted_summoner_id",
        ["50", "424299938281", "9999999999999999999999", "rtbf12345"],
    )
    def test_by_summoner(self, mock_context, region, encrypted_summoner_id):
        actual_response = mock_context.watcher.league.by_summoner(
            region, encrypted_summoner_id
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrypted_summoner_id}".format(
                region=region, encrypted_summoner_id=encrypted_summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "queue", ["RANKED_SOLO_5x5", "RANKED_FLEX_SR", "RANKED_FLEX_TT"]
    )
    @pytest.mark.parametrize("tier", ["IRON", "SILVER", "DIAMOND"])
    @pytest.mark.parametrize("division", ["I", "IV"])
    @pytest.mark.parametrize("page", [2, 420])
    def test_entries(self, mock_context, region, queue, tier, division, page):
        actual_response = mock_context.watcher.league.entries(
            region, queue, tier, division, page=page
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}".format(
                region=region, queue=queue, tier=tier, division=division
            ),
            params={"page": page},
            headers={"X-Riot-Token": mock_context.api_key},
        )

    @pytest.mark.parametrize(
        "encrypted_summoner_id",
        ["50", "424299938281", "9999999999999999999999", "rtbf12345"],
    )
    def test_positions_by_summoner(self, mock_context, region, encrypted_summoner_id):
        actual_response = mock_context.watcher.league.positions_by_summoner(
            region, encrypted_summoner_id
        )

        assert mock_context.expected_response == actual_response
        mock_context.get.assert_called_once_with(
            "https://{region}.api.riotgames.com/lol/league/v4/positions/by-summoner/{encrypted_summoner_id}".format(
                region=region, encrypted_summoner_id=encrypted_summoner_id
            ),
            params={},
            headers={"X-Riot-Token": mock_context.api_key},
        )
