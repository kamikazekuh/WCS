# ../wcs/core/menus/__init__.py

# ============================================================================
# >> IMPORTS
# ============================================================================
# Source.Python Imports
#   Menus
from menus import SimpleMenu
from menus.radio import MAX_ITEM_COUNT

# WCS Imports
#   Menus
from .base import PagedMenu
from .base import PagedPageCountMenu


# ============================================================================
# >> ALL DECLARATION
# ============================================================================
__all__ = ()


# ============================================================================
# >> GLOBAL VARIABLES
# ============================================================================
main_menu = SimpleMenu()
shopmenu_menu = PagedPageCountMenu()
shopinfo_menu = PagedPageCountMenu()
shopinfo_detail_menu = SimpleMenu()
showskills_menu = PagedMenu()
resetskills_menu = SimpleMenu()
spendskills_menu = PagedMenu()
changerace_menu = PagedPageCountMenu()
raceinfo_menu = PagedPageCountMenu()
raceinfo_detail_menu = SimpleMenu()
raceinfo_skills_menu = PagedMenu()
raceinfo_skills_detail_menu = SimpleMenu()
raceinfo_race_detail_menu = SimpleMenu()
playerinfo_menu = PagedPageCountMenu()
playerinfo_detail_menu = SimpleMenu()
playerinfo_detail_skills_menu = PagedMenu()
playerinfo_detail_stats_menu = SimpleMenu()
wcstop_menu = PagedPageCountMenu()
wcstop_detail_menu = SimpleMenu()
wcshelp_menu = SimpleMenu()
welcome_menu = SimpleMenu()
wcsadmin_menu = SimpleMenu()
wcsadmin_management_menu = SimpleMenu()
wcsadmin_management_races_menu = PagedPageCountMenu()
wcsadmin_management_items_menu = PagedPageCountMenu()
wcsadmin_management_races_add_menu = PagedPageCountMenu()
wcsadmin_management_items_add_menu = PagedPageCountMenu()
wcsadmin_management_races_editor_menu = SimpleMenu()
wcsadmin_management_items_editor_menu = SimpleMenu()
wcsadmin_management_race_categories_menu = PagedPageCountMenu()
wcsadmin_management_item_categories_menu = PagedPageCountMenu()
wcsadmin_github_menu = SimpleMenu()
wcsadmin_github_races_menu = PagedMenu()
wcsadmin_github_items_menu = PagedMenu()
wcsadmin_github_options_menu = SimpleMenu()

shopmenu_menu.parent_menu = main_menu
shopinfo_menu.parent_menu = main_menu
showskills_menu.parent_menu = main_menu
spendskills_menu.parent_menu = main_menu
changerace_menu.parent_menu = main_menu
raceinfo_menu.parent_menu = main_menu
raceinfo_skills_menu.parent_menu = raceinfo_detail_menu
playerinfo_menu.parent_menu = main_menu
playerinfo_detail_skills_menu.parent_menu = playerinfo_detail_menu
playerinfo_detail_stats_menu.parent_menu = playerinfo_detail_menu
wcsadmin_management_races_menu.parent_menu = wcsadmin_management_menu
wcsadmin_management_items_menu.parent_menu = wcsadmin_management_menu
wcsadmin_management_races_add_menu.parent_menu = wcsadmin_management_races_menu
wcsadmin_management_items_add_menu.parent_menu = wcsadmin_management_items_menu
wcsadmin_management_race_categories_menu.parent_menu = wcsadmin_management_menu
wcsadmin_management_item_categories_menu.parent_menu = wcsadmin_management_menu
wcsadmin_github_races_menu.parent_menu = wcsadmin_github_menu
wcsadmin_github_items_menu.parent_menu = wcsadmin_github_menu


# ============================================================================
# >> FUNCTIONS
# ============================================================================
def _get_current_options(menu, client):
    page = menu.get_player_page(client)
    start = page * MAX_ITEM_COUNT
    end = (page + 1) * MAX_ITEM_COUNT

    return menu[start:end]
